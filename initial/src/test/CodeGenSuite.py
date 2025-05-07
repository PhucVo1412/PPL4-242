import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_501(self):
        input = """func main() {putInt(5);};"""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,501))
    def test_502(self):
        input = """func main() {var a int = 20;  putInt(a);};"""
        expect = "20"
        self.assertTrue(TestCodeGen.test(input,expect,502))
    def test_503(self):
        input = """var a int = 10; func main() { putInt(a);};"""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_504(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([FuncCall("putInt", [IntLiteral(25)])]))])
        expect = "25"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_505(self):
        input = Program([FuncDecl("main",[],VoidType(),Block([VarDecl("a",IntType(),IntLiteral(500)),FuncCall("putInt", [Id("a")])]))])
        expect = "500"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_506(self):  
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
        func foo(a int , c int) {
            var b int = a + c;
            putInt(b);
        };
        func main() {
            foo(2, 3);
            }
        """
        self.assertTrue(TestCodeGen.test(input, "5", 509)) 

    def test_510(self):
        input = """
        func main() {
            var a float = 3.0;
            putFloat(1 + a)
        }
         """
        self.assertTrue(TestCodeGen.test(input,"4.0",510)) 

    def test_511(self):
        input = """
        func main() {
            var a int = 3;
            var b int = 4;
            putInt(a + b)
        }
         """
        self.assertTrue(TestCodeGen.test(input,"7",511))
    
    def test_512(self):
        input = """
        func main() {
            var a int = 3;
            var b int = 4;
            putInt(a - b)
        }
         """
        self.assertTrue(TestCodeGen.test(input,"-1",512))

    def test_513(self):
        input = """
        func main() {
            var a1 int = 5;
            var a2 int = 7;
            putInt(a1 * a2)
        }
         """
        self.assertTrue(TestCodeGen.test(input,"35",513))

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

    def test_517(self):
        input = """
        func main() {
        var a int = 10;
        var b int = 20;
        putInt(a + b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30", 517))

    def test_518(self):
        input = """
        func main() {
        var a float = 5.5;
        var b float = 2.5;
        putFloat(a - b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.0", 518))

    def test_519(self):
        input = """
        func main() {
        var a int = 6;
        var b int = 3;
        putInt(a / b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2", 519))

    def test_520(self):
        input = """
        func main() {
        var a int = 5;
        var b int = 3;
        putInt(a % b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2", 520))

    def test_521(self):
        input = """
        func main() {
        var a boolean = true;
        var b boolean = false;
        if (a && b) {
            putString("Both True")
        } else {
            putString("Not Both True")
        }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Not Both True", 521))

    def test_522(self):
        input = """
        func main() {
        var a boolean = true;
        var b boolean = false;
        if (a || b) {
            putString("At Least One True")
        } else {
            putString("None True")
        }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "At Least One True", 522))

    def test_523(self):
        input = """
        func main() {
        var a int = 5;
        var b int = 10;
        if (a < b) {
            putString("a is less than b")
        } else {
            putString("a is not less than b")
        }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "a is less than b", 523))

    def test_524(self):
        input = """
        func main() {
        var a int = 10;
        var b int = 10;
        if (a == b) {
            putString("a is equal to b")
        } else {
            putString("a is not equal to b")
        }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "a is equal to b", 524))

    def test_525(self):
        input = """
        func main() {
        var a int = 15;
        var b int = 10;
        if (a > b) {
            putString("a is greater than b")
        } else {
            putString("a is not greater than b")
        }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "a is greater than b", 525))

    def test_526(self):
        input = """
func main() {
    var i int;
    for i := 0; i < 2; i += 1 {
        putInt(i)
    }
    putInt(i)
}
        """
        self.assertTrue(TestCodeGen.test(input,"012",526))
         
    def test_527(self):
        input = """
        func main() {
            var i int;
            for i := 0; i < 5; i += 1 {
                putInt(i)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "01234", 527))

    def test_528(self):
        input = """
        func main() {
            var i int;
            for i := 5; i > 0; i -= 1 {
                putInt(i)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "54321", 528))

    def test_529(self):
        input = """
        func main() {
            var i int;
            for i := 0; i <= 3; i += 1 {
                putInt(i * 2)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "0246", 529))

    def test_530(self):
        input = """
        func main() {
            var i int;
            for i := 1; i < 4; i += 1 {
                if (i % 2 == 0) {
                    putString("Even")
                } else {
                    putString("Odd")
                }
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "OddEvenOdd", 530))

    def test_531(self):
        input = """
        func main() {
            var i int;
            for i := 0; i < 3; i += 1 {
                var j int;
                for j := 0; j < 2; j += 1 {
                    putInt(i + j)
                }
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "011223", 531))

    def test_532(self):
        input = """
        func main() {
            var i int;
            for i := 0; i < 4; i += 1 {
                if (i == 2) {
                    continue;
                }
                putInt(i)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "013", 532))

    def test_533(self):
        input = """
        func main() {
            var i int;
            for i := 0; i < 4; i += 1 {
                if (i == 2) {
                    break;
                }
                putInt(i)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "01", 533))

    def test_534(self):
        input = """
        func main() {
            var i int;
            var sum int = 0;
            for i := 1; i <= 5; i += 1 {
                sum +=  i;
            }
            putInt(sum)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15", 534))

    def test_535(self):
        input = """
        func main() {
            var i int;
            for i := 10; i >= 0; i -= 2 {
                putInt(i)
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1086420", 535))

    def test_536(self):
        input = """
        func main() {
            var i int;
            for i := 0; i < 3; i += 1 {
                putString("Loop")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "LoopLoopLoop", 536))

    def test_537(self):
        input = """func main() {
    var a [2][3] int = [2][3] int {{10, 20, 30}, {40, 50, 60}};
    putInt(a[1][0])
}
"""
        self.assertTrue(TestCodeGen.test(input,"40",537))
    
    def test_538(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            putInt(a[0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1", 538))

    def test_539(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            putInt(a[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3", 539))

    def test_540(self):
        input = """
        func main() {
            var a [3] float = [3] float {1.1, 2.2, 3.3};
            putFloat(a[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2.2", 540))

    def test_541(self):
        input = """
        func main() {
            var a [2][2] int = [2][2] int {{1, 2}, {3, 4}};
            putInt(a[1][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4", 541))

    def test_542(self):
        input = """
        func main() {
            var a [2][3] int = [2][3] int {{10, 20, 30}, {40, 50, 60}};
            putInt(a[0][2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30", 542))

    def test_543(self):
        input = """
        func main() {
            var a [3] float = [3] string {1.0, 2.0, 3.0};
            putFloat(a[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2.0", 543))

    def test_544(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            a[1] := 10;
            putInt(a[1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", 544))

    def test_545(self):
        input = """
        func main() {
            var a [2][2] float = [2][2] float {{1.1, 2.2}, {3.3, 4.4}};
            putFloat(a[0][0] + a[1][1])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5.5", 545))

    def test_546(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            var sum int = 0;
            var i int;
            for i := 0; i < 3; i += 1 {
                sum +=  a[i];
            }
            putInt(sum)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6", 546))

    def test_547(self):
        input = """
        func main() {
            var a [2][3] int = [2][3] int {{1, 2, 3}, {4, 5, 6}};
            var i int;
            for i := 0; i < 2; i += 1 {
                putInt(a[i][0])
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "14", 547))

    def test_548(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            if (a < b) {
                putString("a is less")
            } else {
                putString("a is not less")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "a is less", 548))

    def test_549(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            putInt(a[1] + a[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5", 549))

    def test_550(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            var c int = a + b;
            putInt(c)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30", 550))

    def test_551(self):
        input = """
        func main() {
            var a [2][2] int = [2][2] int {{1, 2}, {3, 4}};
            if (a[0][1] == 2) {
                putString("Correct")
            } else {
                putString("Incorrect")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Correct", 551))

    def test_552(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            var i int;
            for i := 0; i < 3; i += 1 {
                putInt(a[i])
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "123", 552))

    def test_553(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 3;
            putInt(a * b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15", 553))

    def test_554(self):
        input = """
        func main() {
            var a float = 5.5;
            var b float = 2.5;
            putFloat(a / b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "2.2", 554))

    def test_555(self):
        input = """
        func main() {
            var a [2][3] int = [2][3] int {{1, 2, 3}, {4, 5, 6}};
            putInt(a[1][2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6", 555))

    def test_556(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            if (a + b == 30) {
                putString("Sum is 30")
            } else {
                putString("Sum is not 30")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Sum is 30", 556))

    def test_557(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            a[2] := 10;
            putInt(a[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", 557))

    def test_558(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            if (a > b) {
                putString("a is greater")
            } else {
                putString("b is greater")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "b is greater", 558))

    def test_559(self):
        input = """
        func main() {
            var a [2][2] float = [2][2] float {{1.1, 2.2}, {3.3, 4.4}};
            putFloat(a[0][1] + a[1][0])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5.5", 559))

    def test_560(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 5;
            putInt(a - b)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5", 560))

    def test_561(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            var sum int = 0;
            var i int;
            for i := 0; i < 3; i += 1 {
                sum += a[i];
            }
            putInt(sum)
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6", 561))

    def test_562(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            if (a * b == 50) {
                putString("Product is 50")
            } else {
                putString("Product is not 50")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Product is 50", 562))

    def test_563(self):
        input = """
        func main() {
            var a [2][2] int = [2][2] int {{1, 2}, {3, 4}};
            var i int;
            var j int;
            for i := 0; i < 2; i += 1 {
                for j := 0; j < 2; j += 1 {
                    putInt(a[i][j])
                }
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1234", 563))

    def test_564(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            if (a + b > 25) {
                putString("Greater than 25")
            } else {
                putString("Not greater than 25")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Greater than 25", 564))

    def test_565(self):
        input = """
        func main() {
            var a [3] float = [3] float {1.1, 2.2, 3.3};
            putFloat(a[0] + a[2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4.4", 565))

    def test_566(self):
        input = """
        func main() {
            var a int = 15;
            var b int = 10;
            if (a % b == 5) {
                putString("Remainder is 5")
            } else {
                putString("Remainder is not 5")
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Remainder is 5", 566))

    def test_567(self):
        input = """
        func main() {
            var a [2][3] int = [2][3] int {{1, 2, 3}, {4, 5, 6}};
            putInt(a[1][1] * a[0][2])
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15", 567))       

    def test_568(self):
        input = """
        type PPL3 struct {
            number int;
        }

        func main(){
            var a PPL3 = PPL3{number : 10};
            putInt(a.number);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "10", 568))

    def test_569(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func main() {
            var p Person = Person{name: "Alice", age: 25};
            putString(p.name);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Alice", 569))

    def test_570(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func main() {
            var p Person = Person{name: "Bob", age: 30};
            putInt(p.age);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30", 570))

    def test_571(self):
        input = """
        type Rectangle struct {
            width int;
            height int;
        }

        func main() {
            var r Rectangle = Rectangle{width: 5, height: 10};
            putInt(r.width * r.height);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "50", 571))

    def test_572(self):
        input = """
        type Circle struct {
            radius float;
        }

        func main() {
            var c Circle = Circle{radius: 3.5};
            putFloat(c.radius * c.radius * 3.14);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "38.465", 572))

    def test_573(self):
        input = """
        type Point struct {
            x int;
            y int;
        }

        func main() {
            var p Point = Point{x: 3, y: 4};
            putInt(p.x + p.y);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "7", 573))

    def test_574(self):
        input = """
        type Student struct {
            id int;
            grade float;
        }

        func main() {
            var s Student = Student{id: 101, grade: 95.5};
            putFloat(s.grade);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "95.5", 574))

    def test_575(self):
        input = """
        type Book struct {
            title string;
            pages int;
        }

        func main() {
            var b Book = Book{title: "PPL", pages: 300};
            putString(b.title);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "PPL", 575))

    def test_576(self):
        input = """
        type Employee struct {
            name string;
            salary int;
        }

        func main() {
            var e Employee = Employee{name: "John", salary: 5000};
            putInt(e.salary);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5000", 576))

    def test_577(self):
        input = """
        type Car struct {
            brand string;
            year int;
        }

        func main() {
            var c Car = Car{brand: "Toyota", year: 2020};
            putString(c.brand);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Toyota", 577))

    def test_578(self):
        input = """
        type Laptop struct {
            model string;
            price float;
        }

        func main() {
            var l Laptop = Laptop{model: "Dell", price: 999.99};
            putFloat(l.price);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "999.99", 578))

    def test_579(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            var b [3] int = [3] int {4, 5, 6};
            putInt(a[0] + b[2]);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "7", 579))

    def test_580(self):
        input = """
        func main() {
            var a [2][2] int = [2][2] int {{1, 2}, {3, 4}};
            var sum int = a[0][0] + a[1][1];
            putInt(sum);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5", 580))

    def test_581(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            if (a < b) {
                putString("a is less");
            } else {
                putString("a is not less");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "a is less", 581))

    def test_582(self):
        input = """
        func main() {
            var a [3] float = [3] float {1.0, 2.0, 3.3};
            putFloat(a[0] + a[1]);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "3.0", 582))

    def test_583(self):
        input = """
        type Person struct {
            name string;
            age int;
        }

        func main() {
            var p Person = Person{name: "Alice", age: 25};
            putString(p.name);
            putInt(p.age);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Alice25", 583))

    def test_584(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            var c int = a + b;
            putInt(c);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30", 584))

    def test_585(self):
        input = """
        func main() {
            var a [2][2] int = [2][2] int {{1, 2}, {3, 4}};
            var i int;
            var j int;
            for i := 0; i < 2; i += 1 {
                for j := 0; j < 2; j += 1 {
                    putInt(a[i][j]);
                }
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "1234", 585))

    def test_586(self):
        input = """
        func main() {
            var a int = 15;
            var b int = 10;
            if (a % b == 5) {
                putString("Remainder is 5");
            } else {
                putString("Remainder is not 5");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Remainder is 5", 586))

    def test_587(self):
        input = """
        func main() {
            var a [2][3] int = [2][3] int {{1, 2, 3}, {4, 5, 6}};
            putInt(a[1][1] * a[0][2]);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "15", 587))

    def test_588(self):
        input = """
        type Rectangle struct {
            width int;
            height int;
        }

        func main() {
            var r Rectangle = Rectangle{width: 5, height: 10};
            putInt(r.width * r.height);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "50", 588))

    def test_589(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            var sum int = 0;
            var i int;
            for i := 0; i < 3; i += 1 {
                sum += a[i];
            }
            putInt(sum);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "6", 589))

    def test_590(self):
        input = """
        func main() {
            var a int = 5;
            var b int = 10;
            if (a * b == 50) {
                putString("Product is 50");
            } else {
                putString("Product is not 50");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Product is 50", 590))

    def test_591(self):
        input = """
        func main() {
            var a [2][2] float = [2][2] float {{1.1, 2.2}, {3.3, 4.4}};
            putFloat(a[0][1] + a[1][0]);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "5.5", 591))

    def test_592(self):
        input = """
        type Circle struct {
            radius float;
        }

        func main() {
            var c Circle = Circle{radius: 3.5};
            putFloat(c.radius * c.radius * 3.14);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "38.465", 592))

    def test_593(self):
        input = """
        func main() {
            var a [3] int = [3] int {1, 2, 3};
            var b [3] int = [3] int {4, 5, 6};
            var i int;
            for i := 0; i < 3; i += 1 {
                putInt(a[i] + b[i]);
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "579", 593))

    def test_594(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            if (a + b > 25) {
                putString("Greater than 25");
            } else {
                putString("Not greater than 25");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Greater than 25", 594))

    def test_595(self):
        input = """
        func main() {
            var a [3] float = [3] float {1.1, 2.2, 3.3};
            putFloat(a[0] + a[2]);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "4.4", 595))

    def test_596(self):
        input = """
        type Student struct {
            id int;
            grade float;
        }

        func main() {
            var s Student = Student{id: 101, grade: 95.5};
            putFloat(s.grade);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "95.5", 596))

    def test_597(self):
        input = """
        func main() {
            var a [2][3] int = [2][3] int {{1, 2, 3}, {4, 5, 6}};
            var i int;
            for i := 0; i < 2; i += 1 {
                putInt(a[i][0]);
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "14", 597))

    def test_598(self):
        input = """
        func main() {
            var a int = 10;
            var b int = 20;
            var c int = a + b;
            putInt(c);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "30", 598))

    def test_599(self):
        input = """
        func main() {
            var a [2][2] int = [2][2] int {{1, 2}, {3, 4}};
            if (a[0][1] == 2) {
                putString("Correct");
            } else {
                putString("Incorrect");
            }
        }
        """
        self.assertTrue(TestCodeGen.test(input, "Correct", 599))

    def test_600(self):
        input = """
        type Laptop struct {
            model string;
            price float;
        }

        func main() {
            var l Laptop = Laptop{model: "Dell", price: 999.99};
            putFloat(l.price);
        }
        """
        self.assertTrue(TestCodeGen.test(input, "999.99", 600))