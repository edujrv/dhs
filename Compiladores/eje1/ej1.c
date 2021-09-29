/*1. 
Crear un código fuente en C que sume dos números enteros recibidos por
teclado e imprima el resultado por pantalla.

Obtener el archivo luego de la ejecución del pre-procesador. ¿Qué
directivas son eliminadas o reemplazas?

A partir del item anterior, obtener el código assembler utilizando
GCC. ¿Para qué arquitecutura es el código?

Ejecutar el ensamblado del apartado anterior
Enlazar el objeto y generar el ejecutable
Extraer conclusiones sobre lo sucedido en cada una de las etapas.*/

#include <stdio.h>


int main() {
    int num1, num2, suma;
    
    printf("Ingrese el primer numero: ");
    scanf("%d", &num1);
    printf("Ingrese el segundo numero: ");
    scanf("%d", &num2);
    suma = num1 + num2;
    printf("%d",suma);
    return 0;
}
