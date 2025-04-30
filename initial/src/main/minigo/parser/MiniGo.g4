//2252650

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}
    



options{
	language=Python3;
}

program  : decls EOF ;

 


primitive_literals: INTEGER_LIT | FLOAT_LIT | STRING_LIT | TRUE | FALSE | NIL | ID;

literal: INTEGER_LIT 
        | FLOAT_LIT 
        | STRING_LIT 
        | TRUE | FALSE
        | NIL
        | array_literals 
        | struct_literals;

types : array_type types
    | INT 
    | STRING 
    | FLOAT 
    | BOOLEAN 
    | ID ; // ten cua struct hoac interface

idlist: ID COMMA idlist | ID;

// ARRAY LITERALS
array_literals: array_type ( INT | STRING | FLOAT | BOOLEAN | ID) LSB element_list RSB;
array_type : LB (INTEGER_LIT|ID) RB array_type | LB (INTEGER_LIT|ID) RB ;

element_list : element COMMA element_list | element;
element: primitive_literals| struct_literals | LSB element_list RSB;




// STRUCT LITERALS
struct_literals: ID LSB struct_attlist RSB;
struct_attlist:  struct_attlist_prime |; 
struct_attlist_prime : ID COLON expression COMMA struct_attlist_prime|  ID COLON expression;


//Function call
func_call: ID LCB list_expression? RCB ;
list_expression:  expression COMMA list_expression| expression ;



//Method call
method_call: dot_operator func_call  ;
dot_operator: (ID | array_access) DOT dot_operator | (ID | array_access) DOT;


// EXPRESSION 
expression: expression OR expression1 | expression1;
expression1: expression1 AND expression2 | expression2;
expression2: expression2 (COM_EQ | COM_GEQ | COM_GT | COM_LEQ | COM_LT | COM_UEQ) expression3 | expression3;
expression3: expression3 (ADD | SUB) expression4 | expression4;
expression4: expression4 (MUL | DIV | MOD) expression5 | expression5;
expression5: NOT expression5 | SUB expression5 | expression6;
expression6: expression6 LB expression RB
    | expression6 DOT ID
    | expression6 DOT ID LCB list_expression? RCB
    | expression7;
expression7: ID LCB expression RCB |LCB expression RCB | ID | literal | func_call  ;



//Array access
array_access : ID array_op;
array_op: LB expression RB array_op | LB expression RB ;


//Struct access
struct_access: struct_access DOT fieldname | fieldname DOT fieldname;
fieldname:  array_access | ID  ;






// DECLARE
decl: funcdecl | vardecl | struct_decl | method_decl | interface_decl  ;
decls: decl decls | decl;

// Varaible
vardecl: VAR ID types? (EQ expression) (SEMI)
      |  VAR ID types  (SEMI)
      |  CONST ID EQ expression  (SEMI);


// Function
funcdecl: FUNC ID LCB (paramlist|paramlist1) RCB types? LSB stmts return_stmt? RSB (SEMI);
paramlist: paramlist_prime | ;
paramlist_prime : ID types COMMA paramlist_prime | ID types;



// STRUCT TYPE
struct_decl :  TYPE ID STRUCT LSB declist RSB (SEMI);
declist:  ID types SEMI declist |  ID types SEMI   ;


//Method declare
method_decl: FUNC LCB ID ID RCB ID LCB (paramlist|paramlist1) RCB types? LSB stmts return_stmt? RSB (SEMI);



//INTERFACE TYPE
interface_decl: TYPE ID INTERFACE LSB decl_list1 RSB (SEMI);
decl_list1: ID LCB paramlist1 RCB types? (SEMI) decl_list1 |  ID LCB paramlist1 RCB types? (SEMI)  ;
paramlist1: paramlist1_prime | ;
paramlist1_prime: idlist types COMMA paramlist1_prime | idlist types;



//STATEMENT
stmts: stmt stmts  | stmt ;


stmt: (assign_stmt | break_stmt| call_stmt| continue_stmt | return_stmt  ) (SEMI)
    | (if_stmt | for_stmt) (SEMI)  
    | vardecl  ;


// Assignment
assign_stmt: variable (ASSIGN | PLUS_EQ | MINUS_EQ | MUL_EQ | MOD_EQ | DIV_EQ ) expression ;
variable: struct_access | array_access | ID  ;



// If statement 
if_stmt: IF (LCB expression RCB) LSB stmts RSB elseif_stmt? else_stmt?;
elseif_stmt: ELSE IF (LCB expression RCB) LSB stmts RSB elseif_stmt? | ELSE IF (LCB expression RCB) LSB stmts RSB ;
else_stmt: ELSE LSB stmts RSB;

// For Statement in MiniGo
for_stmt: FOR condition LSB stmts RSB;
condition: (assign_stmtfor | vardeclfor) SEMI expression? SEMI assign_stmtfor?
        | (ID | UNDER)  COMMA ID ASSIGN RANGE expression
        | expression ;
 
assign_stmtfor : ID (ASSIGN | PLUS_EQ | MINUS_EQ | MUL_EQ | MOD_EQ | DIV_EQ ) expression ;
vardeclfor: VAR ID types? (EQ expression);

// Break Statement
break_stmt: BREAK ;

//Continue Statement
continue_stmt: CONTINUE ;

//Call statement
call_stmt:  func_call 
        | method_call;
 




// Return statement
return_stmt : RETURN expression? ;






//------end Parser-----

//-----------LEXER--------------------



//Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';





//Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';

COM_EQ : '==';
COM_UEQ: '!=';
COM_LT: '<';
COM_LEQ: '<=';
COM_GT: '>';
COM_GEQ: '>=';

AND: '&&';
OR : '||';
NOT: '!';

ASSIGN: ':=' ;
EQ: '=';
PLUS_EQ: '+=' ; 
MINUS_EQ: '-=' ;
MUL_EQ: '*=';
DIV_EQ: '/=';
MOD_EQ: '%=';

DOT: '.';
UNDER: '_';

//Separators
LCB: '(' ;
RCB: ')' ;
LSB: '{' ;
RSB: '}' ;
LB: '[' ;
RB: ']' ;
COMMA: ',';
SEMI: ';' ;
COLON: ':';

//IDENTIFIERS
ID : ([a-zA-Z_]) ([a-zA-Z0-9_])*;

//LITERALS
INTEGER_LIT
    : DECIMAL_LIT 
    | BINARY_LIT 
    | OCTAL_LIT 
    | HEX_LIT  
    ;
fragment DECIMAL_LIT: [1-9][0-9]* | [0];
fragment BINARY_LIT: [0] [bB] [01]+;
fragment OCTAL_LIT: [0][oO][0-7]+ ;
fragment HEX_LIT: [0][xX][0-9a-fA-F]+;

FLOAT_LIT: INTPART '.' FRACPART? EXPPART?;
fragment INTPART: [0-9]+;
fragment FRACPART: [0-9]*;
fragment EXPPART: [eE] [+-]? [0-9]+;

BOOL_LIT: TRUE | FALSE;

STRING_LIT:  '"' (STR_CHAR | ESC_SEQ)* '"'     ;

COMMENT_INLINE: '//' (~[\r\n])* -> skip;

COMMENT_INBLOCK:('/*' (COMMENT_INLINE | COMMENT_NONGREEDY | .)*?  '*/'
               | '/*' (COMMENT_INLINE )*?  '*/' 
               | '/*' (COMMENT_NONGREEDY)*?  '*/'  
               | '/*' (.)*?  '*/' )-> skip;
fragment COMMENT_NONGREEDY: '/*' .*? '*/' ;

fragment STR_CHAR: ~[\r\n"\\];
fragment ESC_SEQ: '\\' [nrt"'\\];
fragment ESC_ILLEGAL:  '\b' |'\f' |'\r' | '\\' ~[nrt"\\];


//SKIP 
WS: [ \t\f\r]+ -> skip; // skip spaces, tabs 
NL:  '\r'? '\n'
{
if (self.preType in [self.ID,
self.INT, self.FLOAT, self.BOOLEAN, self.STRING,
self.INTEGER_LIT, self.FLOAT_LIT, self.TRUE, self.FALSE, self.STRING_LIT,
self.RSB, self.RB, self.RCB, self.RETURN, self.BREAK, self.CONTINUE, self.NIL]):
    self.type = self.SEMI
    self.text = ";"
    return self.emit()
else:
    self.skip()
}
;



//-------------------end Lexer----------------------


ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' (STR_CHAR | ESC_SEQ)* ('\r\n' | '\n' | EOF) {
    if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[:-2])
    elif (self.text[-1] == '\n'):
        raise UncloseString(self.text[:-1])
    else:
        raise UncloseString(self.text)
};
ILLEGAL_ESCAPE:'"' (STR_CHAR | ESC_SEQ)* ESC_ILLEGAL {
    raise IllegalEscape(self.text)
};


