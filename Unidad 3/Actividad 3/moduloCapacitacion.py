class capacitacion:
   __nombre: str
   __cod : str
   __duracion : int
   
   
   def __init__(self, nombre, cod, duracion):
      self.__nombre = nombre
      self.__cod = int(cod)
      self.__duracion = int(duracion)
      
      
   def getNombre(self):
      return self.__nombre
   def getDuracion(self):
      return self.__duracion
   def getCod(self):
      return self.__cod
   