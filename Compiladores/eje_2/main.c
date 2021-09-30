/*2. 
Generar programas en C que realicen las siguientes operaciones arreglos
de números enteros utilizando aritmética de punteros.
En el caso de operaciones, se deben utilizar dos arreglos de igual longitud y el resultado debe
almacenarse en un tercer arreglo:

-Sumar
-Restar
-Multiplicar
-Buscar máximo
-Buscar mínimo

Cada una de estas funciones debe implementarse en un archivo distinto.
Generar un main donde las funciones creadas anteriormente sean llamada
y ejecutar una compilación de dos pasos cada vez que sea necesario.*/

#include <stdlib.h>
#include <stdio.h>
#include "sumar.h"
//#include "restar.h"
//#include "multiplicar.h"
//#include "buscar_min.h"
//#include "buscar_max.h"

int main(){
    int numeros[10] = {1,2,3,4,5,6,7,8,9,10};
    int numeros2[10] = {1,2,3,4,5,6,7,8,9,10};
    int resultado[10];

    sumar(numeros,numeros2,resultado);
    //restar(numeros,numeros2,resultado);
    //multiplicar(numeros,numeros2,resultado);
    //min = buscar_min(resultado);
    //max = buscar_max(resultado);

    for (int i = 0; i < 10; i++){
        printf("%d - ",resultado[i]);
    }
    
}