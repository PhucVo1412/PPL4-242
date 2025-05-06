.source MiniGoClass.java
.class public  MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is h LHuman; from Label2 to Label3
	new Human
	dup
	sipush 777
	invokespecial Human/<init>(I)V
	astore_1
.var 2 is k LSpeaker; from Label2 to Label3
	new Human
	dup
	sipush 999
	invokespecial Human/<init>(I)V
	astore_2
.var 3 is room LClassroom; from Label2 to Label3
	new Classroom
	dup
	aload_1
	aload_2
	invokespecial Classroom/<init>(LHuman;LSpeaker;)V
	astore_3
	aload_3
	getfield Classroom/student LHuman;
	getfield Human/name I
	invokestatic io/putIntLn(I)V
	aload_3
	getfield Classroom/guest LSpeaker;
	invokeinterface Speaker/speak()V 1
Label3:
Label1:
	return
.limit stack 4
.limit locals 4
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
