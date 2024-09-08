class departamento:
   __id : int
   __propietario: str
   __nroPiso: int
   __nroDpto: int
   __cantHabitaciones: int
   __cantBanos: int
   __superficie: float
   
   def __init__(self, **kwargs):
      self.__id = int(kwargs["id"])
      self.__propietario = kwargs["propietario"]
      self.__nroPiso = int(kwargs["nroPiso"])
      self.__nroDpto = int(kwargs["nroDpto"])
      self.__cantHabitaciones = int(kwargs["cantHabitaciones"])
      self.__cantBanos = int(kwargs["banos"])
      self.__superficie = float(kwargs["superficie"])
   
   def mostrarPropietario(self):
      print(f"El propietario es: {self.__propietario}")
      
   
   def getSuperficie(self):
      return self.__superficie
   
   def getPropietario(self):
      return self.__propietario
   
   def getBanos(self):
      return self.__cantBanos
   
   def getHabitaciones(self):
      return self.__cantHabitaciones
   
   def getPiso(self):
      return self.__nroPiso