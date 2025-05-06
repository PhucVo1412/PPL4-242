.source BasicCalc.java
.class public  BasicCalc
.super java.lang.Object
.implements Calculator
.field public number I

.method public <init>(I)V
.var 0 is this LBasicCalc; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is number I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield BasicCalc/number I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LBasicCalc; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label2:
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public calculate(II)I
.var 0 is this LBasicCalc; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label2:
	iload_1
	iload_2
	iadd
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 3
.end method
