.source MiniGoClass.java
.class public  MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is people [LPerson; from Label2 to Label3
	iconst_1
	multianewarray [LPerson; 1
	astore_1
	aload_1
	iconst_0
	new Person
	dup
	ldc "Anna"
	bipush 19
	invokespecial Person/<init>(Ljava/lang/String;I)V
	aastore
	new Person
	dup
	ldc "Anna"
	bipush 19
	invokespecial Person/<init>(Ljava/lang/String;I)V
	aload_1
	iconst_0
	aload_1
	iconst_0
	aaload
	invokevirtual Person/printInfo()V
Label3:
Label1:
	return
.limit stack 6
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
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
