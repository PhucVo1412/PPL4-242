import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int_literal(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_local_var(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_global_var(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_int_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_local_var_ast(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_global_var_ast(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,506))


    def test_507(self):
        """
        func main() {
            putInt(5)
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt",[IntLiteral(5)])]))])
        self.assertTrue(TestCodeGen.test(input, "5", 507))    

    def test_508(self):
        """
        func main() {
            putFloat(1.0)
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)])]))])
        self.assertTrue(TestCodeGen.test(input, "1.0", 508))

    def test_509(self):
        input = """
        func foo(a int, c int) {
            var b = a + c;
            putInt(b)
        }
        func main() {
            foo(2, 3)
        }
        func foo1() int {return 1;}
                """
        self.assertTrue(TestCodeGen.test(input, "5", 509)) 

    def test_510(self):
        input = """
        func fvoid() {putStringLn("VoTien");}

        var global = fint()
        func main() {
            fvoid();
            putFloatLn(global + 2.0)

            var local = "a";
            putBoolLn(local <= "b")
            local += "c"
            putStringLn(local)

        };

        func fint() int {return 1;}
        """
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",510)) 

    def test_511(self):
        input = """
        func foo() int {return foo1();}
        var a = foo() + foo1();
        func main() {
            putInt(a)
            a := foo()
            putInt(a)
        }
        func foo1() int {return 1;}
        """
        self.assertTrue(TestCodeGen.test(input, "21", 511))  
    
    def test_512(self):
        input ="""
        func main() {
            putFloat(1.0)
        }
        """
        #  Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)])]))])
        self.assertTrue(TestCodeGen.test(input, "1.0", 512))

    def test_513(self):
        input = """
        func main() {
            putIntLn(5 % 2)
            putIntLn(2 % 5)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n", 513))

    def test_514(self):
        input = """
        func main() {
            putBoolLn(5.0 > 2.0)
            putBoolLn(5.0 < 2.0)
            putBoolLn(5.0 <= 5.0)
            putBoolLn(5.0 >= 5.0)
            putBoolLn(5.0 == 5.0)
            putBoolLn(5.0 != 5.0)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "true\nfalse\ntrue\ntrue\ntrue\nfalse\n", 514))

    def test_515(self):
        input = """
        func main() {
            putBoolLn("apple" > "banana")     // False
            putBoolLn("apple" < "banana")     // True
            putBoolLn("apple" <= "apple")     // True
            putBoolLn("banana" >= "apple")    // True
            putBoolLn("hello" == "hello")     // True
            putBoolLn("hello" != "hello")     // False
        }
        """
        self.assertTrue(TestCodeGen.test(input, "false\ntrue\ntrue\ntrue\ntrue\nfalse\n", 515))


    def test_516(self):
        input = """
func main() {
    putBoolLn(! true)
    putBoolLn(! false)
    putIntLn(-1)
    putFloatLn(-1.0)
}
     """
        self.assertTrue(TestCodeGen.test(input, "false\ntrue\n-1\n-1.0\n", 516))

    def test_517(self):
        input = """
        func foo() int {return 1;}        

        func main() {
            putInt(foo())
        }
            """
        self.assertTrue(TestCodeGen.test(input, "1", 517))

    def test_518(self):
        input = """
        func fooInt(a int) int {  return a; }
        func fooFloat(a float) float {  return a; }
        func fooString(a string) string { return a; }
        func fooBool(a boolean) boolean { return a; }

        func main() {
            putInt(fooInt(2));
            putFloat(fooFloat(1.5));
            putString(fooString("S"));
            putBool(fooBool(true));
        }
                
                """
        self.assertTrue(TestCodeGen.test(input, "21.5Strue", 518))

    def test_519(self):
        input = """
    func main() {
        var f = true;
        var g boolean;

        putBoolLn(f)
        putBool(g)
    }
     """
        self.assertTrue(TestCodeGen.test(input, "true\nfalse", 519))

    def test_520(self):
        input = """
        func main() {
            a := getString()
            putString(a)
            return
        }
        """
        self.assertTrue(TestCodeGen.test(input, "VOTIEN", 520))

    def test_521(self):
        input = """
        func main() {
            var a = 1 + 2.0;
            var b = 1.0 > 2.0;
            var c = "vo" + "tien";
            var d = "a" < "b";

            putFloatLn(a)
            putBoolLn(b)
            putStringLn(c)
            putBoolLn(d)
        }
        """
        self.assertTrue(TestCodeGen.test(input,"3.0\nfalse\nvotien\ntrue\n",521)) 

        
        
    # def test_509(self):
    #     input = """
    #     func main() {
    #         var a [1] int ;
    #         a[0] := 1
    #         putInt(a[0]);
    #     }
    #     """
    #     self.assertTrue(TestCodeGen.test(input,"1",509))

    # def test_510(self):
    #     input = """
    #     func main() {
    #         var a [1][1][1] int  = [1][1][1] int {{{0}}};
    #         a[0][0][0] := 1
    #         putInt(a[0][0][0]);
    #     }
    #     """
    #     self.assertTrue(TestCodeGen.test(input,"1",510))