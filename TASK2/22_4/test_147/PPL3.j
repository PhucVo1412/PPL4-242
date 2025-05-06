.source PPL3.java
.class public  PPL3
.super java.lang.Object
.implements Study
.implements Play
.field public number I

.method public <init>(I)V
.var 0 is this LPPL3; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is number I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield PPL3/number I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LPPL3; from Label0 to Label1
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

.method public study()V
.var 0 is this LPPL3; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield PPL3/number I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public play()V
.var 0 is this LPPL3; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield PPL3/number I
	iconst_5
	iadd
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method
