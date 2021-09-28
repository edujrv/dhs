'''2. Agregar a la clase anterior
Un método que permita comparar dos clases vehículo entre si.
El atributo de comparación es la velocidad.
También se debe agregar el método __str__ para que imprima información de la clase'''

from Vehiculo import *

auto = Vehiculo("Renault")
auto.vel_max = 565
auto.km_rec = 500000

auto2 = Vehiculo("Golf")
auto2.vel_max = 564
auto2.km_rec = 45000

if(auto == auto2):
    print("Son iguales")
else:
    print("No son iguales")

print(auto)

