'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce


class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value,isStatic=True):
        #value: String
        self.isStatic = isStatic
        self.value = value

class ClassType(Type):
    def __init__(self, name):
        #value: Id
        self.name = name

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass"
        self.astTree = None
        self.path = None
        self.emit = None

    def init(self):
        mem = [Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True))]
        return mem

    def gen(self, ast, dir_):
        gl = self.init()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emitObjectInit(self):
        frame = Frame("<init>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  # Bắt đầu định nghĩa phương thức <init>
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  

    def visitProgram(self, ast, c):
        env ={}
        env['env'] = [c]
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a,x: self.visit(x,a), ast.decl, env)
        self.emitObjectInit()
        self.emit.printout(self.emit.emitEPILOG())
        return env

    def visitParamDecl(self,ast, o):
        # parName: str
        # parType: Type
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel(), frame.getEndLabel(), frame))  


    def visitVarDecl(self, ast, o):
        # varName : str
        # varType : Type # None if there is no type
        # varInit : Expr # None if there is no initialization

        if 'frame' not in o: # global var
            o['env'][0].append(Symbol(ast.varName, ast.varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, str(ast.varInit.value) if ast.varInit else None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, ast.varType, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            if ast.varInit:
                self.emit.printout(self.emit.emitPUSHICONST(ast.varInit.value, frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index,  frame))
        return o

    
    def visitConstDecl(self, ast, o):
        # conName : str
        # conType : Type # None if there is no type 
        # iniExpr : Expr
        if 'frame' not in o: # global var
            o['env'][0].append(Symbol(ast.conName, ast.conType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, str(ast.iniExpr.value) if ast.iniExpr else None))
        else:
            frame = o['frame']
            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.conName, ast.conType, Index(index)))
            self.emit.printout(self.emit.emitVAR(index, ast.conName, ast.conType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            if ast.iniExpr:
                self.emit.printout(self.emit.emitPUSHICONST(ast.iniExpr.value, frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, index,  frame))
        return o

    def visitFuncDecl(self, ast, o):
        # name: str
        # params: List[ParamDecl]
        # retType: Type # VoidType if there is no return type
        # body: Block
        
        frame = Frame(ast.name, ast.retType)
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)
        o['env'][0].append(Symbol(ast.name, mtype, CName(self.className)))
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.name, mtype,True, frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        env['env'] = [[]] + env['env']
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([None],StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
        self.visit(ast.body,env)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitMethodDecl(self, ast, o):
        # receiver: str
        # recType: Type 
        # fun: FuncDecl
        pass
    
    def visitPrototype(self, ast, o):
        # name: str
        # params:List[Type]
        # retType: Type # VoidType if there is no return type

        pass    

    def visitIntType(self, ast, o):
        pass 

    def visitFloatType(self, ast, o):
        return ast

    def visitBoolType(self, ast, o):
        return ast

    def visitStringType(self, ast, o):
        return ast

    def visitVoidType(self, ast, o):
        return ast

    def visitArrayType(self, ast, o):
        return ast
    
    def visitStructType(self, ast, o):
        return ast

    def visitInterfaceType(self, ast, o):
        return ast

    def visitBlock(self, ast, o):
        #member:List[BlockMember]
        env = o.copy()
        env['env'] = [[]] + env['env']
        env['frame'].enterScope(False)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))
        env = reduce(lambda acc,e: self.visit(e,acc),ast.member,env)
        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o

    def visitAssign(self, ast, o):
        # lhs: LHS
        # rhs: Expr 
        o['isLeft'] = False
        code2,typ2 = self.visit(ast.rhs,o)

        o['isLeft'] = True
        code1,typ1 = self.visit(ast.lhs,o)
    
        code = code1 + code2
        self.emit.printout(code)


    
    def visitIf(self, ast, o):
        #  expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt # None if there is no else
        code,typ = self.visit(ast.expr,o)
        self.emit.printout(code)

        Label0 = o.frame.getNewLabel()
        if ast.elseStmt:
            Label1 = o.frame.getNewLabel()

        code = self.emit.emitIFFALSE(Label0,o.frame)
        self.emit.printout(code)

        self.visit(ast.thenStmt,o)

        if ast.elseStmt:    
            code = self.emit.emitGOTO(Label1,o.frame)

        self.emit.emitLABEL(Label0,o.frame)

        if ast.elseStmt:
            self.visit(self.elseStmt,o.frame)

        self.emit.emitLABEL(Label1,o.frame)



    def visitForBasic(self, ast, o):
        # cond:Expr
        # loop:Block
        o['frame'].enterLoop()
        ConLabel = o['frame'].getContinueLabel()
        BreakLabel = o['frame'].getBreakLable()

        code = self.emit.emitLABEL(ConLabel)
        self.emit.printout(code)

        code,typ = self.visit(ast.cond)
        self.emit.printout(code)

        code = self.emit.emitIFFALSE(BreakLabel,o['frame'])

        self.visit(ast.loop,o['frame'])

        code = self.emit.emitGOTO(ConLabel,o['frame'])
        self.emit.printout(code)

        self.emit.emitLABEL(BreakLabel)
        o['frame'].exitLoop()

    def visitForStep(self, ast, o):
        # init:Stmt
        # cond:Expr
        # upda:Assign
        # loop:Block
        o['frame'].enterLoop()

        ContinueLabel = o['frame'].getContinueLabel()
        BreakLabel = o['frame'].getBreakLabel()

        self.visit(ast.init,o)

        self.emit.printout(self.emit.emitLABEL(ContinueLabel,o['frame']))
        self.visit(ast.cond,o)
        self.emit.printout(self.emit.emitIFFALSE(BreakLabel,o['frame']))

        self.visit(ast.loop,o)
        self.visit(ast.upda,o)
        self.emit.printout(self.emit.emitGOTO(ContinueLabel, o['frame']))

        self.emit.printout(self.emit.emitLABEL(BreakLabel,o['frame']))

        o['frame'].exitLoop()

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))

    def visitReturn(self, ast, o):
        #expr:Expr 
        pass

    def visitId(self, ast, o):
        #name : str
        found = next(filter(lambda x: x.name == ast.name, o['env']), None)

        if isinstance(found.value, Index):
            code = self.emit.emitREADVAR(
                ast.name, 
                found.mtype, 
                found.value.value, 
                o.frame
            )
            return code, found.mtype
        
        elif isinstance(found.value, CName):
            code = self.emit.emitGETSTATIC(
                found.value.value + "/" + ast.name,  
                found.mtype, 
                o.frame
            )
            return code, found.mtype


    def visitArrayCell(self, ast, o):
        # arr:Expr
        # idx:List[Expr]
        pass

    def visitFieldAccess(self, ast, o):
        # receiver:Expr
        # field:str
        pass

    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
        leftCode, leftType = self.visit(ast.left, o)
        rightCode, rightType = self.visit(ast.right, o)
        code = leftCode + rightCode
        typ = leftType
        op = ast.op

        if op in ['+','-']:
            code += self.emit.emitADDOP(ast.op, leftType, o.frame)
        elif op in ['*','/']:   
            code += self.emit.emitMULOP(ast.op, leftType, o.frame)
        elif op == "%":
            code += self.emit.emitMOD(ast.op, leftType, o.frame)
        elif op in [">","<","==",">=","<="]:
            code += self.emit.emitREOP(ast.op, leftType, o.frame)
        return code,typ
        
    def visitUnaryOp(self, ast, o):
        # op:str
        # body:Expr
        
        code1,typ = self.visit(ast.body,o)
        code = ""
        if ast.op == '-':
            code += self.emit.emitPUSHICONST(0,o.frame)
            code += code1
            code += self.emit.emitADDOP(ast.op,typ, o.frame )
        elif ast.op == '!':
            code += self.emit.emitNOT(typ, o.frame)
        return code,typ

    def visitFuncCall(self, ast, o):
        # funName:str
        # args:List[Expr] 
        sym = next(filter(lambda x: x.name == ast.funName, o['env'][-1]),None)
        env = o.copy()
        env['isLeft'] = False
        [self.emit.printout(self.visit(x, env)[0]) for x in ast.args]
        self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
        return o

    def visitMethCall(self, ast, o):
        # receiver: Expr
        # metName: str
        # args:List[Expr]

        pass

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ctx.value,o.frame),IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ctx.value),o.frame),FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value,StringType(),o.frame),StringType()

    def visitBoolLiteral(self, ast, o):
        if ast.value:
            return self.emit.emitPUSHICONST(1,o.frame),IntType()
        return self.emit.emitPUSHICONST(0,o.frame),IntType()

    def visitArrayLiteral(self, ast, o):
        # dimens:List[Expr]
        # eleType: Type
        # value: NestedList
        pass


    def visitStructLiteral(self, ast, o):
        #name:str
        #elements: List[Tuple[str,Expr]]
        pass

    def visitNilLiteral(self, ast, o):
        pass


    
