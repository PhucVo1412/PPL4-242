.source Rectangle.java
.class public  Rectangle
.super java.lang.Object
.field public width I
.field public height I

.method public <init>(II)V
.var 0 is this LRectangle; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is width I from Label0 to Label1
.var 2 is height I from Label0 to Label1
Label2:
	aload_0
	iload_1
	putfield Rectangle/width I
	aload_0
	iload_2
	putfield Rectangle/height I
Label3:
Label1:
	return
.limit stack 4
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LRectangle; from Label0 to Label1
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
