"""
 * @author nhphung
"""

#2252650

from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
from typing import Tuple

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return "MType([" + ",".join(str(x) for x in self.partype) + "]," + str(self.rettype) + ")"

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + str(self.name) + "," + str(self.mtype) + ("" if self.value is None else "," + str(self.value)) + ")"

class StaticChecker(BaseVisitor,Utils):           
    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [Symbol("getInt",MType([],IntType()),"func"),
                            Symbol("putIntLn",MType([IntType()],VoidType()),"func"),
                            Symbol("putInt",MType([IntType()],VoidType()),"func"),
                            Symbol("getFloat",MType([],FloatType()),"func"),
                            Symbol("putFloat",MType([FloatType()],VoidType()),"func"),
                            Symbol("putFloatLn",MType([FloatType()],VoidType()),"func"),
                            Symbol("getBool",MType([],BoolType()),"func"),
                            Symbol("putBool",MType([BoolType()],VoidType()),"func"),
                            Symbol("putBoolLn",MType([BoolType()],VoidType()),"func"),
                            Symbol("getString",MType([],StringType()),"func"),
                            Symbol("putString",MType([StringType()],VoidType()),"func"),
                            Symbol("putStringLn",MType([StringType()],VoidType()),"func"),
                            Symbol("putLn",MType([],VoidType()),"func"),
                        ]
        
        self.global_envi1 = [Symbol("getInt",MType([],IntType()),"func"),
                            Symbol("putIntLn",MType([IntType()],VoidType()),"func"),
                            Symbol("putInt",MType([IntType()],VoidType()),"func"),
                            Symbol("getFloat",MType([],FloatType()),"func"),
                            Symbol("putFloat",MType([FloatType()],VoidType()),"func"),
                            Symbol("putFloatLn",MType([FloatType()],VoidType()),"func"),
                            Symbol("getBool",MType([],BoolType()),"func"),
                            Symbol("putBool",MType([BoolType()],VoidType()),"func"),
                            Symbol("putBoolLn",MType([BoolType()],VoidType()),"func"),
                            Symbol("getString",MType([],StringType()),"func"),
                            Symbol("putString",MType([StringType()],VoidType()),"func"),
                            Symbol("putStringLn",MType([StringType()],VoidType()),"func"),
                            Symbol("putLn",MType([],VoidType()),"func"),
                        ]
        
        self.structList = []
        self.interfaceList = []

        self.funcSymbol = []
        self.methodSymbol = []

        self.currentSymbol = []


    def check(self):
        return self.visit(self.ast,self.global_envi)

    def Compare2Function(self, Func1, Func2): 
    #     FuncDecl(Decl):
    # name: str
    # params: List[ParamDecl]
    # retType: Type # VoidType if there is no return type

        result = Func1.name == Func2.name
        if len(Func1.params) != len(Func2.params):
            return False
        
        result = reduce(lambda x,y: x and y,[type(Func1.params[i].parType) is type(Func2.params[i].parType)  for i in range (0,len(Func1.params))],result)
        result = result and type(Func1.retType) is type(Func2.retType)
        return result

    def Compare2FuncCall(self, Func1, Func2,c): # Symbol
        result = Func1.name == Func2.name
        if len(Func1.mtype.partype) != len(Func2.mtype.partype):
            return False
        
        result = reduce(lambda x,y: x and y,[self.Compare2TypeFuncCall(Func1.mtype.partype[i],Func2.mtype.partype[i],c) for i in range (0,len(Func1.mtype.partype))],result)
        result = result and type(Func1.mtype.rettype) is type(Func2.mtype.rettype)
        return result    

    def Compare2ArrayType(self,Type1, Type2,c ): 
            
        eleType1 = Type1.eleType
        if type(Type1.eleType) is Id:
            eleType1 = self.visit(Type1.eleType,c)

        eleType2 = Type2.eleType
        if type(Type2.eleType) is Id:
            eleType2 = self.visit(Type2.eleType,c)

    
        if type(eleType1) is FloatType and isinstance(eleType2,(IntType,IntLiteral)): 
            pass
        elif not self.Compare2TypeFuncCall(eleType1,eleType2 ,c) :
            return None   

        Typeright = len(Type1.dimens) == len(Type2.dimens)
        if not Typeright:
            return None
       
        for i in range(0,len(Type1.dimens)):
            Type1.dimens[i] = self.visit(Type1.dimens[i],c)
            Type2.dimens[i] = self.visit(Type2.dimens[i],c)

            if not type(Type1.dimens[i] ) is IntLiteral or not type(Type1.dimens[i] ) is IntLiteral:
                return None
            if Type1.dimens[i].value != Type2.dimens[i].value :
                return None
        
        if len(Type1.dimens) == len(Type2.dimens):
            return Type2
        #Typeright = reduce(lambda a,e: a and e,[Type1.dimens[i].value == Type2.dimens[i].value for i in range (0,len(Type1.dimens))],Typeright)
        return True

    def CompareInterfaceVsStruct(self, In, St):
        prototypeList = In.methods
        # name: str
        # params:List[Type]
        # retType: Type # VoidType if there is no return type

        methodsList = St.methods
        # receiver: str
        # recType: Type 
        # fun: FuncDecl

        SameFlag = False

        for prototype in prototypeList:
            for method in methodsList:
                if self.CompareMethodvsPrototype(method,prototype):
                    SameFlag = True
                    break

                SameFlag = False
        return SameFlag

    def CompareMethodvsPrototype(self, method, prototype):
        # receiver: str
        # recType: Type 
        # fun: FuncDecl

        # name: str
        # params:List[Type]
        # retType: Type # VoidType if there is no return type
        SameFlag = method.fun.name == prototype.name

        if type(method.fun.retType) is StructType and type(prototype.retType) is StructType:
            SameFlag = SameFlag and method.fun.retType.name == prototype.retType.name
        else :
            SameFlag = SameFlag and type(method.fun.retType) is type(prototype.retType)

        methodParamList = []
        for para in method.fun.params:
            methodParamList +=  [para.parType]
        prototypeParamList = prototype.params

        if len(methodParamList) != len(prototypeParamList):
            return False 
        
        else:
            for i in range (0, len(methodParamList)):
                if type(methodParamList[i]) is StructType and type(prototypeParamList[i]) is StructType:
                    SameFlag = SameFlag and methodParamList[i].name == prototypeParamList[i].name
                else:
                    SameFlag = SameFlag and type(methodParamList[i]) is type(prototypeParamList[i])

        return SameFlag

    def Compare2Type(self,Typ1,Typ2,c):
        SameFlag = False
        if type(Typ1) is ArrayType and type(Typ2) is ArrayType:
            return self.Compare2ArrayType(Typ1,Typ2,c)
        elif type(Typ1) is StructType and type(Typ2) is StructType:
            return True
        elif type(Typ1) is FloatType and isinstance(Typ2, (IntType,FloatType,IntLiteral)):
            return True
        elif isinstance(Typ1, (IntType,IntLiteral)) and isinstance(Typ2, (IntType,IntLiteral)) :
            return True
        elif type(Typ2) is str and Typ2 == "nil":
            return True
        elif type(Typ1) is type(Typ2):
            return True
        elif isinstance(Typ1,(StructType, InterfaceType)) and type(Typ2) is VoidType:
            return True
        
        return False

    def Compare2TypeFuncCall(self,Typ1,Typ2,c):
        SameFlag = False
        if type(Typ1) is ArrayType and type(Typ2) is ArrayType:
            return self.Compare2ArrayTypeFuncCall(Typ1,Typ2,c)
        elif type(Typ1) is StructType and type(Typ2) is StructType:
            return Typ1.name == Typ2.name
        elif type(Typ1) is InterfaceType and type(Typ2) is InterfaceType:
            return Typ1.name == Typ2.name
        elif isinstance(Typ1, (IntType,IntLiteral)) and isinstance(Typ2, (IntType,IntLiteral)) :
            return True
        elif type(Typ2) is str and Typ2 == "nil":
            return True
        elif type(Typ1) is type(Typ2):
            return True
        
        return False

    def Compare2ArrayTypeFuncCall(self,Type1,Type2,c):
        eleType1 = Type1.eleType
        if type(Type1.eleType) is Id:
            eleType1 = self.visit(Type1.eleType,c)

        eleType2 = Type2.eleType
        if type(Type2.eleType) is Id:
            eleType2 = self.visit(Type2.eleType,c)


        if not self.Compare2TypeFuncCall(eleType1,eleType2 ,c): 
             return None   
        Typeright = len(Type1.dimens) == len(Type2.dimens)
        if not Typeright:
            return None
        
        for i in range(0,len(Type1.dimens)):
            Type1.dimens[i] = self.visit(Type1.dimens[i],c)
            Type2.dimens[i] = self.visit(Type2.dimens[i],c)

            if not type(Type1.dimens[i] ) is IntLiteral or not type(Type1.dimens[i] ) is IntLiteral:
                return None
            if Type1.dimens[i].value != Type2.dimens[i].value :
                return None

        
        if len(Type1.dimens) == len(Type2.dimens):
            return Type2
        elif len(Type1.dimens) < len(Type2.dimens):
            eleType = Type1.eleType
            dimens = []

            i = len(Type2.dimens)
            while i <len(Type2.dimens):
                dimens += [Type2.dimens[i]]   
                i +=1

            return ArrayType(dimens,eleType)


    def visitProgram(self,ast, c):
        #decl : List[Decl]

        env = [c]
        c = env
        for x in ast.decl:
            if type(x) is StructType or type(x) is InterfaceType :
                self.visitFirst(x,c)        

        for x in ast.decl:
            if type(x) is MethodDecl or type(x) is FuncDecl:
                self.visitFirst(x,c)

        for x in ast.decl:
            c = self.visit(x,c)

        # for x in ast.decl:
        #     c = self.visit(x,c)

        return c
        #return list(reduce(lambda a,e : self.visit(e,a), ast.decl, c))
        

    def visitParamDecl(self,ast,c): 
        # parName: str
        # parType: Type

        found = self.lookup(ast.parName, c[0], lambda x: x.name)
        if found :
            raise Redeclared(Parameter(),ast.parName)
        
        c[0] += [Symbol( ast.parName, ast.parType,None)]
        return c

    def visitVarDecl(self, ast, c):
        # varName : str
        # varType : Type # None if there is no type
        # varInit : Expr # None if there is no initialization    

        found = self.lookup(ast.varName, c[0], lambda x: x.name)
        if found:
            raise Redeclared(Variable(), ast.varName)   
        ast1 = VarDecl(ast.varName, ast.varType,ast.varInit)
        if type(ast.varType) is Id:
            ast.varType = self.visit(ast.varType,c)

        
        
        if ast.varInit:
            
            initType = self.visit(ast.varInit, c)           
            if type(initType) is Id:
                for envi in c:
                    found = self.lookup(initType.name,envi,lambda x:x.name)
                    if found : 
                        if not type(found.value) is str:
                            break
                        else:
                            found = None
                if not found:
                    raise Undeclared(Identifier(),initType.name)
            if type(initType) is list  :
                raise TypeMismatch(ast.varInit)
            
            if ast.varType is None:
                ast.varType = initType
            elif type(initType) is str and initType =="nil":
                if not type(ast.varType) is StructType and not type(ast.varType) is InterfaceType:
                    raise TypeMismatch(ast1)

            elif type(initType) is StructType:
                if type(ast.varType) is InterfaceType:
                    if not self.CompareInterfaceVsStruct(ast.varType, initType):
                        raise TypeMismatch(ast1) 
                elif not type(ast.varType) is StructType:
                    raise TypeMismatch(ast1)
                else:
                    if ast.varType.name != initType.name:                       
                        raise TypeMismatch(ast1)
            elif type(initType) is InterfaceType:
                if not type(ast.varType) is InterfaceType:
                    raise TypeMismatch(ast1)
                else:
                    if ast.varType.name != initType.name:
                        raise TypeMismatch(ast1)      
            elif not isinstance(ast.varType, ArrayType) and isinstance(initType, ArrayType):    
                if self.Compare2Type(ast.varType, initType.eleType,c):
                    ast.varType = initType
                else:
                    raise TypeMismatch(ast1)  
            elif isinstance(ast.varType, ArrayType) and isinstance(initType, ArrayType):
                Typeright = self.Compare2ArrayType(ast.varType, initType,c)
                if not Typeright:
                    raise TypeMismatch(ast1)
            elif isinstance(ast.varType, FloatType) and isinstance(initType, (IntLiteral,IntType)):
                pass
            elif not self.Compare2Type(ast.varType, initType,c):
                raise TypeMismatch(ast1)
            
        c[0] += [Symbol(ast.varName, ast.varType, ast.varInit)]    
        return c

        
    def visitConstDecl(self,ast,c): 
    # conName : str
    # conType : Type # None if there is no type 
    # iniExpr : Expr
        found = self.lookup(ast.conName, c[0], lambda x: x.name)
        if found:
            raise Redeclared(Constant(), ast.conName)
        
        ast1 = ConstDecl(ast.conName, ast.conType,ast.iniExpr)
        if type(ast.conType) is Id:
            ast.conType = self.visit(ast.conType,c)

        if ast.iniExpr:
            initType = self.visit(ast.iniExpr, c)           
            if type(initType) is Id:
                for envi in c:
                    found = self.lookup(initType.name,envi,lambda x:x.name)
                    if found : 
                        if not type(found.value) is str:
                            break
                        else:
                            found = None
                if not found:
                    raise Undeclared(Identifier(),initType.name)
                           
            if not isinstance(initType,(IntType,IntLiteral,FloatType,StringType,BoolType,StructType,InterfaceType,ArrayType,VoidType)):
                raise TypeMismatch(ast1)
            
            if type(initType) is str and initType == "nil":
                if not type(ast.conType) is StructType and not type(ast.conType) is InterfaceType:
                    raise TypeMismatch(ast1)
            elif ast.conType is None:
                ast.conType = initType
            elif type(initType) is StructType:
                if type(ast.conType) is InterfaceType:
                    if not self.CompareInterfaceVsStruct(ast.conType, initType):
                        raise TypeMismatch(ast1) 
                elif not type(ast.conType) is StructType:
                    raise TypeMismatch(ast1)
                else:
                    if ast.conType.name != initType.name:                       
                        raise TypeMismatch(ast1)
            elif type(initType) is InterfaceType:
                if not type(ast.conType) is InterfaceType:
                    raise TypeMismatch(ast1)
                else:
                    if ast.conType.name != initType.name:
                        raise TypeMismatch(ast1)    
            elif not isinstance(ast.conType, ArrayType) and isinstance(initType, ArrayType):    
                if self.Compare2Type(ast.conType, initType.eleType,c):
                    ast.conType = initType
                else:
                    raise TypeMismatch(ast1)    
            elif isinstance(ast.conType, ArrayType) and isinstance(initType, ArrayType):
                Typeright = self.Compare2ArrayType(ast.conType, initType,c)
                if not Typeright:
                    raise TypeMismatch(ast1)
            elif isinstance(ast.conType, FloatType) and isinstance(initType, (IntLiteral,IntType)):
                pass
            elif not self.Compare2Type(ast.conType, initType,c):
                raise TypeMismatch(ast1)
            
        c[0] += [Symbol(ast.conName, ast.conType, ast.iniExpr)]    
        return c

    def visitFuncDecl(self,ast, c):  
    # name: str
    # params: List[ParamDecl]
    # retType: Type # VoidType if there is no return type
    # body: Block

        found = self.lookup(ast.name, c[0], lambda x: x.name )
        if found:
            raise Redeclared(Function(), ast.name )

        env = [[]]                     
        paramtypeslist = []
        for para in ast.params:
            paramtypeslist += [self.visit(para.parType,c)]
            env = self.visit(para,env)
               
        

        if isinstance(ast.retType,IntType) : 
            ast.retType = IntLiteral(None)

        if type(ast.retType) is Id:
            ast.retType = self.visit(ast.retType,c)

        self.currentSymbol = [Symbol(ast.name, MType(paramtypeslist , ast.retType) ,"func") ] +  self.currentSymbol


        c[0] += [Symbol(ast.name, MType(paramtypeslist ,ast.retType) , "func")]
        env = [[]] + env + c

        env = self.visit(ast.body, env)

        self.currentSymbol = self.currentSymbol[1::]        
        return c


    def visitMethodDecl(self,ast, c):
    # receiver: str
    # recType: Type 
    # fun: FuncDecl
        recStruct = self.lookup(ast.recType.name, self.structList,lambda x:x.name)
        for method in self.methodSymbol:           
            if method.name == ast.fun.name and recStruct.name == method.mtype.name :
                    raise Redeclared(Method(),ast.fun.name)

        recStruct1 = self.lookup(recStruct.name, c[0], lambda x:x.name)
        if recStruct1 and recStruct1.value == "struct":
            for ele in recStruct1.mtype:
                if ast.fun.name  == ele[0]:
                    raise Redeclared(Method(),ast.fun.name)

        self.methodSymbol += [Symbol(ast.fun.name,recStruct,None)]  


        # FuncDecl
        Myfunc = ast.fun
        paramlistype = []
        #env = [[Symbol(ast.receiver, recStruct, None)]]
        env = [[]]
        # env[0]  += [Symbol("struct", recStruct, ast.receiver)]

        for para in Myfunc.params:
            env = self.visit(para,env)
            paramlistype += [para.parType]

        if type(Myfunc.retType) is Id:
            Myfunc.retType = self.visit(Myfunc.retType,c)

        self.currentSymbol = [Symbol(Myfunc.name, MType(paramlistype ,Myfunc.retType) ,"func") ] +  self.currentSymbol

        env =  [[Symbol("struct", recStruct, ast.receiver)]] + env + [[Symbol(ast.receiver, recStruct, None)]] + c

        #env = [[]] + env + c       
        env = self.visit(Myfunc.body,env)

        self.currentSymbol = self.currentSymbol[1::]
        return c


    def visitPrototype(self,ast, c):
    # name: str
    # params:List[Type]
    # retType: Type # VoidType if there is no return type
    
        found = self.lookup(ast.name, c[0], lambda x:x.name)
        if found :
            raise Redeclared(Prototype(), ast.name )
        c[0] += [ast]
        return c


    def visitIntType(self,ast,c):
        return IntLiteral(None)

    def visitFloatType(self,ast,c):
        return ast

    def visitBoolType(self,ast,c):
        return ast

    def visitStringType(self,ast,c):
        return ast

    def visitArrayType(self,ast,c):
    # dimens:List[Expr]
    # eleType:Type
        for x in ast.dimens:
            self.visit(x,c)
        return ast
    
    def visitStructType(self,ast,c):
    # name: str
    # elements:List[Tuple[str,Type]]
    # methods:List[MethodDecl]
        found = self.lookup(ast.name, c[0], lambda x: x.name)
        if found:
            raise Redeclared(Type(),ast.name)
        
        env = [[]]
        for ele in ast.elements:
            found1 = self.lookup(ele[0], env[0], lambda x: x.name)
            if found1:
                raise Redeclared(Field(), ele[0])
            elif type(found1) is StructType :
                env[0] += [found1]
            else :
                env[0] += [Symbol(ele[0],ele[1],None)]

        for methods in self.methodSymbol:
            if ele[0] == methods.name and ast.name == methods.mtype.name:
                raise Redeclared(Method(), ele[0])

        c[0] += [Symbol(ast.name,ast.elements,"struct")]
        return c
        
    def visitVoidType(self,ast,c):
        return ast
    
    def visitInterfaceType(self,ast,c):
    # name: str
    # methods:List[Prototype]
        found = self.lookup(ast.name, c[0], lambda x: x.name)
        if found:
            raise Redeclared(Type(),ast.name)
        
        env = [[]]
        for meth in ast.methods:
            env = self.visit(meth,env)
        
        for meth in ast.methods:
            if type(meth.retType) is Id:
                meth.retType = self.visit(meth.retType,c)
        c[0] += [Symbol(ast.name,ast.methods,"interface")]
        return c

    def visitBlock(self,ast,c): 
    # member:List[BlockMember]
        for x in ast.member:
            c = self.visit(x,c)
            if not type(c) is list:
                raise TypeMismatch(x)
        return c

    def visitAssign(self,ast,c): 
    # lhs: LHS
    # rhs: Expr    

        leftType = self.visit(ast.lhs,c)

        if type(leftType) is Id:
            c = self.visit(VarDecl(leftType.name, None, ast.rhs),c)
            return c
        
        
        rightType = self.visit(ast.rhs,c)
        if type(rightType) is Id:
            raise Undeclared(Identifier(),rightType.name)
        
        if type(leftType) is VoidType:
            raise TypeMismatch(ast)
        
        if not self.Compare2Type(leftType, rightType,c): 
            raise TypeMismatch(ast)
        
        return c
        

    def visitIf(self,ast,c): 
    # expr:Expr
    # thenStmt:Stmt
    # elseStmt:Stmt # None if there is no else

        exprType = self.visit(ast.expr,c)
        if not isinstance(exprType, BoolType):
            raise TypeMismatch(ast)
        
        env = [[]] + c
        env = self.visit(ast.thenStmt, env)
       
        env = [[]] + c
        if ast.elseStmt:
            env = self.visit(ast.elseStmt, env)

        return c

    def visitForBasic(self,ast,c): 
    # cond:Expr
    # loop:Block
        env = [[]]
        env = env + c

        conditionType = self.visit(ast.cond,c)
        if not isinstance(conditionType, BoolType):
            raise TypeMismatch(ast)
        env = self.visit(ast.loop,env)
        return c


    def visitForStep(self,ast,c): 
    # init:Stmt
    # cond:Expr
    # upda:Assign
    # loop:Block
        env = [[]]
        env = env + c

        env = self.visit(ast.init,env)

        conditionType = self.visit(ast.cond,env)
        if not isinstance(conditionType, BoolType):
            raise TypeMismatch(ast)
        
        self.visit(ast.upda,env)
        env = self.visit(ast.loop,env)
        return c


    def visitForEach(self,ast,c):
    # idx: Id
    # value: Id
    # arr: Expr
    # loop:Block

        env = [[]]
        env = env + c

           
        type3 = self.visit(ast.arr,env)
        type2 = self.visit(ast.idx,env)
        type1 = self.visit(ast.value,env)

        if type(type2) is Id:
            raise Undeclared(Identifier(),type2.name)
        # env[0] += [Symbol(ast.idx.name, IntType(), None)] 


        if type(type1) is Id:
            raise Undeclared(Identifier(),type1.name)
        # env[0] += [Symbol(ast.idx.name, IntType(), None)] 

        if type(type3) is Id:
            raise Undeclared(Identifier(),type3.name)
        if not isinstance(type3,ArrayType):
            raise TypeMismatch(ast)
        
        if len(type3.dimens) == 1:
            type3 = type3.eleType
        else :
            type3.dimens = type3.dimens[1::]
        
        
        # env[0] += [Symbol(ast.value.name, type3, ast.arr)]

        env = self.visit(ast.loop,env)
        return c



    def visitBreak(self,ast,c): 
        return c

    def visitContinue(self,ast,c): 
        return c

    def visitReturn(self,ast,c): 
    # expr:Expr  # None if there is no expr
        found = self.currentSymbol[0]
        
        if type(found.mtype.rettype) is Id:
            returnType1 = self.visit(found.mtype.rettype,c)
        else :
            returnType1 = found.mtype.rettype

        if ast.expr:
            if type(ast.expr) is Id:
                returnType = self.visitIdVar(ast.expr,c)
            else:
                returnType = self.visit(ast.expr,c)
        else : 
            returnType = VoidType()

        
        if type(returnType) is list:
            returnType = VoidType()
        
        
        if type(returnType1) is VoidType and ast.expr:
            raise TypeMismatch(ast)
        
        if type(found.mtype.rettype) is Id:
            returnType1 = self.visit(found.mtype.rettype,c)
        else :
            returnType1 = found.mtype.rettype

        if type(returnType1) is VoidType and type(returnType) is VoidType:
            return c
        elif type(returnType) is str and returnType == "nil":
            return c
        elif type(returnType1) is ArrayType and type(returnType) is ArrayType:
            if not type(returnType1.eleType) is type(returnType.eleType):
                raise TypeMismatch(ast)
            if self.Compare2ArrayType(returnType1,returnType,c):
                return c
        elif type(returnType1) is StructType and type(returnType) is StructType:
            return c
        elif isinstance(returnType1, (IntType,IntLiteral)) and isinstance(returnType, (IntType,IntLiteral)) :
            return c
        elif type(returnType1) == type(returnType):
            return c

        raise TypeMismatch(ast)


    def visitId(self,ast,c):
    #name : str
        found = None

        for structEle in self.structList:
            if ast.name == structEle.name:
                return structEle

        for interfaceEle in self.interfaceList:
            if ast.name == interfaceEle.name:
                return interfaceEle
            
        for envi in c:
            found = self.lookup(ast.name, envi, lambda x:x.name)
            
            if found :
                if isinstance(found,(StructType,InterfaceType)):
                    return found
                elif type(found) is Symbol : 
                    if not type(found.value)  is str:
                        
                        return found.mtype 

        return ast
    

    def visitArrayCell(self,ast,c): 
    # arr:Expr                      dimens:List[Expr]
    # idx:List[Expr]                eleType:Type
        arrType = self.visit(ast.arr,c)

        if type(arrType) is Id:
            raise Undeclared(Identifier(),arrType.name)
        if not type(arrType) is ArrayType:
            raise TypeMismatch(ast)
        
        

        for x in ast.idx:
            typ = self.visit(x,c)
            if type(typ) is Id:
                raise Undeclared(Identifier(),typ.name)
            elif not type(typ) is IntLiteral and not type(typ) is IntType:
                raise TypeMismatch(ast)
            
        if len(ast.idx) > len(arrType.dimens):
            raise TypeMismatch(ast)
        if len(arrType.dimens) == len(ast.idx):      
            return arrType.eleType
        
        eleType = arrType.eleType
        dimens = []

        i = len(ast.idx)
        while i <len(arrType.dimens):
            dimens += [arrType.dimens[i]]   
            i +=1

        return ArrayType(dimens,eleType)
        


    def visitFieldAccess(self,ast,c): 
    # receiver:Expr
    # field:str
        receiverType = self.visit(ast.receiver,c)
        if not type(receiverType) is Id and not type(receiverType) is StructType:
            raise TypeMismatch(ast)

        myStruct = self.lookup(receiverType.name, self.structList, lambda x: x.name)
        
        if not myStruct:
            raise Undeclared(Identifier(),receiverType.name)
        if not type(receiverType) is StructType:
            raise TypeMismatch(ast)
        
        found = self.lookup(ast.field,myStruct.elements, lambda x: x[0])

        if not found :
            raise Undeclared(Field(),ast.field)
        
        if type(found[1]) is Id:
            returnType = self.visit(found[1],c)
        else :
            returnType = found[1]
        return returnType

    def visitBinaryOp(self,ast,c): 
    # op:str
    # left:Expr
    # right:Expr
    
        leftType = self.visit(ast.left,c)
        rightType = self.visit(ast.right,c)

        if type(leftType) is Id:
            raise Undeclared(Identifier(),leftType.name)
    
        if type(rightType) is Id:
            raise Undeclared(Identifier(),rightType.name)
        op = ast.op
        if op == "+":
            if isinstance(leftType,StringType) and isinstance(rightType,StringType):
                return StringType()
            elif (isinstance(leftType,IntLiteral) and isinstance(rightType,IntLiteral)):
                return IntLiteral(leftType.value + rightType.value)
            elif (isinstance(leftType,(IntLiteral, IntType)) and isinstance(rightType,(IntLiteral, IntType))) :
                return IntType()
            elif (isinstance(leftType,FloatType) and isinstance(rightType,FloatType)):
                return FloatType()
            elif (isinstance(leftType,(IntLiteral, IntType)) and isinstance(rightType,FloatType)) or (isinstance(leftType,FloatType) and isinstance(rightType,(IntLiteral, IntType))):
                return FloatType()
            else :
                raise TypeMismatch(ast)
        elif op in ["-","*","/"]:
            if (isinstance(leftType,IntLiteral) and isinstance(rightType,IntLiteral)):
                if op == "-":
                    return IntLiteral(leftType.value - rightType.value)
                if op =="*":
                    return IntLiteral(int(leftType.value * rightType.value))
                if op == "/":
                    return IntLiteral(int(leftType.value / rightType.value))
            
            elif (isinstance(leftType,(IntLiteral, IntType)) and isinstance(rightType,(IntLiteral, IntType))) :
                return IntType()
            elif  (isinstance(leftType,FloatType) and isinstance(rightType,FloatType)):
                return FloatType()
            elif (isinstance(leftType,(IntLiteral, IntType)) and isinstance(rightType,FloatType)) or (isinstance(leftType,FloatType) and isinstance(rightType,(IntLiteral, IntType))):
                return FloatType()
            else :
                raise TypeMismatch(ast)
        elif op =="%":
            if (isinstance(leftType,IntLiteral) and isinstance(rightType,IntLiteral)):
                return IntLiteral(int(leftType.value % rightType.value))
            elif (isinstance(leftType,(IntLiteral, IntType)) and isinstance(rightType,(IntLiteral, IntType))):
                return IntType()
            else :
                raise TypeMismatch(ast)
        elif op in ["==","!=",">","<","<=",">="]:
            if isinstance(leftType, (IntLiteral, IntType)) and isinstance(rightType,(IntLiteral, IntType)):
                return BoolType()
            elif isinstance(leftType,FloatType) and isinstance(rightType, FloatType):
                return BoolType()
            elif isinstance(leftType,StringType) and isinstance(rightType, StringType):
                return BoolType()
            else:
                raise TypeMismatch(ast)
        elif op in ["&&", "||"]:
            if isinstance(leftType,BoolType) and isinstance(rightType, BoolType):
                return BoolType()

        raise TypeMismatch(ast)


    def visitUnaryOp(self,ast,c): 
    # op:str
    # body:Expr
        op = ast.op
        bodyType = self.visit(ast.body,c)
        if op == "-":
            if type(bodyType) is IntLiteral:
                return IntLiteral(- bodyType.value)
            elif isinstance(bodyType, IntType):
                return IntType()
            elif isinstance(bodyType,FloatType):
                return FloatType()
        elif op == "!":
            if isinstance(bodyType, BoolType):
                return BoolType()
        raise TypeMismatch(ast)

    def visitFuncCall(self,ast,c): 
    # funName:str
    # args:List[Expr] # [] if there is no arg 

        allfunclist = self.funcSymbol + self.global_envi1
        namelist = [x.name if (not type(x.value) is str or x.value != "func") and x.name != "struct"  else x.value for x in c[0] ]

 
        globallist = [x.name for x in self.global_envi1]
        allfunclist = list(filter(lambda x: not x.name in namelist or x.name in globallist ,allfunclist))

        
        found = self.lookup(ast.funName, allfunclist , lambda x: x.name )

    
        if not found: 
            raise Undeclared(Function(),ast.funName)

        if type(found.mtype.rettype) is Id:
            found.mtype.rettype = self.visit(found.mtype.rettype,c)

        for i in range(0,len(found.mtype.partype)):
            found.mtype.partype[i] = self.visit(found.mtype.partype[i],c)

        func1 = Symbol(ast.funName, MType([self.visit(e,c) for e in ast.args],found.mtype.rettype), "func")
        Typeright = self.Compare2FuncCall(found,func1,c)

        if not Typeright:
            raise TypeMismatch(ast)
        if type(found.mtype.rettype) is VoidType:
            return c
        
        
        return found.mtype.rettype


    def visitMethCall(self,ast,c): 
    # receiver: Expr
    # metName: str
    # args:List[Expr]        
        receiverType = self.visit(ast.receiver,c)
        

        if type(receiverType) in [IntLiteral,IntType,FloatType,BoolType,StringType]:
            raise TypeMismatch(ast)
    
        found = None
        returnType = None
        MyType = self.lookup(receiverType.name, self.structList, lambda x: x.name)
              
        MyType1 = self.lookup(receiverType.name, self.interfaceList, lambda x: x.name)

        if MyType is None and MyType1 is None:
            raise Undeclared(Method(),ast.metName)
        
        if MyType is None:
            MyType = MyType1
        

        if type(MyType) is StructType:
            found = self.lookup(ast.metName, MyType.methods, lambda x:x.fun.name)
            if not found : 
                raise Undeclared(Method(), ast.metName)  
            myFun = found.fun

            Func1 = Symbol(myFun.name, MType([par.parType for par in myFun.params],myFun.retType),None)
            Func2 = Symbol(ast.metName, MType([self.visit(e,c) for e in ast.args],found.fun.retType), None)
            if not self.Compare2FuncCall(Func1, Func2,c):
                raise TypeMismatch(ast)
            returnType = found.fun.retType
        elif type(MyType) is InterfaceType:
            #name: str
            # params:List[Type]
            # retType: Type # VoidType if there is no return type
            found = self.lookup(ast.metName, MyType.methods, lambda x:x.name)
            if not found : 
                raise Undeclared(Method(), ast.metName)  
            
            Func1 = Symbol(found.name, MType(found.params,found.retType),None)
            Func2 = Symbol(ast.metName, MType([self.visit(e,c) for e in ast.args],found.retType), None)
            if not self.Compare2FuncCall(Func1, Func2,c):
                raise TypeMismatch(ast)
            returnType = found.retType
        
        if not type(returnType) is VoidType:
            return returnType
        else : 
            return c


    def visitIntLiteral(self,ast, c):
        return ast
    
    def visitFloatLiteral(self,ast, c):
        return FloatType()

    def visitStringLiteral(self,ast,c):
        return StringType()

    def visitArrayLiteral(self,ast,c):
        # dimens:List[Expr]
        # eleType: Type
        # value: NestedList

        # ArrayType
        dimen = len(ast.dimens)

        def traverse(x,c):
            if type(x) is list:
                for x1 in x:
                    traverse(x1,c)
            else :
                self.visit(x,c)

        traverse(ast.value,c)


        return ArrayType(ast.dimens,ast.eleType)

    def visitBooleanLiteral(self,ast,c):
        return BoolType()

    def visitStructLiteral(self,ast,c):
        # name:str
        # elements: List[Tuple[str,Expr]] # [] if there is no elements

        # StructType.elements:List[Tuple[str,Type]]
        found = self.lookup(ast.name,self.structList,lambda x : x.name)
        if not found:
            raise Undeclared(Type(),ast.name)

        for i in range (0,len(ast.elements)):
            if found.elements[i][0] !=  ast.elements[i][0]:
                raise TypeMismatch(ast)
            Typ1 = self.visit(found.elements[i][1],c)
            Typ2 = self.visit(ast.elements[i][1],c)

            if type(Typ2) is Id:
                for envi in c:
                    found1 = self.lookup(Typ2.name,envi,lambda x:x.name)
                    if found1 : break
                if not found1:
                    raise Undeclared(Identifier(),Typ2.name)     
            if not self.Compare2Type(Typ1, Typ2,c):
                raise TypeMismatch(ast)
            
        return found
         

    def visitNilLiteral(self,ast,c):
        return "nil"
    
    def visitFirst(self,ast,c):
        if type(ast) is StructType:
            self.structList += [ast]
            return c

        elif type(ast) is InterfaceType:
            self.interfaceList += [ast]
            return c
        
        elif type(ast) is FuncDecl:
            env = [[]]                     
            paramtypeslist = []
            for para in ast.params:
                paramtypeslist += [para.parType]                
            self.funcSymbol += [Symbol(ast.name, MType(paramtypeslist ,ast.retType) , "func")]
            return c
            
        elif type(ast) is MethodDecl:
            receiverType = self.visit(ast.recType,[self.structList])
            
            if type(receiverType) is Id:
                self.structList += [StructType(receiverType.name,[],[])]                          
            found = self.lookup(receiverType.name, self.structList, lambda x:x.name)
            found.methods += [ast]
            return c

        return c
    
    def visitIdVar(self,ast,c):
        for envi in c:
            found = self.lookup(ast.name, envi, lambda x :x.name)
            if found :
                if (found.value and type(found.value) is not str) or not found.value :
                    return found.mtype
        raise Undeclared(Identifier(),ast.name)
    

    # My c structure:

    # c = [[Most local enviroment (in {})],
    #      [Non local enviroments ],
    #      [Global enviroment]
    #     ]

    # visitVarDecl,visitConstDecl--> add Symbol(name,type,init) to c[0]
    # visitFuncDecl --> check if func or method 
    #                       if func : --> create local environment : [[ParamDeclList, Symbol(funname, MType, "func")]]
    #                                    add to c[global] : [Symbol(funname, MType, None)]
    #                        if method: -->
    # visitMethod --> create env = [["method"]] --> visitFuncdecl(env)
    # visitStructType --> add to structList : [StructType]
    # visitInterfaceType --> add to interfaceList : [InterfaceType]

    # visitExp -->check Type and return Type


    # Duyệt lần 1:
    # _ Duyệt qua các struct để cập nhật structList
    # _ Duyệt qua các interface để cập nhật interfaceList
    # _ Duyệt qua các method prototype để
    # *không raise lỗi

    # Duyệt lần 2:
    # _ Duyệt tuần tự từ trên xuống
    # _ Raise lỗi về Redeclared và Undeclared