class objRepartidor:
   __numero : int
   __nombre : str
   __dni : str
   __paquete : list
   __sucursal : object
   
   def __init__(self, numero, nombre, dni, paquete = None, sucursal = None):
      self.__numero = numero
      self.__nombre = nombre
      self.__dni = dni
      self.__paquetes = []
      self.__sucursal = sucursal
   
   
   def getNumero(self):
      return self.__numero
   
   def getNombre(self):
      return self.__nombre
   
   def getDNI(self):
      return self.__dni
   
   def getPaquete(self):
      return self.__paquete
   
   def getSucursal(self):
      return self.__sucursal
   
   def agregarPaquete(self, paquete):
      self.__paquetes.append(paquete)
      
   def setSucursal(self, sucursal):
      self.__sucursal = sucursal
      
   