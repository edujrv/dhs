/*3. 
Automatizar el apartado anterior mediante el uso de makefiles
Luego modificar los códigos fuentes y construir el proyecto.
 Extraer conclusiones*/

#include <stdlib.h>
#include <stdio.h>
#include "../libs/sumar.h"
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