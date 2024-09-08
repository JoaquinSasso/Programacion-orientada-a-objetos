from moduloVehiculo import Vehiculo

class Electrico(Vehiculo):
   __bateria : float
   
   def __init__(self, asientos, potencia, nombre, bateria = 0, combustible = 0):
      super().__init__(asientos, potencia, nombre)
      self.__bateria = float(bateria)
   
   def getBateria(self):
      return self.__bateria

   def __str__(self):
      return f"Clase Electrico"