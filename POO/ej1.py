'''1. 
Crear una clase vehículo.
Contenga los atributos marca, velocidad máxima y kilómetros recorridos.
La marca debe ser ingresada en el constructor 
Demás atributos deben tener sus métodos getters y setters.'''

#Pregunta, como se da cuenta en el property cual es para devolver el valor y cual para eliminar
  

from Vehiculo import *

auto = Vehiculo("Renault")
auto.vel_max = 565
auto.km_rec = 500000
print("Marca: "+auto.marca+"\nVel_max: "+str(auto.vel_max)+"\nKm_rec: "+str(auto.km_rec))


