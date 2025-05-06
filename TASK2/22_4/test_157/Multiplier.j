.source Multiplier.java
.class public  Multiplier
.super java.lang.Object
.field public factor I

.method public <init>(I)V
.var 0 is this LMultiplier; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is factor I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Multiplier/factor I
Label3:
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMultiplier; from Label0 to Label1
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

.method public multiply(I)I
.var 0 is this LMultiplier; from Label0 to Label1
Label0:
.var 1 is value I from Label0 to Label1
Label2:
	aload_0
	getfield Multiplier/factor I
	iload_1
	imul
	ireturn
Label3:
Label1:
.limit stack 2
.limit locals 2
.end method
