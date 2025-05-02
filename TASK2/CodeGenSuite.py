"""
 * Initial code for Assignment
 * Programming Language Principles
 * Author: Võ Tiến
 * Link FB : https://www.facebook.com/profile.php?id=100056605580171
 * Link Group : https://www.facebook.com/groups/211867931379013
 * Date: 02.04.2024
"""
import unittest
from TestUtils import TestCodeGen
import inspect
from AST import *

"""
    (cd java_byte_code/test_001 && 
    java  -jar ../jasmin.jar MiniGoClass.j && 
    java -cp ../_io:. MiniGoClass)
"""
class CodeGenSuite(unittest.TestCase):

    def test_501(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
    def test_502(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
    def test_503(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
    def test_504(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
    def test_505(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))
    def test_506(self):  
        input = Program([VarDecl("a",IntType(),IntLiteral(5000)),FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [Id("a")])]))])
        expect = "5000"
        self.assertTrue(TestCodeGen.test(input,expect,inspect.stack()[0].function))


    def test_507(self):
        """
        func main() {
            putInt(5)
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt",[IntLiteral(5)])]))])
        self.assertTrue(TestCodeGen.test(input, "5", inspect.stack()[0].function))    

    def test_508(self):
        """
        func main() {
            putFloat(1.0)
        }
        """
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)])]))])
        self.assertTrue(TestCodeGen.test(input, "1.0", inspect.stack()[0].function))

    def test_509(self):
        input = """
        func foo(a int , c int) {
            var b int = a + c;
            putInt(b);
        };
        func main() {
            foo(2, 3);
        };
        func foo1() int {return 1;};
                """
        self.assertTrue(TestCodeGen.test(input, "5", inspect.stack()[0].function)) 

    def test_510(self):
        input = """
        func main() {
            var a float = 3.0;
            putFloat(1 + a)
        }
         """
        self.assertTrue(TestCodeGen.test(input,"4.0",inspect.stack()[0].function)) 

    def test_511(self):
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
        self.assertTrue(TestCodeGen.test(input,"VoTien\n3.0\ntrue\nac\n",inspect.stack()[0].function)) 

    def test_512(self):
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
        self.assertTrue(TestCodeGen.test(input, "21", inspect.stack()[0].function))  
    
    def test_512(self):
        input ="""
        func main() {
            putFloat(1.0)
        }
        """
        #  Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putFloat",[FloatLiteral(1.0)])]))])
        self.assertTrue(TestCodeGen.test(input, "1.0", inspect.stack()[0].function))

    def test_513(self):
        input = """
        func main() {
            putIntLn(5 % 2)
            putIntLn(2 % 5)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1\n2\n", inspect.stack()[0].function))

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
        self.assertTrue(TestCodeGen.test(input, "true\nfalse\ntrue\ntrue\ntrue\nfalse\n", inspect.stack()[0].function))

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
        self.assertTrue(TestCodeGen.test(input, "false\ntrue\ntrue\ntrue\ntrue\nfalse\n", inspect.stack()[0].function))


    def test_516(self):
        input = """
        func main() {
            putBoolLn(! true)
            putBoolLn(! false)
            putIntLn(-1)
            putFloatLn(-1.0)
        }
     """
        self.assertTrue(TestCodeGen.test(input, "false\ntrue\n-1\n-1.0\n", inspect.stack()[0].function))

    def test_517(self):
        input = """
        func foo() int {return 1;}        

        func main() {
            putInt(foo())
        }
            """
        self.assertTrue(TestCodeGen.test(input, "1", inspect.stack()[0].function))

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
        self.assertTrue(TestCodeGen.test(input, "21.5Strue", inspect.stack()[0].function))

    def test_519(self):
        input = """
    func main() {
        var f = true;
        var g boolean;

        putBoolLn(f)
        putBool(g)
    }
     """
        self.assertTrue(TestCodeGen.test(input, "true\nfalse", inspect.stack()[0].function))

    def test_520(self):
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
        self.assertTrue(TestCodeGen.test(input,"3.0\nfalse\nvotien\ntrue\n",inspect.stack()[0].function)) 
    
    def test_521(self):
        input = """
var a float = 3;
func main() {
    putFloatLn(a)
    var a float = 4;
    putFloatLn(a)
    a := 2
    putFloat(a)
}
        """
        self.assertTrue(TestCodeGen.test(input,"3.0\n4.0\n2.0",inspect.stack()[0].function))

    def test_522(self):
        input = """
        func main() {
            var a [2] int = [2] int {10, 20};
            putInt(a[0])
        }
        """
        self.assertTrue(TestCodeGen.test(input,"10",inspect.stack()[0].function))
    
    def test_523(self):
        input = """
func main() {
    var a [1] int ;
    a[0] := 1
    putInt(a[0]);
}
    """
        self.assertTrue(TestCodeGen.test(input,"1",inspect.stack()[0].function))
        
    def test_524(self):
        input = """func main() {
    var a [2][3] int = [2][3] int {{10, 20, 30}, {40, 50, 60}};
    putInt(a[1][0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"40",inspect.stack()[0].function))

    def test_525(self):
        input = """
func main() {
    var a [2][3] int ;
    putInt(a[0][0])
    putInt(a[0][1])
    putInt(a[0][2])
    putInt(a[1][0])
    putInt(a[1][1])
    putInt(a[1][2])
}
"""     
        self.assertTrue(TestCodeGen.test(input,"000000",inspect.stack()[0].function))

    def test_526(self):
        input = """func main() {
    var a [2][3][2] int ;
    putInt(a[0][0][0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"0",inspect.stack()[0].function))

    def test_527(self):
        input = """ func main() {
    var a [2][3] float;
    a[0][0] += 2.0
    putFloat(a[0][0] + a[0][1])
}
"""
        self.assertTrue(TestCodeGen.test(input,"2.0",inspect.stack()[0].function))

    def test_528(self):
        input = """
func main() {
    var a [2][3] boolean;
    a[0][0] := true
    putBool(a[0][0])

}
"""
        self.assertTrue(TestCodeGen.test(input,"true",inspect.stack()[0].function))

    def test_529(self):
        input = """
    var a [2] int;
    func main() {
        a[0] := 100
        a[1] += a[0] + a[0]
        putInt(a[1])
    }
    """
        self.assertTrue(TestCodeGen.test(input,"200",inspect.stack()[0].function))

    def test_530(self):
        input = """ func main() {
        var a = [2][2] int {{1,2}, {3,4}};
        var b = a[0]
        putInt(b[1]);
    }
    """
        self.assertTrue(TestCodeGen.test(input,"2",inspect.stack()[0].function))
    
    def test_531(self):
        input = """func main() {
    if (true) {
        putBool(true)
    } 
}
"""
        self.assertTrue(TestCodeGen.test(input,"true",inspect.stack()[0].function))

    def test_532(self):
        input = """
func main() {
    if (true) {
        putBool(true)
    } else {
        putBool(false)     
    }
}
    """
        self.assertTrue(TestCodeGen.test(input,"true",inspect.stack()[0].function))

    def test_533(self):
        input = """
func main() {
    if (false) {
        putInt(1);
    } else if (false) {
        putInt(2);
    } else {
        putInt(3);
    }
}
        
        """
        self.assertTrue(TestCodeGen.test(input,"3",inspect.stack()[0].function))
    
    def test_534(self):
        input = """
func main() {
    var i = 2;
    for i > 0 {
        putInt(i);
        i -= 1;
    }
    putInt(i);
}
        """
        self.assertTrue(TestCodeGen.test(input,"210",inspect.stack()[0].function))

    def test_535(self):
        input = """
func main() {
    var i int;
    for i := 0; i < 2; i += 1 {
        putInt(i)
    }
    putInt(i)
}
        """
        self.assertTrue(TestCodeGen.test(input,"012",inspect.stack()[0].function))