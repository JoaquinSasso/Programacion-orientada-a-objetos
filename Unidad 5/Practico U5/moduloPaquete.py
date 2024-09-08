class objPaquete:
   __numero : int
   __peso : float
   __nombreDestinario : str
   __direccionDestinatario: str
   __entregado : bool
   __observaciones : str
   __sucursal : object
   __repartidor : object
   __transporte: object
   
   
   def __init__(self, nro, peso, nombreDestinatario, direccionDestinatario, entegado, obsevaciones):
      self.__numero = nro
      self.__peso = peso
      self.__nombreDestinario = nombreDestinatario
      self.__direccionDestinatario = direccionDestinatario
      self.__entregado = entegado
      self.__observaciones = obsevaciones
      self.__sucursal = None
      self.__repartidor = None
      self.__transporte = None
      

   
   def getNumero(self):
      return self.__numero
   
   def getDireccionDestinatario(self):
      return self.__direccionDestinatario
   
   def getNombreDestinatario(self):
      return self.__nombreDestinario
   
   def getPeso(self):
      return self.__peso
   
   def getEntregado(self):
      return self.__entregado
   
   def getObservaciones(self):
      return self.__observaciones
   
   def getSucursal(self):
      return self.__sucursal
   
   def getRepartidor(self):
      return self.__repartidor
   
   def getTransporte(self):
      return self.__transporte
   
   def setSucursal(self, sucursal):
      self.__sucursal = sucursal
   
   def setRepartidor(self, repartidor):
      self.__repartidor = repartidor
   
   def setTransporte(self, transporte):
      self.__transporte = transporte
   
   