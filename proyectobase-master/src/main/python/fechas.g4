grammar fechas;

fragment SEPARACION: '/';
fragment DOS_PUNTOS: ':';
fragment ESPACIO: ' ';
fragment DIAS: ('0'[1-9]) | ([12][0-9]) | ('3'[01]);
fragment MESES: ('0'[1-9]) | ('1'[0-2]);
fragment ANIOS: ([0-9][0-9][0-9][0-9]);
fragment HORA: ([01][0-9] | '2'[0-3]);     // 00 - 23
fragment MINUTO: ([0-5][0-9]);
fragment HORA_COMPLETA: HORA DOS_PUNTOS MINUTO;
fragment ID_BUSCADO: [A-Z] ([a-z]|[A-Z])+;
fragment ID: ([a-z]|[A-Z])+;

fragment DIAS_DAD: ('1'[0-9]);
fragment MESES_PARES: ('0'[2468]) | ('1'[02]);
fragment ANIOS_RANGO: ('199'[89]) | ('200'[0-8]);   // 1998 - 2008
fragment HORA_BUSCADA: ('10:'[3-5][0-9] |
                        '1'[1-5]':' MINUTO |
                        '16:'[0-2][0-9] |
                        '16:30');    // 10:30 - 16:30



FECHA_BUSCADA: DIAS_DAD SEPARACION MESES_PARES SEPARACION ANIOS_RANGO ESPACIO+ HORA_BUSCADA ESPACIO+ ID_BUSCADO;
FECHA: DIAS SEPARACION MESES SEPARACION ANIOS ESPACIO+ HORA_COMPLETA ESPACIO+ ID;

WS: [\n\r]->skip;


s: FECHA_BUSCADA {print("FECHA_BUSCADA ->" + $FECHA_BUSCADA.text)} s |
   FECHA {print("FECHA ->" + $FECHA.text)} s |
   EOF;
 