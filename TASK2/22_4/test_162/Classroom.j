.source Classroom.java
.class public  Classroom
.super java.lang.Object
.field public student LHuman;
.field public guest LSpeaker;

.method public <init>(LHuman;LSpeaker;)V
.var 0 is this LClassroom; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
.var 1 is student LHuman; from Label0 to Label1
.var 2 is guest LSpeaker; from Label0 to Label1
Label2:
	aload_0
	aload_1
	putfield Classroom/student LHuman;
	aload_0
	aload_2
	putfield Classroom/guest LSpeaker;
Label3:
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LClassroom; from Label0 to Label1
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
