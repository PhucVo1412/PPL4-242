.source Laptop.java
.class public  Laptop
.super java.lang.Object
.field public model Ljava/lang/String;
.field public price F

.method public <init>(Ljava/lang/String;F)V
.var 0 is this LLaptop; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is model Ljava/lang/String; from Label0 to Label1
.var 2 is price F from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Laptop/model Ljava/lang/String;
	aload_0
	fload_2
	putfield Laptop/price F
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LLaptop; from Label0 to Label1
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
