/*grammar expReg;

LETRA: [a-zA-Z];

PALABRA: (LETRA)+;

SPACE: [\n]->skip;

s: PALABRA {print("PALABRA -> "+$PALABRA.text)} s
    | EOF;


*/


/*
DIGITO: [0123456789];
LETRA: [a-zA-Z];
MAS: '+';


// Operadores de expresiones reg:

// seleccion: a | b
s1: DIGITO | LETRA;

// concatenacion
s2: DIGITO LETRA;

// agrupacion
s3: MAS (LETRA|DIGITO);

// Repeticion
    // Cero o mas veces: *
    // Una o mas veces: +
    // Al menos una vez: ? 
entero: (DIGITO)+;
palabra: (LETRA)+;

// comodin: .
s4: .;  // matchea con cualquiera menos el espacio

// agrupacion
 NUMERO: [0-9];

// negacion
neg: ^[NUMERO]; // cualquier cosa q no sea numero */