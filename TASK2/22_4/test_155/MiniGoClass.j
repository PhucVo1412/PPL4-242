.source MiniGoClass.java
.class public  MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is c LCalculator; from Label2 to Label3
	new BasicCalc
	dup
	iconst_5
	bipush 15
	invokespecial BasicCalc/<init>(II)V
	astore_1
.var 2 is result I from Label2 to Label3
	aload_1
	invokeinterface Calculator/sum()I 1
	istore_2
	iload_2
	invokestatic io/putIntLn(I)V
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
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
