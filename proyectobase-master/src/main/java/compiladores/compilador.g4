grammar compilador;

@header {
package compiladores;
}

LETRA : [A-Za-z] ;
DIGITO : [0-9] ;

WS : [ \t\n\r] -> skip ;


s : LETRA s
  | DIGITO s
  | EOF
  ;
