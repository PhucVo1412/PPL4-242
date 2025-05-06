.source Human.java
.class public  Human
.super java.lang.Object
.implements Speaker
.field public name I

.method public <init>(I)V
.var 0 is this LHuman; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is name I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Human/name I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LHuman; from Label0 to Label1
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

.method public speak()V
.var 0 is this LHuman; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Human/name I
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 1
.end method
