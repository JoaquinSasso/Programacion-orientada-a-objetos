class cuenta:
   __cvu : int
   __apellido: str
   __nombre: str
   __dni: int
   __telefono: int
   __saldo: float
   __rendimiento = 68.0
   
   
   @classmethod
   def actualizarRendimiento(cls, nuevoRendimiento):
      cls.__rendimiento = nuevoRendimiento
   
   
   def __init__(self, cvu, apellido, nombre, dni, telefono, saldo):
      self.__cvu = cvu
      self.__apellido = apellido
      self.__dni = dni
      self.__nombre = nombre
      self.__telefono = telefono
      self.__saldo = saldo
      
      
   def getCvu(self):
      return self.__cvu
   def getApellido(self):
      return self.__apellido
   def getNombre(self):
      return self.__nombre
   def getDni(self):
      return self.__dni
   def getTelefono(self):
      return self.__telefono
   def getSaldo(self):
      return self.__saldo
   @classmethod
   def getRendimiento(cls):
      return cls.__rendimiento
   def actualizarSaldo(self, importe):
      self.__saldo += importe
   def setSaldo(self, nuevoSaldo):
      self.__saldo = nuevoSaldo
      
      