class objSucursal:
   __numero : int
   __provincia : str
   __localidad : str
   __direccion : str
   __paquetes : list
   __repartidores : list
   __transportes : list
   
   
   def __init__(self, numero, provincia, localidad, direccion):
      self.__numero = numero
      self.__provincia = provincia
      self.__localidad = localidad
      self.__direccion = direccion
      self.__paquetes = []
      self.__localidad = []
      self.__repartidores = []
      
   
   def getNumero(self):
      return self.__numero
   
   def getProvincia(self):
      return self.__provincia
   
   def getLocalidad(self):
      return self.__localidad
   
   def getDireccion(self):
      return self.__direccion
   
   def getPaquetes(self):
      return self.__paquetes
   
   def getRepartidores(self):
      return self.__repartidores
   
   def getTransportes(self):
      return self.__transportes
   
   def agregarPaquete(self, paquete):
      self.__paquetes.append(paquete)
      
   def agregarRepartidor(self, repartidor):
      self.__repartidores.append(repartidor)
   
   def agregarTransporte(self, transporte):
      self.__transportes.append(transporte)