class Vehiculo:
    #'''Esta clase define los atributos (marcas , velocidad maxima y km recorridos) de un auto'''

    def __init__(self, marca):
         self.marca = marca

    @property
    def vel_max(self):
        return self.__vel_max
    @vel_max.setter
    def vel_max(self, val):
        self.__vel_max = val
    
    @property
    def km_rec(self):
        return self.__km_rec
    @km_rec.setter
    def km_rec(self, val):
        self.__km_rec = val

    def __eq__(self, other):
        return self.vel_max == other.vel_max

    def __lt__(self, other):
        return self.vel_max < other.vel_max

    def __gt__(self, other):
        return self.vel_max > other.vel_max

    def __str__(self):
        return "Marca: {}, Vel_max: {}, Km_rec: {}".format(self.marca,self.vel_max,self.km_rec)