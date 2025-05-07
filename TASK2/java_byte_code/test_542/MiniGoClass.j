.source MiniGoClass.java
.class public  MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static generateBinary([III)V
Label0:
.var 0 is arr [I from Label0 to Label1
.var 1 is n I from Label0 to Label1
.var 2 is index I from Label0 to Label1
Label2:
	iload_2
	iload_1
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label6
Label8:
.var 3 is i I from Label8 to Label9
	iconst_0
	istore_3
Label12:
	iload_3
	iload_1
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	aload_0
	iload_3
	iaload
	invokestatic io/putInt(I)V
Label16:
Label10:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label12
Label11:
	invokestatic io/putLn()V
Label9:
	goto Label7
Label6:
Label17:
	aload_0
	iload_2
	iconst_0
	iastore
	aload_0
	iload_1
	iload_2
	iconst_1
	iadd
	invokestatic MiniGoClass/generateBinary([III)V
	aload_0
	iload_2
	iconst_1
	iastore
	aload_0
	iload_1
	iload_2
	iconst_1
	iadd
	invokestatic MiniGoClass/generateBinary([III)V
Label18:
Label7:
Label3:
Label1:
	return
.limit stack 12
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is n I from Label2 to Label3
	iconst_3
	istore_1
.var 2 is arr [I from Label2 to Label3
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	dup
	iconst_5
	iconst_0
	iastore
	dup
	bipush 6
	iconst_0
	iastore
	dup
	bipush 7
	iconst_0
	iastore
	dup
	bipush 8
	iconst_0
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	astore_2
	ldc "All binary strings of length = "
	invokestatic io/putString(Ljava/lang/String;)V
	iload_1
	invokestatic io/putInt(I)V
	invokestatic io/putLn()V
	aload_2
	iload_1
	iconst_0
	invokestatic MiniGoClass/generateBinary([III)V
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
	bipush 10
	putstatic MiniGoClass/MAX I
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
