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
        pass

    def visitParamDecl(self,ast, o):
        pass

    def visitVarDecl(self, ast, o):
        pass
    
    def visitConstDecl(self, ast, o):
        pass

    def visitFuncDecl(self, ast, o):
        pass
    
    def visitMethodDecl(self, ast, o):
        pass
    
    def visitPrototype(self, ast, o):
        pass    

    def visitIntType(self, ast, o):
        pass 

    def visitFloatType(self, ast, o):
        pass

    def visitBoolType(self, ast, o):
        pass

    def visitStringType(self, ast, o):
        pass

    def visitVoidType(self, ast, o):
        pass

    def visitArrayType(self, ast, o):
        pass
    
    def visitStructType(self, ast, o):
        pass

    def visitInterfaceType(self, ast, o):
        pass

    def visitBlock(self, ast, o):
        pass

    def visitAssign(self, ast, o):
        pass
    
    def visitIf(self, ast, o):
        pass

    def visitForBasic(self, ast, o):
        pass

    def visitForStep(self, ast, o):
        pass

    def visitBreak(self, ast, o):
        pass

    def visitContinue(self, ast, o):
        pass

    def visitReturn(self, ast, o):
        pass

    def visitId(self, ast, o):
        found = next(filter(lambda x: x.name == ast.name, o.sym), None)

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
        pass

    def visitFieldAccess(self, ast, o):
        pass

    def visitBinaryOp(self, ast, o):
        pass
        
    def visitUnaryOp(self, ast, o):
        pass

    def visitFuncCall(self, ast, o):
        pass

    def visitMethCall(self, ast, o):
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
        pass

    def visitStructLiteral(self, ast, o):
        pass

    def visitNilLiteral(self, ast, o):
        pass


    
