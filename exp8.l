//Correct LEX Program (exp8.l)
%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[ \t]       { /* ignore spaces */ }
\n          { return 0; }
.           { return yytext[0]; }

%%

int yywrap()
{
    return 1;
}
//Correct YACC Program (exp8.y)
%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(char *s);
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%

E : E '+' E
  | E '-' E
  | E '*' E
  | E '/' E
  | NUMBER
  ;

%%

int main()
{
    printf("Enter Expression:\n");
    yyparse();
    printf("Valid Expression\n");
    return 0;
}

void yyerror(char *s)
{
    printf("Invalid Expression\n");
}
//yacc -d exp8.y
//flex exp8.l
//gcc y.tab.c lex.yy.c -o exp8 -lfl
//./exp8
//input: 10+20*3
