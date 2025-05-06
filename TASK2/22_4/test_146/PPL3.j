.source PPL3.java
.class public  PPL3
.super java.lang.Object
.field public number I
.field public ppl LPPL2;

.method public <init>(ILPPL2;)V
.var 0 is this LPPL3; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is number I from Label0 to Label1
.var 2 is ppl LPPL2; from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield PPL3/number I
	aload_0
	aload_2
	putfield PPL3/ppl LPPL2;
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
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
