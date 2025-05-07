.source MiniGoClass.java
.class public  MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is a [[I from Label2 to Label3
	iconst_2
	anewarray [I
	dup
	iconst_0
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	aastore
	dup
	iconst_1
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	aastore
	astore_1
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
	iconst_0
	istore_2
Label6:
	iload_2
	iconst_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
	aload_1
	iload_2
	aaload
	iconst_0
	iaload
	invokestatic io/putInt(I)V
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
Label3:
Label1:
	return
.limit stack 11
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
