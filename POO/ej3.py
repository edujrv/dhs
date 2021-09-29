'''3. Agregar infraestructura unit test al ejercicio anterior y comparar que la
comparación funciona para vehículos más lentos, más rápidos o igual de
veloces.'''
#Unit test?
from Vehiculo import *
from pytest import *

# pip install pytest

auto = Vehiculo("Renault")
auto.vel_max = 565
auto.km_rec = 500000

auto2 = Vehiculo("Golf")
auto2.vel_max = 564
auto2.km_rec = 45000

assert (auto == auto2) == False
assert (auto > auto2) == True
assert (auto < auto2) == False


if(auto == auto2):
    print("Son iguales")
elif(auto < auto2):
    print("Tu renault es lentisimo")
elif(auto > auto2):
    print("Tu renault es una bestia")



