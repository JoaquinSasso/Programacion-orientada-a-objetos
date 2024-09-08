from moduloCombustion import Combustion
from moduloElectrico import Electrico

class Hibrido(Electrico, Combustion):
   __autonomia : float
   
   def __init__(self, asientos, potencia, nombre, bateria=0, combustible=0, autonomia = 0):
      super().__init__(asientos, potencia, nombre, bateria, combustible)
      self.__autonomia = autonomia
   
   def getAutonomia(self):
      return self.__autonomia

   def __str__(self):
      return f"Clase Hibrido"