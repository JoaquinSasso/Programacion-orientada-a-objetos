class cliente:
   __nombre: str
   __apellido : str
   __dni : str
   __nroCuenta : int
   __saldoAnterior : float
   
   def __init__(self, nombre, apellido, dni, nro, saldoA):
      self.__nombre = nombre
      self.__apellido = apellido
      self.__dni = dni
      self.__nroCuenta = nro
      self.__saldoAnterior = saldoA
      
   def getNombre(self):
      return self.__nombre
   def getApellido(self):
      return self.__apellido
   def getDni(self):
      return self.__dni
   def getNro(self):
      return self.__nroCuenta
   def getSaldo(self):
      return self.__saldoAnterior
   def setSaldo(self, saldo):
      self.__saldoAnterior = saldo