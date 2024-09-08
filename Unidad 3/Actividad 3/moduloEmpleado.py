class empleado:
   __nombre: str
   __id : int
   __puesto: str
   
   
   def __init__(self, id, nombre, puesto):
      self.__id = int(id)
      self.__nombre = nombre
      self.__puesto = puesto
      
   def getId(self):
      return self.__id
   def getPuesto(self):
      return self.__puesto
   def getNombre(self):
      return self.__nombre