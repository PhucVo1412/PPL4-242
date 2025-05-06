.source MiniGoClass.java
.class public  MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a LPPL3; from Label2 to Label3
	new PPL3
	dup
	iconst_1
	invokespecial PPL3/<init>(I)V
	astore_1
.var 2 is b LStudy; from Label2 to Label3
	aload_1
	astore_2
.var 3 is c LPlay; from Label2 to Label3
	aload_1
	astore_3
	aload_2
	invokeinterface Study/study()V 1
	aload_3
	invokeinterface Play/play()V 1
Label3:
Label1:
	return
.limit stack 3
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
