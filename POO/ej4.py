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

from datetime import datetime, timedelta
from sys import stdout
from time import sleep


semaforo = [Camion(),Colectivo(),Motocicleta(),Automovil()]
flag = True
rnd = randint(3,7)
print(rnd)

print("Arranquen!!")

tempo = timedelta(seconds = rnd)
for movil in semaforo:
    movil.arrancar()

print(rnd)

while(str(tempo) != '0:00:00'):
    stdout.write("\r%s"%tempo)
    stdout.flush()
    tempo = tempo - timedelta(seconds=1)
    sleep(1)

print("\nFrenen!!")
for movil in semaforo:
    movil.frenar()
    movil.tiempo_de_marcha(rnd)
    print(movil.presentacion()+": "+str(movil.tiempo_marcha))

stdout.flush()


    