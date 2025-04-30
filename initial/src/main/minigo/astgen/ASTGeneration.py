from MiniGoVisitor import MiniGoVisitor
from MiniGoParser import MiniGoParser
from AST import *
from typing import Tuple

#2252650

class ASTGeneration(MiniGoVisitor):
    #program  : decls EOF ;
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return Program(self.visit(ctx.decls()))


    #primitive_literals: INTEGER_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | ID;
    def visitPrimitive_literals(self, ctx:MiniGoParser.Primitive_literalsContext):
        if ctx.INTEGER_LIT():
            if ctx.INTEGER_LIT().getText().startswith(("0x","0X","0o","0O","0b","0B")) :
                return IntLiteral (ctx.INTEGER_LIT().getText())        
            return IntLiteral(int(ctx.INTEGER_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.ID():
            return Id(ctx.ID().getText())


    # literal: INTEGER_LIT 
    #    | FLOAT_LIT 
    #    | STRING_LIT 
    #    | TRUE | FALSE
    #    | NIL
    #    | array_literals 
    #    | struct_literals;
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        if ctx.INTEGER_LIT():
            if ctx.INTEGER_LIT().getText().startswith(("0x","0X","0o","0O","0b","0B")) :
                return IntLiteral (ctx.INTEGER_LIT().getText())        
            return IntLiteral(int(ctx.INTEGER_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.NIL():
            return NilLiteral()
        elif ctx.array_literals(): 
            return self.visit(ctx.array_literals())
        elif ctx.struct_literals(): 
            return self.visit(ctx.struct_literals())

    # types : array_type types
    #| INT 
    #| STRING 
    #| FLOAT 
    #| BOOLEAN 
    #| ID ;
    def visitTypes(self, ctx:MiniGoParser.TypesContext):
        if ctx.INT():
            return IntType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.array_type():
            dimens = self.visit(ctx.array_type())
            eleType = self.visit(ctx.types())
            return ArrayType(dimens,eleType)
        


    # idlist: ID COMMA idlist | ID;
    def visitIdlist(self, ctx:MiniGoParser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())


    # array_literals: array_type ( INT | STRING | FLOAT | BOOLEAN | ID) LSB element_list RSB;
    def visitArray_literals(self, ctx:MiniGoParser.Array_literalsContext):
        dimens = self.visit(ctx.array_type())
        if ctx.INT():
            eleType = IntType()
        elif ctx.FLOAT():
            eleType = FloatType()
        elif ctx.STRING():
            eleType = StringType()
        elif ctx.BOOLEAN():
            eleType = BoolType()
        else :
            eleType = Id(ctx.ID().getText())
        
        value = self.visit(ctx.element_list())
        return ArrayLiteral(dimens, eleType, value)


    # array_type : LB (INTEGER_LIT|ID) RB array_type | LB (INTEGER_LIT|ID) RB ;
    def visitArray_type(self, ctx:MiniGoParser.Array_typeContext):
        if ctx.INTEGER_LIT():
            if ctx.INTEGER_LIT().getText().startswith(("0x","0X","0o","0O","0b","0B")) :
                element = IntLiteral (ctx.INTEGER_LIT().getText())        
            else:
                element =  IntLiteral(int(ctx.INTEGER_LIT().getText()))
        elif ctx.ID():
            element = Id(ctx.ID().getText())
        
        if ctx.getChildCount() == 3:
            return [element]
        return [element] + self.visit(ctx.array_type())

    # element_list : element COMMA element_list | element;
    def visitElement_list(self, ctx:MiniGoParser.Element_listContext):
        value = [self.visit(ctx.element())]
        if ctx.getChildCount() == 1:
            return value
        return value + self.visit(ctx.element_list())


    # element: primitive_literals| struct_literals | LSB element_list RSB;
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return self.visit(ctx.element_list())


    # struct_literals: ID LSB struct_attlist RSB;
    def visitStruct_literals(self, ctx:MiniGoParser.Struct_literalsContext):
        name = ctx.ID().getText()
        elements = self.visit(ctx.struct_attlist())
        return StructLiteral(name,elements)


    # struct_attlist:  struct_attlist_prime |; .
    def visitStruct_attlist(self, ctx:MiniGoParser.Struct_attlistContext):
        return self.visit(ctx.struct_attlist_prime()) if ctx.struct_attlist_prime() else []


    # struct_attlist_prime : ID COLON expression COMMA struct_attlist_prime|  ID COLON expression;
    def visitStruct_attlist_prime(self, ctx:MiniGoParser.Struct_attlist_primeContext):
        fieldName = ctx.ID().getText()
        fieldVal = self.visit(ctx.expression())
        if ctx.getChildCount() == 3:
            return [(fieldName,fieldVal)]
        return [(fieldName,fieldVal)] + self.visit(ctx.struct_attlist_prime())

    # func_call: ID LCB list_expression? RCB ;
    def visitFunc_call(self, ctx:MiniGoParser.Func_callContext):
        funName = ctx.ID().getText()
        args = self.visit(ctx.list_expression()) if ctx.list_expression() else []
        return FuncCall(funName, args)


    # list_expression:  expression COMMA list_expression| expression ;
    def visitList_expression(self, ctx:MiniGoParser.List_expressionContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.list_expression())


    # method_call: dot_operator DOT func_call  ;
    def visitMethod_call(self, ctx:MiniGoParser.Method_callContext):
        func = self.visit(ctx.func_call())

        receiver = self.visit(ctx.dot_operator())
        metName = func.funName
        args = func.args
        return MethCall(receiver,metName, args)


    # dot_operator: dot_operator DOT (ID | array_access) | (ID | array_access) ;
    def visitDot_operator(self, ctx:MiniGoParser.Dot_operatorContext):
        if ctx.getChildCount() == 1:  
            return Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.array_access())
        else :
            if ctx.ID():
                return FieldAccess( self.visit(ctx.dot_operator()) , ctx.ID().getText())
            elif ctx.array_access():
                temp = self.visit(ctx.array_access())
                return ArrayCell( FieldAccess( self.visit(ctx.dot_operator()) , str(temp.arr.name)), temp.idx)

        


    # expression: expression OR expression1 | expression1;
    def visitExpression(self, ctx:MiniGoParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1())
        e = self.visit(ctx.expression())
        e1 = self.visit(ctx.expression1())
        op = str(ctx.OR().getText())
        return BinaryOp(op,e,e1)


    # expression1: expression1 AND expression2 | expression2;
    def visitExpression1(self, ctx:MiniGoParser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2())
        e = self.visit(ctx.expression1())
        e1 = self.visit(ctx.expression2())
        op = str(ctx.AND().getText())
        return BinaryOp(op,e,e1)


    # expression2: expression2 (COM_EQ | COM_GEQ | COM_GT | COM_LEQ | COM_LT | COM_UEQ) expression3 | expression3;
    def visitExpression2(self, ctx:MiniGoParser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        e = self.visit(ctx.expression2())
        e1 = self.visit(ctx.expression3())
        op = str(ctx.getChild(1).getText())
        return BinaryOp(op,e,e1)


    # expression3: expression3 (ADD | SUB) expression4 | expression4;
    def visitExpression3(self, ctx:MiniGoParser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        e = self.visit(ctx.expression3())
        e1 = self.visit(ctx.expression4())
        op = str(ctx.getChild(1).getText())
        return BinaryOp(op,e,e1)



    # expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
    def visitExpression4(self, ctx:MiniGoParser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        e = self.visit(ctx.expression4())
        e1 = self.visit(ctx.expression5())
        op = str(ctx.getChild(1).getText())
        return BinaryOp(op,e,e1)



    # expression5: NOT expression5 | SUB expression5 | expression6;
    def visitExpression5(self, ctx:MiniGoParser.Expression5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression6())
        e = self.visit(ctx.expression5())
        op = str(ctx.getChild(0).getText())
        return UnaryOp(op,e)



    # expression6: expression6 LB expression RB
    #| expression6 DOT ID LCB list_expression? RCB
    #| expression7;
    #| expression6 DOT ID
    def visitExpression6(self, ctx:MiniGoParser.Expression6Context):
        if ctx.LB(): 
            expression6 = self.visit(ctx.expression6())
            if type(expression6) == ArrayCell:
                return ArrayCell(expression6.arr, expression6.idx  + [self.visit(ctx.expression())])
            return ArrayCell(expression6, [self.visit(ctx.expression())])
        elif ctx.LCB():
            receiver = self.visit(ctx.expression6())
            metName = ctx.ID().getText()
            args = self.visit(ctx.list_expression()) if ctx.list_expression()  else []
            return MethCall(receiver,metName,args)
        elif ctx.expression7():
            return self.visit(ctx.expression7())
        else: 
            receiver = self.visit(ctx.expression6())
            field = ctx.ID().getText()
            return FieldAccess(receiver,field)
            


    # expression7: LCB expression RCB | ID | literal | func_call  ;
    def visitExpression7(self, ctx:MiniGoParser.Expression7Context):
        if ctx.getChildCount() == 3:
            return self.visit(ctx.expression())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))
        



    # array_access : ID array_op;
    def visitArray_access(self, ctx:MiniGoParser.Array_accessContext):
        arr = Id(ctx.ID().getText())
        idx = self.visit(ctx.array_op())
        return ArrayCell(arr,idx)


    # array_op: LB expression RB array_op | LB expression RB ;
    def visitArray_op(self, ctx:MiniGoParser.Array_opContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.array_op())


    # struct_access: struct_access DOT (array_access | ID) | (array_access | ID)  DOT (array_access | ID);
    def visitStruct_access(self, ctx:MiniGoParser.Struct_accessContext):
        if ctx.struct_access():
            if ctx.ID():
                return FieldAccess( self.visit(ctx.struct_access()) , ctx.ID(0).getText())
            elif ctx.array_access():
                temp = self.visit(ctx.array_access(0))
                return ArrayCell( FieldAccess( self.visit(ctx.struct_access()) , str(temp.arr.name)), temp.idx)
        else :
            if ctx.ID(0) and ctx.ID(1):
                # Case 3a: ID DOT ID
                return FieldAccess(Id(ctx.ID(0).getText()), ctx.ID(1).getText())
            elif ctx.ID(0) and ctx.array_access():
                # Case 3b: ID DOT array_access
                temp = self.visit(ctx.array_access(0))
                return ArrayCell(FieldAccess(Id(ctx.ID(0).getText()), str(temp.arr.name)), temp.idx)
            elif ctx.array_access(0) and ctx.ID():
                # Case 4: array_access DOT ID
                temp = self.visit(ctx.array_access(0))
                return FieldAccess(ArrayCell(temp.arr, temp.idx), ctx.ID().getText())
            elif ctx.array_access(0) and ctx.array_access(1):
                # Case 5: array_access DOT array_access
                    temp1 = self.visit(ctx.array_access(0))
                    temp2 = self.visit(ctx.array_access(1))
                    return ArrayCell(FieldAccess(ArrayCell(temp1.arr, temp1.idx), str(temp2.arr.name)), temp2.idx)   

    # decl: funcdecl | vardecl | struct_decl | method_decl | interface_decl  ;
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visit(ctx.getChild(0))


    # decls: decl decls | decl;
    def visitDecls(self, ctx:MiniGoParser.DeclsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decls())

    # vardecl: VAR ID types? (EQ expression) (SEMI)
    #  |  VAR ID types  (SEMI)
    #  |  CONST ID EQ expression  (SEMI);
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        if ctx.VAR():
            varName  = ctx.ID().getText()
            varType = self.visit(ctx.types()) if ctx.types() else None
            varInit = self.visit(ctx.expression()) if ctx.expression() else None
            return VarDecl(varName, varType, varInit)
        else : 
            conName = ctx.ID().getText()
            conType = self.visit(ctx.types()) if ctx.types() else None
            iniExpr = self.visit(ctx.expression()) 
            return ConstDecl(conName,conType,iniExpr)


    # funcdecl: FUNC ID LCB (paramlist|paramlist1) RCB types? LSB stmts return_stmt? RSB (SEMI);
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        name = ctx.ID().getText()
        params = []
        if ctx.paramlist():
            params = self.visit(ctx.paramlist())  
        elif  ctx.paramlist1(): 
            params_list = self.visit(ctx.paramlist1())
            params = [ParamDecl(varname.name,vartypes) for (varname, vartypes) in params_list]
        retType = self.visit(ctx.types()) if ctx.types() else VoidType()
        blockmember = self.visit(ctx.stmts()) + ([self.visit(ctx.return_stmt())] if ctx.return_stmt() else [])

        body = Block(blockmember)
        #body = Block([Return(None)])
        return FuncDecl(name , params, retType, body)
    

    # paramlist: paramlist_prime | ;
    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        if ctx.paramlist_prime():
            return self.visit(ctx.paramlist_prime())
        return []


    # paramlist_prime : ID types COMMA paramlist_prime | ID types;
    def visitParamlist_prime(self, ctx:MiniGoParser.Paramlist_primeContext):
        parName = ctx.ID().getText()
        parType = self.visit(ctx.types())
        if ctx.paramlist_prime():
            return [ParamDecl(parName,parType)] + self.visit(ctx.paramlist_prime())
        return  [ParamDecl(parName,parType)]


    # struct_decl :  TYPE ID STRUCT LSB declist RSB (SEMI);
    def visitStruct_decl(self, ctx:MiniGoParser.Struct_declContext):
        return StructType(ctx.ID().getText(), self.visit(ctx.declist()),[])

    # declist:  ID types SEMI declist |  ID types SEMI   ;
    def visitDeclist(self, ctx:MiniGoParser.DeclistContext):
        fieldname = ctx.ID().getText()
        fieldtype = self.visit(ctx.types())
        if ctx.getChildCount() == 3:
            return [(fieldname,fieldtype)]
        return [(fieldname,fieldtype)] + self.visit(ctx.declist())


    # method_decl: FUNC LCB ID ID RCB ID LCB (paramlist|paramlist1) RCB types? LSB stmts return_stmt? RSB (SEMI);
    def visitMethod_decl(self, ctx:MiniGoParser.Method_declContext):
        receiver = ctx.ID(0).getText()
        recType = Id(ctx.ID(1).getText())

        name = ctx.ID(2).getText()
        if ctx.paramlist():
            params = self.visit(ctx.paramlist())  
        else:
            params_list = self.visit(ctx.paramlist1())
            params = [ParamDecl(varname.name,vartypes) for (varname, vartypes) in params_list]
        retType = self.visit(ctx.types()) if ctx.types() else VoidType()
        body = Block(self.visit(ctx.stmts()) + ([self.visit(ctx.return_stmt())] if ctx.return_stmt() else []))
        func = FuncDecl(name,params,retType,body)

        return MethodDecl(receiver,recType,func)


    # interface_decl: TYPE ID INTERFACE LSB decl_list1 RSB (SEMI);
    def visitInterface_decl(self, ctx:MiniGoParser.Interface_declContext):
        name = ctx.ID().getText()
        methods = self.visit(ctx.decl_list1())
        return InterfaceType(name,methods)


    # decl_list1: ID LCB paramlist1 RCB types? (SEMI) decl_list1 |  ID LCB paramlist1 RCB types? (SEMI)  ;
    def visitDecl_list1(self, ctx:MiniGoParser.Decl_list1Context):
        name = ctx.ID().getText()
        params_list = self.visit(ctx.paramlist1())
        params = [y for (x,y) in params_list]
        retType = self.visit(ctx.types()) if ctx.types() else VoidType()
        if ctx.decl_list1():
            return [Prototype(name,params,retType)] + self.visit(ctx.decl_list1())
        return [Prototype(name,params,retType)]


    # paramlist1: paramlist1_prime | ;
    def visitParamlist1(self, ctx:MiniGoParser.Paramlist1Context):
        return self.visit(ctx.paramlist1_prime()) if ctx.paramlist1_prime() else []


    # paramlist1_prime: idlist types COMMA paramlist1_prime | idlist types;
    def visitParamlist1_prime(self, ctx:MiniGoParser.Paramlist1_primeContext):
        id_list = self.visit(ctx.idlist())
        typesc = self.visit(ctx.types())
        result = [(x,typesc) for x in id_list]
        if ctx.getChildCount() == 2:
            return result
        return result + self.visit(ctx.paramlist1_prime())


    # stmts: stmt stmts  | stmt ;
    def visitStmts(self, ctx:MiniGoParser.StmtsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.stmt())]
        return [self.visit(ctx.stmt())] + self.visit(ctx.stmts())


    #stmt: (assign_stmt | break_stmt| call_stmt| continue_stmt | return_stmt  ) (SEMI)
    # | (if_stmt | for_stmt) (SEMI)  
    # | vardecl  ;
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visit(ctx.getChild(0))


    # assign_stmt: variable (ASSIGN | PLUS_EQ | MINUS_EQ | MUL_EQ | MOD_EQ | DIV_EQ ) expression ;
    def visitAssign_stmt(self, ctx:MiniGoParser.Assign_stmtContext):
        if ctx.ASSIGN():
            return Assign(self.visit(ctx.variable()), self.visit(ctx.expression()))
        elif ctx.PLUS_EQ():
            return Assign(self.visit(ctx.variable()), BinaryOp("+",self.visit(ctx.variable()),self.visit(ctx.expression())))
        elif ctx.MINUS_EQ():
            return Assign(self.visit(ctx.variable()), BinaryOp("-",self.visit(ctx.variable()),self.visit(ctx.expression())))
        elif ctx.MUL_EQ():
            return Assign(self.visit(ctx.variable()), BinaryOp("*",self.visit(ctx.variable()),self.visit(ctx.expression())))
        elif ctx.MOD_EQ():
            return Assign(self.visit(ctx.variable()), BinaryOp("%",self.visit(ctx.variable()),self.visit(ctx.expression())))
        elif ctx.DIV_EQ():
            return Assign(self.visit(ctx.variable()), BinaryOp("/",self.visit(ctx.variable()),self.visit(ctx.expression())))

    # variable: struct_access | array_access | ID  ;
    def visitVariable(self, ctx:MiniGoParser.VariableContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        return self.visit(ctx.getChild(0))


    # if_stmt: IF (LCB expression RCB) LSB stmts RSB elseif_stmt? else_stmt?;
    def visitIf_stmt(self, ctx:MiniGoParser.If_stmtContext):
        if (ctx.elseif_stmt()):
            expr = self.visit(ctx.expression())
            thenStmt = Block(self.visit(ctx.stmts()))
            elseifList = self.visit(ctx.elseif_stmt())  
            else_stmt = Block(self.visit(ctx.else_stmt())) if ctx.else_stmt() else None
            return If(expr, thenStmt, self.IfHandler(elseifList, else_stmt))

        else :
            expr = self.visit(ctx.expression())
            thenStmt = Block(self.visit(ctx.stmts()))
            elseStmt = Block(self.visit(ctx.else_stmt())) if ctx.else_stmt() else None
            return If(expr,thenStmt, elseStmt)
            


    # elseif_stmt: ELSE IF (LCB expression RCB) LSB stmts RSB elseif_stmt? | ELSE IF (LCB expression RCB) LSB stmts RSB ;
    def visitElseif_stmt(self, ctx:MiniGoParser.Elseif_stmtContext):
        expr = self.visit(ctx.expression())
        thenStmt = Block(self.visit(ctx.stmts()))

        if ctx.elseif_stmt():
            return [(expr,thenStmt)] + self.visit(ctx.elseif_stmt())
        return [(expr,thenStmt)]


    # else_stmt: ELSE LSB stmts RSB;
    def visitElse_stmt(self, ctx:MiniGoParser.Else_stmtContext):
        return self.visit(ctx.stmts())


    def IfHandler(self,elseif_stmts :List[Tuple[Expr,Block]], else_stmt: Block):
        if len(elseif_stmts) == 0:
            return else_stmt
        exp, block = elseif_stmts[0]
        return If(exp, block, self.IfHandler(elseif_stmts[1:], else_stmt))



    # for_stmt: FOR condition LSB stmts RSB;
    def visitFor_stmt(self, ctx:MiniGoParser.For_stmtContext):
        loop = Block(self.visit(ctx.stmts()))
        (type,condi) = self.visit(ctx.condition())
        if type == 1:
            return ForEach(condi[0],condi[1],condi[2],loop)
        elif type == 2:
            return ForBasic(condi[0],loop)
        elif type == 0:
            return ForStep(condi[0],condi[1],condi[2],loop)


    # condition: (assign_stmtfor | vardeclfor) SEMI expression? SEMI assign_stmtfor?, ForStep
    #    | (ID | UNDER)  COMMA ID ASSIGN RANGE expression; ForEach
    #    | expression ; ForBasic
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        if ctx.SEMI():
            init = self.visit(ctx.getChild(0))
            cond = self.visit(ctx.expression()) if ctx.expression() else None
            upda = self.visit(ctx.getChild(ctx.getChildCount()-1)) if ctx.getChild(ctx.getChildCount()-1) is not ctx.SEMI(1) else None
            return (0,[init,cond,upda])
        elif ctx.getChildCount() == 6:
            idx = Id(ctx.getChild(0).getText())
            value = Id(ctx.getChild(2).getText())
            arr = self.visit(ctx.expression())
            return (1,[idx,value,arr])
        else:
            return (2,[self.visit(ctx.expression())])


    # assign_stmtfor : ID (ASSIGN | PLUS_EQ | MINUS_EQ | MUL_EQ | MOD_EQ | DIV_EQ ) expression ;
    def visitAssign_stmtfor(self, ctx:MiniGoParser.Assign_stmtforContext):
        if ctx.ASSIGN():
            return Assign(Id(ctx.ID().getText()), self.visit(ctx.expression()))
        elif ctx.PLUS_EQ():
            return Assign(Id(ctx.ID().getText()), BinaryOp("+",Id(ctx.ID().getText()),self.visit(ctx.expression())))
        elif ctx.MINUS_EQ():
            return Assign(Id(ctx.ID().getText()), BinaryOp("-",Id(ctx.ID().getText()),self.visit(ctx.expression())))
        elif ctx.MUL_EQ():
            return Assign(Id(ctx.ID().getText()), BinaryOp("*",Id(ctx.ID().getText()),self.visit(ctx.expression())))
        elif ctx.MOD_EQ():
            return Assign(Id(ctx.ID().getText()), BinaryOp("%",Id(ctx.ID().getText()),self.visit(ctx.expression())))
        elif ctx.DIV_EQ():
            return Assign(Id(ctx.ID().getText()), BinaryOp("/",Id(ctx.ID().getText()),self.visit(ctx.expression())))


    # vardeclfor: VAR ID types? (EQ expression);
    def visitVardeclfor(self, ctx:MiniGoParser.VardeclforContext):
        lhs = ctx.ID().getText()
        rhs = self.visit(ctx.expression())
        varType = self.visit(ctx.types()) if ctx.types() else None
        return VarDecl(lhs,varType,rhs)


    # break_stmt: BREAK ;break_stmt: BREAK ;
    def visitBreak_stmt(self, ctx:MiniGoParser.Break_stmtContext):
        return Break()


    # continue_stmt: CONTINUE ;continue_stmt: CONTINUE ;
    def visitContinue_stmt(self, ctx:MiniGoParser.Continue_stmtContext):
        return Continue()


    #  call_stmt:  func_call 
    #    | method_call; 
    def visitCall_stmt(self, ctx:MiniGoParser.Call_stmtContext):
        return self.visit(ctx.getChild(0))


    # return_stmt : RETURN expression? ;
    def visitReturn_stmt(self, ctx:MiniGoParser.Return_stmtContext):
        e = self.visit(ctx.expression()) if ctx.expression() else None
        return Return(e)

    

