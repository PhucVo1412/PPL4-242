'''
2252650 
'''
from Utils import *
# from StaticCheck import *
# from StaticError import *
from Emitter import *
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce
from Visitor import *
from AST import *


    
# class Val(ABC):
#     pass

# class Index(Val):
#     def __init__(self, value):
#         #value: Int

#         self.value = value

# class CName(Val):
#     def __init__(self, value,isStatic=True):
#         #value: String
#         self.isStatic = isStatic
#         self.value = value

# class ClassType(Type):
#     def __init__(self, name):
#         #value: Id
#         self.name = name
#     def accept(self, v, param):
#         return v.visitClassType(self, param)

    
class CodeGenerator(BaseVisitor,Utils):
    def __init__(self):
        self.className = "MiniGoClass" 
        self.astTree = None
        self.path = None
        self.emit = None
        self.currFunction = None
        self.list_function = []
        # self.arrayCell = None
        # self.arrayCellType = None
        self.structface_list = []
        self.currStruct = None

    def init_global_symbols(self):
        global_function = [ Symbol("getInt",MType([],IntType()),CName("io",True)),
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
        return global_function

    def gen(self, ast, dir_):
        gl = self.init_global_symbols()
        self.astTree = ast
        self.path = dir_
        self.emit = Emitter(dir_ + "/" + self.className + ".j")
        self.visit(ast, gl)
       
        
    def emit_default_constructor(self):
        frame = Frame("<Construct>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<init>", MType([], VoidType()), False, frame))  
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))  # Tạo biến "this" trong phương thức <init>
        
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))  
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  
    
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()  
    
    def emit_class_init(self, ast, env):
        frame = Frame("<C Construct>", VoidType())  
        self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([], VoidType()), True, frame)) 
        frame.enterScope(True)  
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        env['frame'] = frame
        self.visit(Block([Assign(Id(item.varName), item.varInit) for item in ast.decl if isinstance(item, VarDecl) and item.varInit]  +
                         [Assign(Id(item.conName), item.iniExpr) for item in ast.decl if isinstance(item, ConstDecl) and item.iniExpr]),env)
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))  
        self.emit.printout(self.emit.emitENDMETHOD(frame))  
        frame.exitScope()

    def visitProgram(self, ast, c):
        #decl : List[Decl]
        self.list_function = c + [Symbol(item.name, MType(list(map(lambda x: x.parType, item.params)), item.retType), CName(self.className)) for item in ast.decl if isinstance(item, FuncDecl)]
      
        self.structface_list += list([x for x in ast.decl if isinstance(x, (StructType,InterfaceType)) ])

        for item in ast.decl:
            if type(item) is MethodDecl:
                structName = item.recType.name
                structFound = self.lookup(structName, self.structface_list,lambda x: x.name)
                structFound.methods += [item]
            
                

        env = {}
        env['env'] = [c]

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, VarDecl) or  isinstance(x, ConstDecl) else a, ast.decl, env)

        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)

        self.emit_default_constructor()
        self.emit_class_init(ast,env)

        self.emit.printout(self.emit.emitEPILOG())

        for item in  self.structface_list:
            self.currStruct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, env)

        return env
    
    def visitParamDecl(self,ast, o):
        # parName: str
        # parType: Type
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index),IntLiteral(0) if type(ast.parType) is IntType else None))
        self.emit.printout(self.emit.emitVAR(index, ast.parName, ast.parType, frame.getStartLabel() ,frame.getEndLabel(), frame)) 

        return o

    def initialize(self,varType, o):
            if type(varType) is IntType:
                return IntLiteral(0)
            elif type(varType) is FloatType:
                return FloatLiteral(0.0)
            elif type(varType) is StringType:
                return StringLiteral("\"\"")
            elif type(varType) is BoolType:
                return BooleanLiteral(False)
            elif type(varType) is Id:
                structFound = self.lookup(varType.name, self.structface_list,lambda x:x.name)
                return StructLiteral(structFound.name,[])
            elif type(varType) is ArrayType:
                dimensions = varType.dimens

                if not dimensions:
                    return self.initialize(varType.eleType, o)

                dim_sizes = []
                for dim in dimensions:
                    if type(dim) is IntLiteral:
                        dim_sizes.append(dim.value)
                    elif type(dim) is Id:
                        sym = next(filter(lambda x: x.name == dim.name, [j for i in o['env'] for j in i]), None)
                        dim_sizes.append(sym.initValue.value) 
                    elif type(dim) is ArrayCell:
                        sym = next(filter(lambda x: x.name == dim.arr.name, [j for i in o['env'] for j in i]), None)
                        ids = []
                        for id in dim.idx:
                            ids += [id.value]

                        val = sym.initValue.value
                        for index in ids:
                            val = val[index]
                        dim_sizes.append(val.value) 
                        
                def build_array(dims, eleType):
                    if len(dims) == 1:
                        return [self.initialize(eleType, o) for _ in range(dims[0])]
                    else:
                        return [build_array(dims[1:], eleType) for _ in range(dims[0])]
                        
                # Generate the nested array structure
                elements = build_array(dim_sizes, varType.eleType)
                
                return ArrayLiteral(dimensions, varType.eleType, elements)


    def visitVarDecl(self, ast, o):
        # varName : str
        # varType : Type # None if there is no type
        # varInit : Expr # None if there is no initialization     

        if not ast.varInit:
            ast.varInit = self.initialize(ast.varType, o)
        

        env = o.copy()
        env['frame'] = Frame("<Mytemplate>", VoidType()) 

        rhsCode, rhsType = self.visit(ast.varInit, env)
        if not ast.varType :
            ast.varType = rhsType


        if 'frame' not in o:  
            o['env'][0].append(Symbol(ast.varName, ast.varType,CName(self.className), self.calculateIntLiteral(ast.varInit,o) if type(ast.varType) is IntType else ast.varInit))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, ast.varType, True, False, None))
        else:
            frame = o['frame']

            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, ast.varType,Index(index), self.calculateIntLiteral(ast.varInit,o) if type(ast.varType) is IntType else ast.varInit )) 
            self.emit.printout(self.emit.emitVAR(index, ast.varName, ast.varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            codeR, Rtyp = self.visit(ast.varInit, o)
            if type(ast.varType) is FloatType and type(Rtyp) is IntType:
                codeR += self.emit.emitI2F(frame) 
                  
            if type(ast.varType) is Id:
                self.emit.printout(codeR)
                self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame)) 
                return o
            self.emit.printout(codeR)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, ast.varType, index, frame))                   
        return o

    
    def visitConstDecl(self, ast, o) :
        # conName : str
        # conType : Type # None if there is no type
        # iniExpr : Expr # None if there is no initialization     
    
        if not ast.iniExpr:
            ast.iniExpr = self.initialize(ast.conType, o)
        

        env = o.copy()
        env['frame'] = Frame("<Mytemplate>", VoidType()) 

        rhsCode, rhsType = self.visit(ast.iniExpr, env)
        if not ast.conType :
            ast.conType = rhsType


        if 'frame' not in o:  
            o['env'][0].append(Symbol(ast.conName, ast.conType,CName(self.className), self.calculateIntLiteral(ast.iniExpr,o) if type(ast.conType) is IntType else ast.iniExpr))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.conName, ast.conType, True, True, None))
        else:
            frame = o['frame']

            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.conName, ast.conType,Index(index), self.calculateIntLiteral(ast.iniExpr,o) if type(ast.conType) is IntType else ast.iniExpr )) 
            self.emit.printout(self.emit.emitVAR(index, ast.conName, ast.conType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            codeR, Rtyp = self.visit(ast.iniExpr, o)
            if type(ast.conType) is FloatType and type(Rtyp) is IntType:
                codeR += self.emit.emitI2F(frame) 
                  
            if type(ast.conType) is Id:
                self.emit.printout(codeR)
                self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, index, frame)) 
                return o
            self.emit.printout(codeR)
            self.emit.printout(self.emit.emitWRITEVAR(ast.conName, ast.conType, index, frame))                   
        return o


    def visitFuncDecl(self, ast, o):
        # name: str
        # params: List[ParamDecl]
        # retType: Type # VoidType if there is no return type
        # body: Block

        self.fun = ast

        frame = Frame(ast.name, ast.retType)

        isMain = ast.name == "main"
        if isMain:
            mtype = MType([ArrayType([None],StringType())], VoidType())
            #ast.body = Block([] + ast.body.member)
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
        
        self.currFunction = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype,False, frame))
        frame.enterScope(True) 

        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),"this",Id(self.currStruct.name),env['frame'].getStartLabel(),env['frame'].getEndLabel(),env['frame'])) 

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id("java.lang.Object.super"), 0, frame))  
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  

        env['env'] = [[]] + env['env']
        env = reduce(lambda acc,e: self.visit(e,acc),ast.fun.params,env)  

        self.visit(ast.fun.body, env) 


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
    def visitPrototype(self, ast, o):
        # name: str
        # params:List[Type]
        # retType: Type # VoidType if there is no return type
        list_type = [param for param in ast.params if type(param)]
        retType = ast.retType if ast.retType else VoidType()

        return self.emit.emitABSTRACTMETHOD(ast.name, list_type, retType)
         

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
        #dimens:List[Expr]
        #eleType:Type
        return ast
    
    def visitStructType(self, ast, o):
        # name: str
        # elements:List[Tuple[str,Type]]
        # methods:List[MethodDecl]
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object"))

        for item in self.structface_list: 
            if type(item) is InterfaceType and self.compare2Type(item, ast, [(InterfaceType, StructType)]): 
                self.emit.printout(self.emit.emitIMPLEMENT(item.name)) 

        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(item[0],item[1], False, False, None))

        self.visit(MethodDecl(None, Id(ast.name), FuncDecl("<init>", [ParamDecl(item[0],item[1]) for item in ast.elements], VoidType(),                                             
                            Block([Assign(FieldAccess(Id("this"),item[0]),Id(item[0])) for item in ast.elements]))), o)   
           
        self.visit(MethodDecl(None, Id(ast.name), FuncDecl("<init>",[],VoidType(),Block([]))), o)

        for item in ast.methods: 
            self.visit(item, o)

        self.emit.printout(self.emit.emitEPILOG())


    def visitInterfaceType(self, ast, o):
        # name: str
        # methods:List[Prototype]

        self.emit.printout(self.emit.emitPROLOGINTERFACE(ast.name, "java.lang.Object"))
        for item in ast.methods:
            self.emit.printout(self.visit(item,o))
            self.emit.printout(self.emit.emitENDMETHOD())
        self.emit.printout(self.emit.emitEPILOG())

    def visitBlock(self, ast, o):
        #member:List[BlockMember]

        env = o.copy()
        env['env'] = [[]] + env['env']


        env['frame'].enterScope(False)

        self.emit.printout(self.emit.emitLABEL(env['frame'].getStartLabel(), env['frame']))

        for stmt in ast.member:
            if type(stmt) is FuncCall or type(stmt) is MethCall:
                env['stmt'] = True
            self.visit(stmt,env)

        self.emit.printout(self.emit.emitLABEL(env['frame'].getEndLabel(), env['frame']))
        env['frame'].exitScope()
        return o

    def visitAssign(self, ast, o):
        # lhs: LHS
        # rhs: Expr 
        if type(ast.lhs) is Id and not next(filter(lambda x: x.name == ast.lhs.name, [sym for env in o['env'] for sym in env]), None) :
            return self.visit(VarDecl(ast.lhs.name,None,ast.rhs),o)

        if type(ast.lhs) is FieldAccess:
            # receiver:Expr
            # field:str
            fieldAccess = ast.lhs
            if type(fieldAccess.receiver) is Id and fieldAccess.receiver.name == "this":
                self.emit.printout(self.emit.emitREADVAR("this", Id(self.currStruct.name),0,o['frame']))
                field = self.lookup(fieldAccess.field,self.currStruct.elements,lambda x: x[0])
                rhsCode, rhsType = self.visit(ast.rhs, o) 
                self.emit.printout(rhsCode)
                self.emit.printout(self.emit.emitPUTFIELD(f"{self.currStruct.name}/{field[0]}",field[1],o['frame']))
                return o
            elif type(fieldAccess.receiver) is Id:
                code,typ = self.visit(fieldAccess.receiver,o)
                structFound = self.lookup(typ.name, self.structface_list, lambda x:x.name)
                field = self.lookup(fieldAccess.field,structFound.elements,lambda x: x[0])
                rhsCode, rhsType = self.visit(ast.rhs, o)
                o['isLeft'] = False
                self.emit.printout(code + rhsCode)
                self.emit.printout(self.emit.emitPUTFIELD(f"{structFound.name}/{field[0]}",field[1],o['frame']))
                return o

        elif type(ast.lhs) is ArrayCell:
            pass

        rhsCode, rhsType = self.visit(ast.rhs, o)
        o['isLeft'] = True
        lhsCode, lhsType = self.visit(ast.lhs, o) 
        o['isLeft'] = False

        if type(lhsType) is FloatType and type(rhsType) is IntType:
            rhsCode += self.emit.emitI2F(o['frame'])

        o['frame'].push()


        if type(ast.lhs) is ArrayCell:
            o['frame'].push()
            o['frame'].push()
            self.emit.printout(lhsCode)
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitASTORE(lhsType,o['frame']))
            o['frame'].pop()
            o['frame'].pop()
        else:
            self.emit.printout(rhsCode)
            self.emit.printout(lhsCode)

        return o

    
    def visitIf(self, ast, o):
        #  expr:Expr
        # thenStmt:Stmt
        # elseStmt:Stmt # None if there is no else
        code,typ = self.visit(ast.expr,o)
        self.emit.printout(code)

        Label0 = o['frame'].getNewLabel()
        Label1 = o['frame'].getNewLabel() if ast.elseStmt else None
 
        self.emit.printout(self.emit.emitIFFALSE(Label0,o['frame']))
        self.visit(ast.thenStmt,o)

        if ast.elseStmt:    
            self.emit.printout(self.emit.emitGOTO(Label1,o['frame']))

        self.emit.printout(self.emit.emitLABEL(Label0,o['frame']))

        if ast.elseStmt:
            self.visit(ast.elseStmt,o)

        self.emit.printout(self.emit.emitLABEL(Label1,o['frame']))
        return o



    def visitForBasic(self, ast, o):
        # cond:Expr
        # loop:Block
        o['frame'].enterLoop()
        NewLabel = o['frame'].getNewLabel()
        ConLabel = o['frame'].getContinueLabel()
        BreakLabel = o['frame'].getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(ConLabel,o['frame']))
        self.emit.printout(self.visit(ast.cond,o)[0])
        self.emit.printout(self.emit.emitIFFALSE(NewLabel,o['frame']))

        self.visit(ast.loop,o)

        self.emit.printout(self.emit.emitGOTO(ConLabel,o['frame']))
        self.emit.printout(self.emit.emitLABEL(NewLabel,o['frame']))
        self.emit.printout(self.emit.emitLABEL(BreakLabel,o['frame']))
        o['frame'].exitLoop()
        return o

    def visitForStep(self, ast, o):
        # init:Stmt
        # cond:Expr
        # upda:Assign
        # loop:Block
        env = o.copy()
        env['env'] = [[]] + env['env']

        env['frame'].enterLoop()
        ContinueLabel = env['frame'].getContinueLabel()
        BreakLabel = env['frame'].getBreakLabel()
        NewLabel = env['frame'].getNewLabel()

        self.visit(ast.init,env)

        self.emit.printout(self.emit.emitLABEL(NewLabel,env['frame']))
        self.emit.printout(self.visit(ast.cond,env)[0])
        self.emit.printout(self.emit.emitIFFALSE(BreakLabel,env['frame']))

        self.visit(ast.loop,env)

        self.emit.printout(self.emit.emitLABEL(ContinueLabel,env['frame']))
        self.visit(ast.upda,env)
        self.emit.printout(self.emit.emitGOTO(NewLabel, env['frame']))

        self.emit.printout(self.emit.emitLABEL(BreakLabel,env['frame']))

        env['frame'].exitLoop()
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
        self.emit.printout(self.emit.emitRETURN(VoidType(),o['frame']))    
        return o

    def visitId(self, ast, o):
        #name : str

        environment = [j for i in o['env'] for j in i]
        sym = self.lookup(ast.name, environment, lambda x: x.name)

        if sym is None:
            if o.get('isLeft'):
                return self.emit.emitWRITEVAR("this",Id(ast.name), 0, o['frame']),Id("this")
            return self.emit.emitREADVAR("this",Id(ast.name), 0, o['frame']),Id("this")

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
        


    def visitArrayCell(self, ast, o) :
        #   arr:Expr
        #   idx:List[Expr]

        newO = o.copy()
        newO['isLeft'] = False
        codeGen, arrType = self.visit(ast.arr, newO) 

        

        for idx, item in enumerate(ast.idx):
            codeGen += self.visit(item, newO)[0]
            if idx != len(ast.idx) - 1:
                codeGen += self.emit.emitALOAD(arrType, o['frame'])

        retType = None
        if len(arrType.dimens) == len(ast.idx):
            retType = arrType.eleType
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(arrType.eleType, o['frame']) 
        else:
            retType = ArrayType(arrType.dimens[1:: ], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame']) 

        return codeGen, retType

    def visitFieldAccess(self, ast, o):
        # receiver:Expr
        # field:str
    

        code, typ = self.visit(ast.receiver, o)
    
        if typ.name == "this":
            found1 = next(filter(lambda x: x.name == self.currStruct.name, self.structface_list),None)
            found2 = next(filter(lambda x: x[0] == ast.field, found1.elements),None)
            if o.get('isLeft'):
                return code + self.emit.emitPUTFIELD(f"{found1.name}/{ast.field}", found2[1],o['frame']), found2[1]
            else:
                return code + self.emit.emitGETFIELD(f"{found1.name}/{found2[0]}", found2[1],o['frame']), found2[1] 

        if typ.name != "this":
            found1 = next(filter(lambda x: x.name == typ.name, self.structface_list),None)
            found2 = next(filter(lambda x: x[0] == ast.field, found1.elements),None)
            if o.get('isLeft'):
                return code + self.emit.emitPUTFIELD(f"{found1.name}/{ast.field}", found2[1],o['frame']), found2[1]
            else:
                return code + self.emit.emitGETFIELD(f"{found1.name}/{found2[0]}", found2[1],o['frame']), found2[1]

    def visitBinaryOp(self, ast, o):
        # op:str
        # left:Expr
        # right:Expr
       
        op = ast.op
        frame = o['frame']
        codeL, Ltyp = self.visit(ast.left, o)
        codeR, Rtyp = self.visit(ast.right, o)

        if op in ['+', '-'] and isinstance(Ltyp,(IntType,FloatType)):
            returnTyp = IntType() if type(Ltyp) is IntType and type(Rtyp) is IntType else FloatType()
            if type(returnTyp) is FloatType:
                if type(Ltyp) is IntType:
                    codeL += self.emit.emitI2F(frame)
                elif type(Rtyp) is IntType:
                    codeR += self.emit.emitI2F(frame)
            return codeL + codeR + self.emit.emitADDOP(op,returnTyp,frame),returnTyp 
        if op in ['*', '/']:
            returnTyp = IntType() if type(Ltyp) is IntType and type(Rtyp) is IntType else FloatType()
            if type(returnTyp) is FloatType:
                if type(Ltyp) is IntType:
                    codeL += self.emit.emitI2F(frame)
                elif type(Rtyp) is IntType:
                    codeR += self.emit.emitI2F(frame)
            return codeL + codeR + self.emit.emitMULOP(op,returnTyp,frame),returnTyp 
        if op == "%":
            return codeL + codeR +  self.emit.emitMOD(frame), Ltyp
        if op in ['==', '!=', '<', '>', '>=', '<='] and isinstance(Ltyp,(IntType,FloatType)):
            return codeL + codeR +  self.emit.emitREOP(op,Ltyp, frame),BoolType()
        if op == "||":
            return codeL + codeR +   self.emit.emitOROP(frame),BoolType()
        if op == "&&":
            return codeL + codeR + self.emit.emitANDOP(frame), BoolType() 

        # nối string string        
        if op in ['+', '-'] and type(Ltyp) is StringType:
            return codeL + codeR + self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", MType([StringType()],StringType()),frame)  , StringType()  
        if op in ['==', '!=', '<', '>', '>=', '<='] and type(Ltyp) is StringType:
            code = codeL + codeR + self.emit.emitREOP(op, Ltyp, frame)
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

        sym = next(filter(lambda x: x.name == ast.funName, self.list_function),None)
        env = o.copy()
        if o.get('stmt'):
            o["stmt"] = False
            code = "".join([str(self.visit(x,o)[0]) for x in ast.args])
            self.emit.printout(code)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            return o 
        
        code = "".join([str(self.visit(x, o)[0]) for x in ast.args])
        code += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])

        return code, sym.mtype.rettype

    def visitMethCall(self, ast, o):
        # receiver: Expr
        # metName: str
        # args:List[Expr]

        code, typ = self.visit(ast.receiver, o)
        if isinstance(typ, Id):
            typ = self.lookup(typ.name,self.structface_list,lambda x:x.name)

        is_stmt = o.get('stmt')

        for arg in ast.args:
            code += self.visit(arg, o)[0]

        returnType = None
        if isinstance(typ, StructType):
            method = next(filter(lambda x: x.fun.name == ast.metName, typ.methods), None)
            mtype = MType(list([item.parType for item in method.fun.params]), method.fun.retType)
            returnType = method.fun.retType
            code += self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, o['frame'])
            
        elif isinstance(typ, InterfaceType):
            method = next(filter(lambda x: x.name == ast.metName, typ.methods), None)
            
            mtype = MType(list([item for item in method.params]), method.retType)
            returnType = method.retType
            code += self.emit.emitINVOKEINTERFACE(f"{typ.name}/{ast.metName}", mtype, o['frame'])

        if is_stmt:
            self.emit.printout(code)
            return o
        
        return code, returnType

    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(ast.value,o['frame']),IntType()

    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value),o['frame']),FloatType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value,StringType(),o['frame']),StringType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value), o['frame']), BoolType()
    
    def visitArrayLiteral(self, ast, o):
        # dimens:List[Expr]
        # eleType: Type
        # value: NestedList
        def getdimensions(dat):
            if not isinstance(dat[0], list):
                return [IntLiteral(len(dat))]

            return [IntLiteral(len(dat))] + getdimensions(dat[0])
        
        def nested2recursive(dat, o) :
            if not isinstance(dat,list): 
                return self.visit(dat, o)
            
            frame = o['frame']
            if not isinstance(dat[0],list):
                codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)
                _ , type_element_array = self.visit(dat[0], o)
                codeGen += self.emit.emitNEWARRAY(type_element_array,o['frame'])
                
                for idx, item in enumerate(dat):
                    codeGen += self.emit.emitDUP(o['frame'])
                    codeGen += self.emit.emitPUSHICONST(idx,o['frame'])
                    codeGen += self.visit(item, o)[0] 
                    codeGen += self.emit.emitASTORE(type_element_array, o['frame'])
                return codeGen, ArrayType([IntLiteral(len(dat))],ast.eleType)
            
            codeGen = self.emit.emitPUSHCONST(len(dat), IntType(), frame)
            _, type_element_array = nested2recursive(dat[0], o)
            codeGen += self.emit.emitANEWARRAY(type_element_array,o['frame'])
            for idx, item in enumerate(dat):
                codeGen += self.emit.emitDUP(o['frame'])
                codeGen += self.emit.emitPUSHICONST(idx,o['frame'])
                codeGen += nested2recursive(item, o)[0]
                codeGen += self.emit.emitASTORE(type_element_array, o['frame'])
            return  codeGen, ArrayType(getdimensions(dat),ast.eleType)
        
        return nested2recursive(ast.value, o) 

 

    def visitStructLiteral(self, ast, o):
        #name:str
        #elements: List[Tuple[str,Expr]]
        code = self.emit.emitNEW(ast.name, o['frame'])
        code += self.emit.emitDUP(o['frame'])
        param_type_list = []
        for item in ast.elements:
            code1, typ = self.visit(item[1], o)
            code += code1
            param_type_list += [typ]

        code += self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>", MType(param_type_list, VoidType()))
        return code, Id(ast.name)

    def visitNilLiteral(self, ast, o):
        code = self.emit.emitPUSHNULL(o['frame'])
        return code, Id("")

    def calculateIntLiteral(self, ast, o):

        def visitBinaryOp(self,ast,o): 
        # op:str
        # left:Expr
        # right:Expr
            leftType = self.calculateIntLiteral(ast.left,o)
            rightType = self.calculateIntLiteral(ast.right,o)
            op = ast.op
            if op == "+":
                    return IntLiteral(leftType.value + rightType.value)
            elif op in ["-","*","/"]:
                if (isinstance(leftType,IntLiteral) and isinstance(rightType,IntLiteral)):
                    if op == "-":
                        return IntLiteral(leftType.value - rightType.value)
                    if op =="*":
                        return IntLiteral(int(leftType.value * rightType.value))
                    if op == "/":
                        return IntLiteral(int(leftType.value / rightType.value))
            elif op =="%":
                return IntLiteral(int(leftType.value % rightType.value))           
        def visitUnaryOp(self,ast,o): 
            op = ast.op
            bodyType = self.calculateIntLiteral(ast.body,c)
            return IntLiteral(- bodyType.value)
        def visitId(self,ast,o):
            #name : str
            sym = next(filter(lambda x: x.name == ast.name, [j for i in o['env'] for j in i]),None)      
            return IntLiteral(sym.initValue.value)

        if type(ast) is IntLiteral:
            return ast
        elif type(ast) is BinaryOp:
            return visitBinaryOp(self,ast,o)
        elif type(ast) is UnaryOp:
            return visitUnaryOp(self,ast,o)
        elif type(ast) is Id:
            return visitId(self,ast,o)
        else :
            return IntLiteral(0)

    def compare2Type(self, LSH_type, RHS_type, list_type_permission) :
        if type(RHS_type) is StructType and RHS_type.name == "":
            return True

        LSH_type = self.lookup(LSH_type.name, self.structface_list, lambda x: x.name  ) if isinstance(LSH_type, Id) else LSH_type
        RHS_type = self.lookup(RHS_type.name, self.structface_list, lambda x: x.name  ) if isinstance(RHS_type, Id) else RHS_type

        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                return all(
                    any(
                        struct_methods.fun.name == inteface_method.name and
                        self.compare2Type(struct_methods.fun.retType, inteface_method.retType,list_type_permission) and
                        len(struct_methods.fun.params) == len(inteface_method.params) and
                        reduce(
                            lambda x, i: x and self.compare2Type(struct_methods.fun.params[i].parType, inteface_method.params[i]),
                            range(len(struct_methods.fun.params)),
                            True
                        )
                        for struct_methods in RHS_type.methods
                    )
                    for inteface_method in LSH_type.methods
                )
            # Kiểm tra tương thích giữa hai InterfaceType hoặc hai StructType.
            if isinstance(LSH_type, (StructType,InterfaceType)) and isinstance(RHS_type, (StructType,InterfaceType)):
                return LSH_type.name == RHS_type.name 

        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            return (len(LHS.dimens) == len(RHS.dimens)
                    and all(
                        l.value == r.value  for l, r in zip(LSH_type.dimens, RHS_type.dimens)
                    )
                    and self.compare2Type(LHS_type.eleType, RHS_type.eleType, [list_type_permission[0]] if len(list_type_permission) != 0 else []))

        if type(LSH_type) == type(RHS_type):
            return True
        
        if isinstance(LSH_type, FloatType) and isinstance(RHS_type, IntType):
            return True

        return False