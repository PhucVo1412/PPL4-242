'''
2252650 
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *


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
    def accept(self, v, param):
        return v.visitClassType(self, param)

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass" 
        self.astTree = None
        self.path = None
        self.emit = None
        self.function = None
        self.list_function = []
        self.arrayCell = None
        self.arrayCellType = None

    def init(self):
        mem = [ Symbol("getInt",MType([],IntType()),CName("io",True)),
                Symbol("putInt",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("putIntLn",MType([IntType()],VoidType()),CName("io",True)),
                Symbol("getFloat",MType([],FloatType()),CName("io",True)),
                Symbol("putFloat",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("putFloatLn",MType([FloatType()],VoidType()),CName("io",True)),
                Symbol("getBool",MType([],BoolType()),CName("io",True)),
                Symbol("putBool",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("putBoolLn",MType([BoolType()],VoidType()),CName("io",True)),
                Symbol("getString",MType([],StringType()),CName("io",True)),
                Symbol("putString",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putStringLn",MType([StringType()],VoidType()),CName("io",True)),
                Symbol("putLn",MType([],VoidType()),CName("io",True)),
                ]
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
    
    def emitObjectCInit(self, ast, env):
        frame = Frame("<cinit>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        self.visit(Block([Assign(Id(item.varName), item.varInit) for item in ast.decl if isinstance(item, VarDecl) and item.varInit]  ),env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def visitProgram(self, ast, c):
        self.fun_list = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
        
        env = {}
        env['env'] = [c]

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or  isinstance(x, ConstDecl) else a, ast.decl, env)

        reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)

        self.emitObjectInit()
        self.emitObjectCInit(ast,env)

        self.emit.printout(self.emit.emitEPILOG())

        return env

    def visitParamDecl(self,ast, o):
        # parName: str
        # parType: Type
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index)))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame))     
        return o


    def visitVarDecl(self, ast, o):
        # varName : str
        # varType : Type # None if there is no type
        # varInit : Expr # None if there is no initialization
        def create_init(varType, o):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("\"\"")
            elif type(varType) is BoolType:
                return BooleanLiteral("false")
            elif type(varType) is ArrayType:
                pass #TODO


        varInit = ast.varInit 
        varType = ast.varType 

        if not varInit:
            varInit = create_init(varType, o)
            if type(varType) is ArrayType:
                varInit = ArrayLiteral(varType.dimens, varType.dimens, varInit)
            ast.varInit = varInit


            ast.varInit = varInit
        env = o.copy()
        env['frame'] = Frame("<template_VT>", VoidType()) 

        rhsCode, rhsType = self.visit(varInit, env)

        if not varType:
            varType = rhsType

        if 'frame' not in o: # TH global var 
            o['env'][0].append(Symbol(ast.varName, varType, CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
        else:
            frame = o['frame']

            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType, Index(index))) 


            self.emit.printout(self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(frame) 
                  
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index, frame))                   
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

        self.fun = ast

        frame = Frame(ast.name, ast.retType)

        isMain = ast.name == "main"
        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            ast.body = Block([] + ast.body.member)
        else:
            mtype = MType(list(map(lambda x: x.parType, ast.params)), ast.retType)

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
        return ast

    def visitFloatType(self, ast, o):
        return ast

    def visitBoolType(self, ast, o):
        return ast

    def visitStringType(self, ast, o):
        return ast

    def visitVoidType(self, ast, o):
        return ast

    def visitArrayType(self, ast, o):
        # arr:Expr
        # idx:List[Expr]
        codeGen = ""
        # TODO : Lặp qua dimens để thêm code vào codeGen, dùng visit và lưu ý rằng visit sẽ trả về cặp mã và kiểu của nó.
        # Cuối cùng đủ tham số thì dùng emitMULTIANEWARRAY để tạo mảng mới.
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])
        return codeGen, ast

    
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

        for stmt in ast.member:
            if type(stmt) is FuncCall:
                env['stmt'] = True
            env = self.visit(stmt,env)


        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o

    def visitAssign(self, ast, o):
        # lhs: LHS
        # rhs: Expr 
        if type(ast.lhs) is Id and not next(filter(lambda x: x.name == ast.lhs.name, [sym for env in o['env'] for sym in env]), None) :
            return self.visit(VarDecl(ast.lhs.name,None,ast.rhs),o)

        
        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o) 
        o['isLeft'] = False

        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhscode += self.emit.emitI2F(o['frame'])
        o['frame'].push()
        self.emit.printout(rhsCode)
        self.emit.printout(lhsCode)
        return o


        # if type(ast.lhs) is ArrayCell:
        #     self.emit.printout(code1)
        #     self.emit.printout(rhsCode)
        #     self.emit.printout(self.emit.emitASTORE("TODO")) # lưu vào mảng, truyền vào mảng và o['frame'].Gợi ý, khi visit lhs ta có visitAarrayCell và dùng self.. để lưu mảng đang xét
        # # access id
        # else:
        #     self.emit.printout(rhsCode)
        #     self.emit.printout(lhsCode)

        # return o


        return o


    
    def visitIf(self, ast, o):
        #  expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt # None if there is no else
        code,typ = self.visit(ast.expr,o)
        self.emit.printout(code)

        Label0 = o['frame'].getNewLabel()
        if ast.elseStmt:
            Label1 = o['frame'].getNewLabel()

        code = self.emit.emitIFFALSE(Label0,o['frame'])
        self.emit.printout(code)

        self.visit(ast.thenStmt,o)

        if ast.elseStmt:    
            code = self.emit.emitGOTO(Label1,o['frame'])

        self.emit.emitLABEL(Label0,o['frame'])

        if ast.elseStmt:
            self.visit(self.elseStmt,o['frame'])

        self.emit.emitLABEL(Label1,o['frame'])
        return o



    def visitForBasic(self, ast, o):
        # cond:Expr
        # loop:Block
        o['frame'].enterLoop()
        ConLabel = o['frame'].getContinueLabel()
        BreakLabel = o['frame'].getBreakLable()

        code = self.emit.emitLABEL(ConLabel)
        self.emit.printout(code)

        code,typ = self.visit(ast.cond,o)
        self.emit.printout(code)

        code = self.emit.emitIFFALSE(BreakLabel,o['frame'])

        self.visit(ast.loop,o['frame'])

        code = self.emit.emitGOTO(ConLabel,o['frame'])
        self.emit.printout(code)

        self.emit.emitLABEL(BreakLabel)
        o['frame'].exitLoop()
        return o

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
        return o

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getBreakLabel(), o['frame']))
        return o

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o['frame'].getContinueLabel(), o['frame']))
        return o

    def visitReturn(self, ast, o):
        #expr:Expr 
        if ast.expr:
            self.emit.printout(self.visit(ast.expr, o)[0])
        self.emit.printout(self.emit.emitRETURN(self.visit(ast.expr, o)[1],o['frame']))
        return o

    def visitId(self, ast, o):
        #name : str
        sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)
        if o.get('isLeft'):
            if type(sym.value) is Index: 
                return self.emit.emitWRITEVAR(ast.name, sym.mtype, sym.value.value, o['frame']), sym.mtype
            else:         
                #Putstatic là ghi vào biến static,
                return self.emit.emitPUTSTATIC(f"{sym.value.value}/{sym.name}",sym.mtype,o['frame']),sym.mtype  
            
        if type(sym.value) is Index: 
            return self.emit.emitREADVAR(ast.name, sym.mtype, sym.value.value, o['frame']) , sym.mtype 
        else:         
            return self.emit.emitGETSTATIC(f"{sym.value.value}/{sym.name}",  sym.mtype, o['frame']),sym.mtype 
        


    def visitArrayCell(self, ast: ArrayCell, o: dict) -> tuple[str, Type]:
        newO = o.copy()
        newO['isLeft'] = False ## kiểm tra xem đang bên nào
        code, typ = self.visit(ast.arr, o) 

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item,o)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        # retType = None
        # ## trả về một kiểu nào đó không phải array
        # if len(arrType.dimens) == len(ast.idx):
        #     retType = ## TODO
        #     if not o.get('isLeft'):
        #         codeGen += ## TODO
        #     else:
        #         self.arrayCell = ## TODO
        # ## trả về một array
        # else:
        #     retType = ## TODO
        #     if not o.get('isLeft'):
        #         codeGen += ## TODO
        #     else:
        #         self.arrayCell = ## TODO

        return code,typ

    def visitFieldAccess(self, ast, o):
        # receiver:Expr
        # field:str
        pass

    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
       
        op = ast.op
        frame = o['frame']
        codeLeft, typeLeft = self.visit(ast.left, o)
        codeRight, typeRight = self.visit(ast.right, o)
        if op in ['+', '-'] and type(typeLeft) in [FloatType, IntType]:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                elif type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitADDOP(op,typeReturn,frame),typeReturn 
        if op in ['*', '/']:
            typeReturn = IntType() if type(typeLeft) is IntType and type(typeRight) is IntType else FloatType()
            if type(typeReturn) is FloatType:
                if type(typeLeft) is IntType:
                    codeLeft += self.emit.emitI2F(frame)
                elif type(typeRight) is IntType:
                    codeRight += self.emit.emitI2F(frame)
            return codeLeft + codeRight + self.emit.emitMULOP(op,typeReturn,frame),typeReturn 
        if op in ['%']:
            return codeLeft + codeRight +  self.emit.emitMOD(frame), typeLeft
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [FloatType, IntType]:
            return codeLeft + codeRight +  self.emit.emitREOP(op,typeLeft, frame),BoolType()
        if op in ['||']:
            return codeLeft + codeRight +   self.emit.emitOROP(op,typeLeft, frame),BoolType()
        if op in ['&&']:
            return codeLeft + codeRight + self.emit.emitANDOP(frame), BoolType() 

        # nối string string        
        if op in ['+', '-'] and type(typeLeft) in [StringType]:
            return codeLeft + codeRight + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()],StringType()),frame)  , StringType()  
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(typeLeft) in [StringType]:
            code = codeLeft + codeRight + self.emit.emitREOP(op, typeLeft, frame)
            return code, BoolType()    
        
    def visitUnaryOp(self, ast, o):
        # op:str
        # body:Expr
        
        if ast.op == '!':
            code, typ = self.visit(ast.body, o)
            return code + self.emit.emitNOT(BoolType(), o['frame']), BoolType()
        
        code, typ = self.visit(ast.body, o)
        return code + self.emit.emitNEGOP(typ, o['frame']),typ

    def visitFuncCall(self, ast, o):
            # funName:str
            # args:List[Expr] # [] if there is no arg 

        sym = next(filter(lambda x: x.name == ast.funName, self.fun_list),None)
        if o.get('stmt'):
            o["stmt"] = False
            output = "".join([str(self.visit(x,o)[0]) for x in ast.args])
            self.emit.printout(output)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            return o 
        
        output = "".join([str(self.visit(x, o)[0]) for x in ast.args])
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])

        # Vì funcall ở chỗ này là 1 biểu thức nên mình cần trả về giá trị kèm theo kiểu trả về luôn.
        return output, sym.mtype.rettype

    def visitMethCall(self, ast, o):
        # receiver: Expr
        # metName: str
        # args:List[Expr]

        pass

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value,o['frame']),IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value),o['frame']),FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(str(ast.value),StringType(),o['frame']),StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(int(ast.value), o['frame']), BoolType()
    
    def visitArrayLiteral(self, ast, o):
        # dimens:List[Expr]
        # eleType: Type
        # value: NestedList
        def nested2recursive(dat: Union[Literal, list['NestedList']], o: dict) -> tuple[str, Type]:
            if not isinstance(dat,list): 
                return ## TODO
            
            frame = o['frame']
            codeGen = self.emit.emitPUSHICONST(len(ast.dimens), o['frame'] )
            # trường hợp mảng một chiều   
            if not isinstance(dat[0],list):
                codeGen += self.emit.emitNEWARRAY(ast.eleType,o['frame'])
                _ , type_element_array = self.visit(dat[0], o)
                
                for idx, item in enumerate(dat):
                    codeGen += self.emit.emitDUP(o['frame'])
                    codeGen += self.emit.emitPUSHICONST(idx,o['frame'])
                    codeGen += self.visit(item, o)[0] 
                    codeGen += self.emit.emitASTORE(type_element_array, o['frame'])
                return codeGen, ArrayType(ast.dimens,ast.eleType)
            
            # trường hợp mảng 2 chiều 
            codeGen += self.emit.emitANEWARRAY(ast.eleType,o['frame'])
            _, type_element_array = nested2recursive(dat[0], o)
            for idx, item in enumerate(dat):
                codeGen += self.emit.emitDUP(o['frame'])
                codeGen += self.emit.emitPUSHICONST(idx,o['frame'])
                codeGen += nested2recursive(item, o)
                codeGen += self.emit.emitASTORE(type_element_array, o['frame'])
            return  codeGen, ArrayType(ast.dimens,ast.eleType)
        
        return nested2recursive(ast.value, o) 

 

    def visitStructLiteral(self, ast, o):
        #name:str
        #elements: List[Tuple[str,Expr]]
        pass

    def visitNilLiteral(self, ast, o):
        pass


    
