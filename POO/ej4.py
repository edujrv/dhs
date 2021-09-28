'''4. 
Definir una clase abstracta llamada vehículo con las interfaces:
- arrancar()
- frenar()
- tiempo_de_marcha()
Luego implementar las clases hijas:
a) Colectivo
b) Motocicleta
c) Camión
d) Automóvil

Implementar cada uno de los métodos heredados de la clase abstracta.
Crear una lista con 10 instancias
1 Colectivo
2 motocicleta
3 camiones
4 automóviles
Se debe recorrer la lista, invocar a los métodos arrancar() y esperar un tiempo random.
Finalmente, se debe volver a recorrer la lista, invocando los métodos frenar()
Imprimir el tiempo de marcha de cada uno de los vehículos 
(diferencia de tiempos entre arrancar y frenar).'''

from Vehiculo2 import *
import time
from random import *

semaforo = [Camion(),Colectivo(),Motocicleta(),Automovil()]
tiemposi = list()
tiemposf = list()
flag = True

print("Arranquen!!")
i = 0
for movil in semaforo:
    movil.arrancar()
    tiemposi[i] = time.time()
    i+=1

while(flag == True):
    rnd = randint(1,1000)
    if (180 <= rnd <= 535):
        flag = False
print(rnd)
print("Frenen!!")
i = 0
for movil in semaforo:
    movil.frenar()
    movil.tiempo_de_marcha(tiemposi[i], time.time())
    print(movil.tiempo_marcha)
    i+=1



    