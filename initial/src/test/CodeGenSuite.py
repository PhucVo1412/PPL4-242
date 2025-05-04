import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_501(self):
    #     input = """func main() {putInt(5);};"""
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
    # def test_502(self):
    #     input = """func main() {var a int = 20;  putInt(a);};"""
    #     expect = "20"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))
    # def test_503(self):
    #     input = """var a int = 10; func main() { putInt(a);};"""
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    # def test_504(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
    #     expect = "25"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))
    # def test_505(self):
    #     input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
    #     expect = "500"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))
    # def test_506(self):  
    #     input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
    #     expect = "5000"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_507(self):
    #     """
    #     func main() {
    #         putInt(5)
    #     }
    #     """
    #     input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt",[IntLiteral(5)])]))])
    #     self.assertTrue(TestCodeGen.test(input, "5", 507))    

    # def test_508(self):
    #     """
    #     func main() {
    #         putFloat(1.0)
    #     }
    #     """
    #     input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)])]))])
    #     self.assertTrue(TestCodeGen.test(input, "1.0", 508))

    # def test_509(self):
    #     input = """
    #     func foo(a int , c int) {
    #         var b int = a + c;
    #         putInt(b);
    #     };
    #     func main() {
    #         foo(2, 3);
    #         }
    #     """
    #     self.assertTrue(TestCodeGen.test(input, "5", 509)) 

    # def test_510(self):
    #     input = """
    #     func main() {
    #         var a float = 3.0;
    #         putFloat(1 + a)
    #     }
    #      """
    #     self.assertTrue(TestCodeGen.test(input,"4.0",510)) 

    # def test_511(self):
    #     input = """
    #     func main() {
    #         var a int = 3;
    #         var b int = 4;
    #         putInt(a + b)
    #     }
    #      """
    #     self.assertTrue(TestCodeGen.test(input,"7",511))
    
    # def test_512(self):
    #     input = """
    #     func main() {
    #         var a int = 3;
    #         var b int = 4;
    #         putInt(a - b)
    #     }
    #      """
    #     self.assertTrue(TestCodeGen.test(input,"-1",512))

    # def test_513(self):
    #     input = """
    #     func main() {
    #         var a1 int = 5;
    #         var a2 int = 7;
    #         putInt(a1 * a2)
    #     }
    #      """
    #     self.assertTrue(TestCodeGen.test(input,"35",513))

    def test_514(self):
        input = """func main() {
    if (true) {
        putString("Hello")
    } 
}
"""
        self.assertTrue(TestCodeGen.test(input,"Hello",514))

    def test_515(self):
        input = """
        func main() {
        if (true) {
            putString("Hello")
        } else {
            putString("World")
        }
        }
    """
        self.assertTrue(TestCodeGen.test(input,"Hello",515))
    
    def test_516(self):
        input = """
        func main() {
        if (false && true) {
            putString("Hello")
        } else if (true || false){
            putString("World")
        }
        }
    """
        self.assertTrue(TestCodeGen.test(input,"World",516))