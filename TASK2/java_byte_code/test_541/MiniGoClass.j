.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static MAX I

.method public static bfs([[II)V
Label0:
.var 0 is graph [[I from Label0 to Label1
.var 1 is start I from Label0 to Label1
Label2:
.var 2 is visited [Z from Label2 to Label3
	iconst_5
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_0
	bastore
	dup
	iconst_3
	iconst_0
	bastore
	dup
	iconst_4
	iconst_0
	bastore
	astore_2
.var 3 is queue [I from Label2 to Label3
	iconst_5
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
	astore_3
.var 4 is front I from Label2 to Label3
	iconst_0
	istore 4
.var 5 is rear I from Label2 to Label3
	iconst_0
	istore 5
	aload_2
	iload_1
	iconst_1
	bastore
	aload_3
	iload 5
	iload_1
	iastore
	iload 5
	iconst_1
	iadd
	istore 5
Label4:
	iload 4
	iload 5
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
Label9:
.var 6 is u I from Label9 to Label10
	aload_3
	iload 4
	iaload
	istore 6
	iload 4
	iconst_1
	iadd
	istore 4
	iload 6
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
.var 7 is v I from Label9 to Label10
	iconst_0
	istore 7
Label13:
	iload 7
	getstatic MiniGoClass/MAX I
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
Label16:
	aload_0
	iload 6
	aaload
	iload 7
	iaload
	iconst_1
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	aload_2
	iload 7
	baload
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	iand
	ifle Label22
Label23:
	aload_2
	iload 7
	iconst_1
	bastore
	aload_3
	iload 5
	iload 7
	iastore
	iload 5
	iconst_1
	iadd
	istore 5
Label24:
Label22:
LabelNone:
Label17:
Label11:
	iload 7
	iconst_1
	iadd
	istore 7
	goto Label13
Label12:
Label10:
	goto Label4
Label6:
Label5:
Label3:
Label1:
	return
.limit stack 28
.limit locals 8
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is graph [[I from Label2 to Label3
	iconst_5
	anewarray [I
	dup
	iconst_0
	iconst_5
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
	aastore
	dup
	iconst_1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_1
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	aastore
	dup
	iconst_2
	iconst_5
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
	iconst_0
	iastore
	dup
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	aastore
	dup
	iconst_3
	iconst_5
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
	iconst_1
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_1
	iastore
	aastore
	dup
	iconst_4
	iconst_5
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
	iconst_1
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	aastore
	astore_1
	aload_1
	iconst_0
	invokestatic MiniGoClass/bfs([[II)V
Label3:
Label1:
	return
.limit stack 14
.limit locals 2
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
	iconst_5
	putstatic MiniGoClass/MAX I
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
