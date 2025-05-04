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
        self.function = None
        self.list_function = []
        self.arrayCell = None
        self.arrayCellType = None
        self.list_type = {}
        self.struct = None

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
        self.visit(Block([Assign(Id(item.varName), item.varInit) for item in ast.decl if isinstance(item, VarDecl) and item.varInit]  +
                         [Assign(Id(item.conName), item.iniExpr) for item in ast.decl if isinstance(item, ConstDecl) and item.iniExpr]),env)
        
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

        env = reduce(lambda a, x: self.visit(x, a) if isinstance(x, FuncDecl) else a, ast.decl, env)

        self.emitObjectInit()
        self.emitObjectCInit(ast,env)

        self.emit.printout(self.emit.emitEPILOG())

        for item in self.list_type.values():
            self.struct = item
            self.emit = Emitter(self.path + "/" + item.name + ".j")
            self.visit(item, {
                'env': env['env']
            })
        return env
    
    def visitParamDecl(self,ast, o):
        # parName: str
        # parType: Type
        frame = o['frame']
        index = frame.getNewIndex()
        o['env'][0].append(Symbol(ast.parName, ast.parType, Index(index),IntLiteral(0) if type(ast.parType) is IntType else None))
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
                return BooleanLiteral(False)
            elif type(varType) is ArrayType:
                dimensions = varType.dimens
                
                # Base case: if no dimensions left, initialize the element type
                if not dimensions:
                    return create_init(varType.eleType, o)
                    
                # Extract dimension sizes (assuming dimensions are IntLiteral)
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
                        # Innermost dimension: create elements of eleType
                        return [create_init(eleType, o) for _ in range(dims[0])]
                    else:
                        # Recursively build sub-arrays for higher dimensions
                        return [build_array(dims[1:], eleType) for _ in range(dims[0])]
                        
                # Generate the nested array structure
                elements = build_array(dim_sizes, varType.eleType)
                
                return ArrayLiteral(dimensions, varType.eleType, elements)

                
        varInit = ast.varInit 
        varType = ast.varType 

        if not varInit:
            varInit = create_init(varType, o)
            ast.varInit = varInit
        
        env = o.copy()
        env['frame'] = Frame("<Mytemplate>", VoidType()) 

        rhsCode, rhsType = self.visit(varInit, env)
        if not varType:
            varType = rhsType

        if 'frame' not in o: # TH global var 
            o['env'][0].append(Symbol(ast.varName, varType,CName(self.className), self.calculateIntLiteral(ast.varInit,o) if type(varType) is IntType else ast.varInit))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.varName, varType, True, False, None))
        else:
            frame = o['frame']

            index = frame.getNewIndex()
            o['env'][0].append(Symbol(ast.varName, varType,Index(index), self.calculateIntLiteral(ast.varInit,o) if type(varType) is IntType else ast.varInit )) 



            self.emit.printout(self.emit.emitVAR(index, ast.varName, varType, frame.getStartLabel(), frame.getEndLabel(), frame))  
            rhsCode, rhsType = self.visit(varInit, o)
            if type(varType) is FloatType and type(rhsType) is IntType:
                rhsCode += self.emit.emitI2F(frame) 
                  
            self.emit.printout(rhsCode)
            self.emit.printout(self.emit.emitWRITEVAR(ast.varName, varType, index, frame))                   
        return o

    
    def visitConstDecl(self, ast, o) :
        return self.visit(VarDecl(ast.conName, ast.conType, ast.iniExpr), o)


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
        
        self.function = ast.fun
        frame = Frame(ast.fun.name, ast.fun.retType)
        mtype = MType(list(map(lambda x: x.parType, ast.fun.params)), ast.fun.retType)
        
        env = o.copy()
        env['frame'] = frame
        self.emit.printout(self.emit.emitMETHOD(ast.fun.name, mtype,False, frame))
        frame.enterScope(True) 

        self.emit.printout(self.emit.emitVAR("this",Id("this"),env['frame'].getStartLabel(),env['frame'].getEndLable(),env['frame'])) 
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if ast.receiver is None:
            self.emit.printout(self.emit.emitREADVAR("this", Id("java.lang.Object.super"), 0, frame))  
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))  

        env['env'] = [[]] + env['env']
        # env = reduce(lambda acc,e: self.visit(e,acc),ast.params,env)
        env = reduce(lambda acc,e: self.visit(e,acc),ast.fun.params,env)  

        self.visit(ast.fun.body, env) #duyệt block thân hàm


        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(ast.fun.retType) is VoidType:
            self.emit.printout(self.visit(Return(None),env)) 
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
        return o
    
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
        #dimens:List[Expr]
        #eleType:Type
        codeGen = ""
        for item in ast.dimens:
            codeGen += self.visit(item, o)[0]
        codeGen += self.emit.emitMULTIANEWARRAY(ast, o['frame'])
        return codeGen, ast

    
    def visitStructType(self, ast: StructType, o):
        # name: str
        # elements:List[Tuple[str,Type]]
        # methods:List[MethodDecl]
        self.emit.printout(self.emit.emitPROLOG(f"{ast.name}", "java.lang.Object"))
        for item in self.list_type.values(): # Lặp qua các type đc khai báo(interface/struct)
            if item.name == ast.name and self.checkType(item, ast, [(InterfaceType, StructType)]): 
                self.emit.printout("TODO") # Sinh ra đoạn .implement ___ như ở ví dụ bên trên.
        for item in ast.elements:
            self.emit.printout(self.emit.emitATTRIBUTE(item[0],item[1], False, False, None))

        self.visit(MethodDecl(None, None, FuncDecl("<init>", [ParamDecl(item[0],item[1]) for item in ast.elements], VoidType(),
                                                   
                            Block([VarDecl(item[0],item[1],None) for item in ast.elements]))), o)   
           
        self.visit(MethodDecl(None, None, FuncDecl("<init>",[],VoidType()), o))
        for item in ast.methods: self.visit(item, o)
        self.emit.printout(self.emit.emit) # kết thúc khai báo của struct

    def visitInterfaceType(self, ast, o):
        # name: str
        # methods:List[Prototype]
        self.emit.printout(self.emit.emitPROLOG(ast.name, "java.lang.Object", True))
        for item in ast.methods:
            self.emit.emitprintout(self.visit(item,o)[0])
            self.emit.emitprintout(self.emit.emitENDMETHOD(o['frame']))
        self.emit.printout(self.emit.emitEPILOG())

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
                self.arrayCell =  ast 
        else:
            retType = ArrayType(arrType.dimens[1:: ], arrType.eleType)
            if not o.get('isLeft'):
                codeGen += self.emit.emitALOAD(retType, o['frame']) 
            else:
                self.arrayCell = ast

        return codeGen, retType

    def visitFieldAccess(self, ast, o):
        # receiver:Expr
        # field:str

        code, typ = self.visit(ast.receiver, o)

        found = next(filter(lambda x: x.name == typ.name, self.list_type),None)
        found1 = next(filter(lambda x: x[0] == ast.field, found.elements),None)
        return code + self.emit.emitGETFIELD(f"java.lang.Object.{found.name}{found1[0]}", found1[1],o['frame']), found1[1] 


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
            return codeLeft + codeRight +   self.emit.emitOROP(frame),BoolType()
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
        env = o.copy()
        if o.get('stmt'):
            o["stmt"] = False
            output = "".join([str(self.visit(x,o)[0]) for x in ast.args])
            self.emit.printout(output)
            self.emit.printout(self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame']))
            return o 
        
        output = "".join([str(self.visit(x, o)[0]) for x in ast.args])
        output += self.emit.emitINVOKESTATIC(f"{sym.value.value}/{ast.funName}",sym.mtype, o['frame'])

        return output, sym.mtype.rettype

    def visitMethCall(self, ast, o):
        # receiver: Expr
        # metName: str
        # args:List[Expr]

        code, typ = self.visit(ast.receiver, o)
        if isinstance(typ, Id):
            typ = self.list_type.get(typ.name)

        # 3. Kiểm tra xem lời gọi phương thức này có phải là một statement hay một expression
        is_stmt = o.pop("stmt", False)

        # 4. Tạo mã cho các đối số của phương thức.
        for arg in ast.args:
            code += self.visit(arg, o)[0]

        returnType = None
        if isinstance(typ, StructType):
            method = next(filter(lambda x: x.name == ast.metName, typ.methods), None)
            mtype = MType(list([item.parType for item in method.fun.params]), method.fun.retType)
            returnType = method.fun.retType
            self.emit.printout(self.emit.emitINVOKEVIRTUAL(f"{typ.name}/{ast.metName}", mtype, o['frame']))
            code += self.emit.emitINVOKEVIRTUAL("TODO", mtype, o['frame'])
            
        elif isinstance(typ, InterfaceType):
            method = next(filter(lambda x: x.name == ast.metName, typ.methods), None)
            
            mtype = MType(list([item for item in method.params]), method.retType)
            returnType = method.retType
            code += self.emit.emitINVOKEINTERFACE(f"TODO", mtype, o['frame'])
        
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
        list_type = []
        for item in ast.elements:
            # Xử lý từng thành phần (field và giá trị) của struct literal.
            # Gợi ý:
            # 1. Gọi self.visit(item[1], o) để lấy mã và kiểu của giá trị khởi tạo (item[1]).
            # 2. Thêm mã này vào 'code'.
            # 3. Thêm kiểu của giá trị khởi tạo vào 'list_type'.
            c, t = self.visit(item[1], o)
            code += c
            list_type += [t]

        # Gọi constructor của struct.
        # Gợi ý:
        # 1. Tạo MType cho constructor dựa trên 'list_type' (kiểu của các tham số).
        # 2. Sử dụng self.emit.emitINVOKESPECIAL để gọi constructor của struct (ast.name/<init>).
        code += self.emit.emitINVOKESPECIAL(o['frame'], f"{ast.name}/<init>", MType(list_type, VoidType()) if len(ast.elements) else MType([], VoidType()))
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

    def checkType(self, LSH_type, RHS_type, list_type_permission) :
        if type(RHS_type) == StructType and RHS_type.name == "":
            return True

        LSH_type = self.lookup(LSH_type.name, self.list_type.values(), lambda x: x.name  ) if isinstance(LSH_type, Id) else LSH_type
        RHS_type = self.lookup(RHS_type.name, self.list_type.values(), lambda x: x.name  ) if isinstance(RHS_type, Id) else RHS_type

        if (type(LSH_type), type(RHS_type)) in list_type_permission:
            if isinstance(LSH_type, InterfaceType) and isinstance(RHS_type, StructType):
                return all(
                    any(
                        # So sánh tên, kiểu trả về và kiểu tham số của phương thức.
                        struct_methods.fun.name == inteface_method.name and
                        self.checkType(struct_methods.fun.retType, inteface_method.retType) and
                        len(struct_methods.fun.params) == len(inteface_method.params) and
                        reduce(
                            lambda x, i: x and self.checkType(struct_methods.fun.params[i].parType, inteface_method.params[i]),
                            range(len(struct_methods.fun.params)),
                            True
                        )
                        for struct_methods in RHS_type.methods
                    )
                    for inteface_method in LSH_type.methods
                )
            # Kiểm tra tương thích giữa hai InterfaceType hoặc hai StructType.
            if isinstance(LSH_type, (StructType,InterfaceType)) and isinstance(RHS_type, (StructType,InterfaceType)):
                return LHS_type.name == RHS_type.name 

        if isinstance(LSH_type, ArrayType) and isinstance(RHS_type, ArrayType):
            return (len(LHS.dimens) == len(RHS.dimens)
                    and all(
                        l.value == r.value  for l, r in zip(LSH_type.dimens, RHS_type.dimens)
                    )
                    and self.checkType("TODO", "TODO", [list_type_permission[0]] if len(list_type_permission) != 0 else []))

        if type(LSH_type) == type(RHS_type):
            return True
        
        if isinstance(LSH_type, FloatType) and isinstance(RHS_type, IntType):
            return True

        return False