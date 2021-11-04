/*grammar compilador;

fragment LETRA: [a-zA-Z];
fragment DIGITO: [0-9];

PA: '(';  
PC: ')';

PALABRA: (LETRA)+;
NUM_ENTERO: (DIGITO)+;

WS: [ \t\n\r]->skip;

si: s EOF;

s: PA s PC s
  |
  ;

*/

grammar compilador;

fragment LETRA: [a-zA-Z];
fragment DIGITO: [0-9];
fragment MAS: '+';
fragment MENOS: '-';
fragment IGUAL: '=';
fragment MULT_DIV: [*/];


PALABRA: (LETRA)+;
NUM_ENTERO: (DIGITO)+;
SUMA: (NUM_ENTERO)MAS(NUM_ENTERO)IGUAL(NUM_ENTERO);
RESTA: (NUM_ENTERO)MENOS(NUM_ENTERO)IGUAL(NUM_ENTERO);
GENERIC_OP: (NUM_ENTERO)MULT_DIV(NUM_ENTERO)IGUAL(NUM_ENTERO);

WS: [ \t\n\r]->skip;

s: PALABRA {print("PALABRAA -> "+$PALABRA.text+"  "+str($PALABRA))} s | 
   NUM_ENTERO {print("NUMERO -> "+$NUM_ENTERO.text+"  "+str($NUM_ENTERO))} s | 
   SUMA {print("SUMA ->"+$SUMA.text)} s |
   RESTA {print("RESTA ->"+$RESTA.text)} s |
   GENERIC_OP {print("MULT o DIV ->"+$GENERIC_OP.text)} s |
   EOF;
 