%{
#include <stdio.h>

int chars = 0, words = 0, lines = 0, tabs = 0, numbers = 0, spaces = 0, sentences = 0;
%}

%%

[0-9]+        { numbers++; chars += yyleng; }
[a-zA-Z]+     { words++; chars += yyleng; }
" "           { spaces++; chars++; }
\t            { tabs++; chars++; }
\n            { lines++; chars++; }
[.!?]         { sentences++; chars++; }
.             { chars++; }

%%

int main()
{
    printf("Enter text (Press Ctrl+D to stop input):\n");
    yylex();

    printf("\nCharacters : %d\n", chars);
    printf("Words      : %d\n", words);
    printf("Lines      : %d\n", lines);
    printf("Tabs       : %d\n", tabs);
    printf("Numbers    : %d\n", numbers);
    printf("Spaces     : %d\n", spaces);
    printf("Sentences  : %d\n", sentences);

    return 0;
}

int yywrap()
{
    return 1;
}
//save: exp7.l
ptional: cd Desktop/SPCC
sudo apt install flex
lex exp7.l or flex exp7.l
gcc lex.yy.c -o exp7 -lfl
./exp7
if not flex available 
TO RUN CODE:
1. Install tools (only once)
sudo apt update
sudo apt install flex bison gcc

2. yacc -d exp8.y
flex exp8.l
gcc lex.yy.c y.tab.c -o expr -ll
./expr

