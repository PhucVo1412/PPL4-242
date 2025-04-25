from Emitter import *
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *


class CodeGenerator:
    def gen(self, ast, path):
        gc = CodeGenVisitor(ast, path)
        gc.visit(ast, None)

class Access():
    def __init__(self, frame : Frame, symbol, isLeft):
        self.frame = frame 
        self.symbol = symbol 
        self.isLeft = isLeft 

class CodeGenVisitor(Visitor):
    def __init__(self, astTree, path):
        self.astTree = astTree
        self.path = path
        self.className = "MiniGO"
        self.emit = Emitter(self.path + "/" + self.className  + ".j")
        
    def visitProgram(self, ast: Program, o : Access):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))

        #! 2.1 init contructor MT22
        frame = Frame("<init>", VoidType())
        self.emit.printout(self.emit.emitMETHOD(lexeme = "<init>", in_ = FunctionType("init", [], VoidType()), isStatic = False, frame = frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", "Ljava/lang/Object;", frame.getStartLabel(), frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitREADVAR("this", self.className, 0, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))   
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    

        frame = Frame("main", VoidType)
        self.emit.printout(self.emit.emitMETHOD(lexeme="main", in_= FunctionType("main", [ArrayType([IntLiteral(1)], StringType())], VoidType()), isStatic = True, frame = frame))
        frame.enterScope(True)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        self.visit(ast.decl[0].body.member[0], Access(frame, [[]], False))
        self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))   
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()    

        self.emit.emitEPILOG()
    
    def visitVarDecl(self, ast, o : Access):
        return None

    def visitConstDecl(self, ast, o : Access):
        return None
   
    def visitFuncDecl(self, ast, o : Access):
        return None

    def visitMethodDecl(self, ast, o : Access):
        return None

    def visitPrototype(self, ast, o : Access):
        return None
    
    def visitIntType(self, ast, o : Access):
        return None
    
    def visitFloatType(self, ast, o : Access):
        return None
    
    def visitBoolType(self, ast, o : Access):
        return None
    
    def visitStringType(self, ast, o : Access):
        return None
    
    def visitVoidType(self, ast, o : Access):
        return None
    
    def visitArrayType(self, ast, o : Access):
        return None
    
    def visitStructType(self, ast, o : Access):
        return None

    def visitInterfaceType(self, ast, o : Access):
        return None
    
    def visitBlock(self, ast: Block, o : Access):
        return None
 
    def visitAssign(self, ast, o : Access):
        return None
   
    def visitIf(self, ast, o : Access):
        return None
    
    def visitForBasic(self, ast, o : Access):
        return None
 
    def visitForStep(self, ast, o : Access):
        return None

    def visitForEach(self, ast, o : Access):
        return None

    def visitContinue(self, ast, o : Access):
        return None
    
    def visitBreak(self, ast, o : Access):
        return None
    
    def visitReturn(self, ast, o : Access):
        return None

    def visitBinaryOp(self, ast, o : Access):
        return None
    
    def visitUnaryOp(self, ast, o : Access):
        return None
    
    def visitFuncCall(self, ast: FuncCall, o : Access):
        frame = o.frame
        argsCode, argsType = self.visit(ast.args[0], o)
        self.emit.printout(argsCode)
        if ast.funName == "putInt":
            self.emit.printout(self.emit.emitINVOKESTATIC(f"io/{ast.funName}", FunctionType(ast.funName, [IntType()], VoidType()), frame))
            return 
        # TODO

    def visitMethCall(self, ast, o : Access):
        return None
    
    def visitId(self, ast, o : Access):
        return None
    
    def visitArrayCell(self, ast, o : Access):
        return None
    
    def visitFieldAccess(self, ast, o : Access):
        return None
    
    def visitIntLiteral(self, ast: IntLiteral, o : Access):
        return self.emit.emitPUSHCONST(ast.value, IntType(), o.frame), IntType()
    
    def visitFloatLiteral(self, ast, o : Access):
        # TODO
        return None
    
    def visitBooleanLiteral(self, ast, o : Access):
        return None
    
    def visitStringLiteral(self, ast, o : Access):
        return None

    def visitArrayLiteral(self, ast, o : Access):
        return None

    def visitStructLiteral(self, ast, o : Access):
        return None

    def visitNilLiteral(self, ast, o : Access):
        return None