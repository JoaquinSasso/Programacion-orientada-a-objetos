from moduloVehiculo import Vehiculo

class Combustion(Vehiculo):
   __combustible : float
   
   def __init__(self, asientos, potencia, nombre, bateria = 0, combustible = 0):
      super().__init__(asientos, potencia, nombre)
      self.__combustible = combustible
   
   def getCombustible(self):
      return self.__combustible

   def __str__(self):
      return f"Clase Combustion"
   
   def polimorfismo(self):
      print("\nEsta es la funcion polimorfismo de un vehiculo a combustible")
      print(f"El vehiculo tiene capacidad de {self.__combustible} litros de combustible")