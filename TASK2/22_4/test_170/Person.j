.source Person.java
.class public  Person
.super java.lang.Object
.field public name Ljava/lang/String;
.field public age I

.method public <init>(Ljava/lang/String;I)V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is name Ljava/lang/String; from Label0 to Label1
.var 2 is age I from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Person/name Ljava/lang/String;
	aload_0
	iload_2
	putfield Person/age I
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
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

.method public isAdult()Z
.var 0 is this LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Person/age I
	bipush 18
	if_icmplt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 1
.end method
