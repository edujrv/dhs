from abc import ABC, abstractmethod

class Vehiculo(ABC):
    tiempo_marcha = None
    @abstractmethod
    def arrancar(self):
        pass
    def frenar(self):
        pass
    def tiempo_de_marcha(self, time):
        pass
#################
class Colectivo(Vehiculo):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, time):
        self.tiempo_marcha = (time)
    def presentacion(self):
        return "Colectivo"

class Motocicleta(Vehiculo):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, time):
        self.tiempo_marcha = (time)
    def presentacion(self):
        return "Motocicleta"
class Camion(Vehiculo):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, time):
        self.tiempo_marcha = (time)
    def presentacion(self):
        return "Camion"

class Automovil(Vehiculo):
    def arrancar(self):
        return 
    def frenar(self):
        return 
    def tiempo_de_marcha(self, time):
        self.tiempo_marcha = (time)
    def presentacion(self):
        return "Automovil"
