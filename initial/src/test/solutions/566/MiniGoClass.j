.source MiniGoClass.java
.class public  MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a I from Label2 to Label3
	bipush 15
	istore_1
.var 2 is b I from Label2 to Label3
	bipush 10
	istore_2
	iload_1
	iload_2
	irem
	iconst_5
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
	ldc "Remainder is 5"
	invokestatic io/putString(Ljava/lang/String;)V
Label9:
	goto Label7
Label6:
Label10:
	ldc "Remainder is not 5"
	invokestatic io/putString(Ljava/lang/String;)V
Label11:
Label7:
Label3:
Label1:
	return
.limit stack 3
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
