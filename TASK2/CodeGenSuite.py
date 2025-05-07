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

    def test_536(self):
        input = """
        func main() {
            var i int = 10;
            for var i int = 0; i < 2; i += 1 {
                putIntLn(i)
            }
            putInt(i)
        }
        """
        self.assertTrue(TestCodeGen.test(input,"0\n1\n10",inspect.stack()[0].function))

    def test_537(self):
        input = """
        const a = "votien"
func main() {
    putString(a)
}
"""
        self.assertTrue(TestCodeGen.test(input,"votien",inspect.stack()[0].function))

    def test_538(self):
        input = """
const a = 2
func main() {
    var b [a] int;
    putInt(b[0]);
    b[0] := 20;
    putInt(b[0]);
}
        """
        self.assertTrue(TestCodeGen.test(input,"020",inspect.stack()[0].function))

    def test_539(self):
        input = """
const a = 1 + 1
const c = 5 - a
func main() {
    var b [a][c] int;
    putInt(b[0][0]);
    b[0][0] := 20;
    putInt(b[0][0]);
}
        """
        self.assertTrue(TestCodeGen.test(input,"020",inspect.stack()[0].function))

    def test_540(self):
        input = """
const a = [2] int {2,3}
func main() {
    var b [a[0]][a[1]] int;
    putInt(b[0][0]);
    b[0][0] := 20;
    putInt(b[0][0]);
}
        """
        self.assertTrue(TestCodeGen.test(input,"020",inspect.stack()[0].function))

    def test_541(self):
        input = """
        const MAX = 5;
        
        func bfs(graph [MAX][MAX]int, start int){
            var visited [MAX] boolean;
            var queue [MAX] int;
            var front = 0;
            var rear = 0;
            visited[start] := true;
            queue[rear] := start;
            rear += 1;
            
            for front < rear {
                var u = queue[front]
                front += 1;
                putInt(u)
                putString(" ")
                for v := 0; v < MAX; v += 1{
                    if (graph[u][v] == 1 && !visited[v]){
                        visited[v] := true;
                        queue[rear] := v;
                        rear += 1;
                    }
                }   
            }
        }
        
        func main(){
            var graph = [MAX][MAX] int {{0, 1, 0, 0, 0}, {1, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 0, 1, 0, 1}, {0, 0, 0, 1, 0}};
            bfs(graph, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0 1 2 3 4 ", inspect.stack()[0].function))

    def test_542(self):
        input = """
        const MAX = 10;
        
        func generateBinary(arr [MAX]int, n int, index int){
            if (index == n) {
                for i := 0; i < n; i += 1 {
                    putInt(arr[i]);
                }
                putLn();
            } else {
                arr[index] := 0;
                generateBinary(arr, n, index + 1);
                arr[index] := 1;
                generateBinary(arr, n, index + 1);
            }
        }
        
        func main() {
            var n = 3;
            var arr [MAX] int;
            putString("All binary strings of length = ")
            putInt(n)
            putLn()
            generateBinary(arr, n, 0);
        }
        """
        self.assertTrue(TestCodeGen.test(input, """All binary strings of length = 3
000
001
010
011
100
101
110
111
""", inspect.stack()[0].function))
        
        def test_543(self):
            input = """func Phuc() {putStringLn("Phuc");}

        var gl = int1()
        func main() {
            Phuc();
            putFloatLn(global + 2.0)

            var local1 = "a";
            putBoolLn(local <= "b")
            local1 += "c"
            putStringLn(local1)

        };

         func int1() int {return 1;}
         """
            self.assertTrue(TestCodeGen.test(input,"Phuc\n3.0\ntrue\nac\n",inspect.stack()[0].function))

    def test_544(self):
        input = """
        
        type Course interface {study();}
        type PPL3 struct {number int;}
        func (p PPL3) study() {putInt(p.number);}

        func main(){
            var a PPL3 = PPL3 {number: 10}
            putIntLn(a.number)
            a.study()
        }
        
        """
        self.assertTrue(TestCodeGen.test(input,"10\n10",inspect.stack()[0].function))
    

    def test_545(self):
        input = """
type Course interface {study();}
type PPL3 struct {number int;}
func (p PPL3) study() {putInt(p.number);}

func main(){
    var a Course = nil
    a := PPL3 {number: 10}
    a.study()
}
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))

    def test_546(self):
        input = """
type PPL3 struct {number int;}

func main(){
    var a PPL3
    a.number := 10
    putInt(a.number)
}
        """
        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))
    
    def test_599(self):
        input = """func main() {
            var a [3] int = [3] int {1, 2, 3};
            a[1] = 10;
            putInt(a[1])
        
        }
        """

        self.assertTrue(TestCodeGen.test(input, "10", inspect.stack()[0].function))
