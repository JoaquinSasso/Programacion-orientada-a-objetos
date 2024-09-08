class Vehiculo:
   __asientos : int
   __potencia: int
   __nombre: str
   
   def __init__(self, asientos, potencia, nombre):
      self.__asientos = int(asientos)
      self.__potencia = float(potencia)
      self.__nombre = nombre      
   
   def getNombre(self):
      return self.__nombre
   
   def getAsientos(self):
      return self.__asientos
   
   def getPotencia(self):
      return self.__potencia   
   
   def polimorfismo(self):
      print("\nEsta es la funcion polimorfismo de un vehiculo")
      print(f"La identidad de este objeto es: {id(self)}")
