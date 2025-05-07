.source Car.java
.class public  Car
.super java.lang.Object
.field public brand Ljava/lang/String;
.field public year I

.method public <init>(Ljava/lang/String;I)V
.var 0 is this LCar; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is brand Ljava/lang/String; from Label0 to Label1
.var 2 is year I from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Car/brand Ljava/lang/String;
	aload_0
	iload_2
	putfield Car/year I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LCar; from Label0 to Label1
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
