from abc import ABC, abstractmethod

class Vehiculo(ABC):
    tiempo_marcha = None
    @abstractmethod
    def arrancar(self):
        pass
    def frenar(self):
        pass
    def tiempo_de_marcha(self, start, finish):
        pass
#################
class Colectivo(Vehiculo):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, start, finish):
        self.tiempo_marcha = (finish-start)

class Motocicleta(Vehiculo):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, start, finish):
        self.tiempo_marcha = (finish-start)

class Camion(Vehiculo):
    def arrancar(self):
        return super().arrancar()
    def frenar(self):
        return super().frenar()
    def tiempo_de_marcha(self, start, finish):
        self.tiempo_marcha = (finish-start)

class Automovil(Vehiculo):
    def arrancar(self):
        return 
    def frenar(self):
        return 
    def tiempo_de_marcha(self, start, finish):
        self.tiempo_marcha = (finish-start)
