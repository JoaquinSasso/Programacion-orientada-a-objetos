class producto:
   __nombre: str
   __fechaEnvasado : str
   __fechaVencimiento : str
   __temperatura : float
   __paisOrigen : str
   __numeroLote: str
   __costoBase : float
   
   
   def __init__(self, nombre, fechaEnvsado, fechaVencimiento, temperatura, paisOrigen, numeroLote, costoBase):
      self.__nombre = nombre
      self.__fechaEnvasado = fechaEnvsado
      self.__fechaVencimiento = fechaVencimiento
      self.__temperatura = temperatura
      self.__paisOrigen = paisOrigen
      self.__numeroLote = numeroLote
      self.__costoBase = costoBase
   
   def getNombre(self):
      return self.__nombre
   
   def getFechaEnvasado(self):
      return self.__fechaEnvasado
   
   def getFechaVencimiento(self):
      return self.__fechaVencimiento
   
   def getTemperatura(self):
      return self.__temperatura
   
   def getPaisOrigen(self):
      return self.__paisOrigen
   
   def getNumeroLote(self):
      return self.__numeroLote
   
   def getCostoBase(self):
      return self.__costoBase
   
   def __str__(self):
      pass
   