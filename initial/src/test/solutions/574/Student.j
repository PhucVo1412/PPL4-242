.source Student.java
.class public  Student
.super java.lang.Object
.field public id I
.field public grade F

.method public <init>(IF)V
.var 0 is this LStudent; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is id I from Label0 to Label1
.var 2 is grade F from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Student/id I
	aload_0
	fload_2
	putfield Student/grade F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LStudent; from Label0 to Label1
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
