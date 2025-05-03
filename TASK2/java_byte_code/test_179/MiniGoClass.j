.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static binarySearch([IIII)I
Label0:
.var 0 is arr [I from Label0 to Label1
.var 1 is low I from Label0 to Label1
.var 2 is high I from Label0 to Label1
.var 3 is target I from Label0 to Label1
Label2:
	iload_1
	iload_2
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label7:
	iconst_1
	ineg
	ireturn
	return
Label8:
Label6:
LabelNone:
.var 4 is mid I from Label2 to Label3
	iload_1
	iload_2
	iload_1
	isub
	iconst_2
	idiv
	iadd
	istore 4
	aload_0
	iload 4
	iaload
	iload_3
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
Label12:
	iload 4
	ireturn
	return
Label13:
Label11:
LabelNone:
	aload_0
	iload 4
	iaload
	iload_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label18:
	aload_0
	iload 4
	iconst_1
	iadd
	iload_2
	iload_3
	invokestatic MiniGoClass/binarySearch([IIII)I
	ireturn
	return
Label19:
	goto Label17
Label16:
Label20:
	aload_0
	iload_1
	iload 4
	iconst_1
	isub
	iload_3
	invokestatic MiniGoClass/binarySearch([IIII)I
	ireturn
	return
Label21:
Label17:
Label3:
Label1:
.limit stack 14
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is arr [I from Label2 to Label3
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	dup
	iconst_4
	iconst_4
	iastore
	dup
	iconst_5
	iconst_5
	iastore
	dup
	bipush 6
	bipush 6
	iastore
	dup
	bipush 7
	bipush 7
	iastore
	dup
	bipush 8
	bipush 8
	iastore
	dup
	bipush 9
	bipush 9
	iastore
	astore_1
.var 2 is result I from Label2 to Label3
	aload_1
	iconst_0
	bipush 9
	iconst_5
	invokestatic MiniGoClass/binarySearch([IIII)I
	istore_2
	iload_2
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 5
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
