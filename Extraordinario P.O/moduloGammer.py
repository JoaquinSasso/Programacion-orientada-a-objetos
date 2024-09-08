class gammer:
   __idJugador : int
   __dni : str
   __nombre : str
   __apellido : str
   __alias : str
   __plan : str
   __importeBase : float
   __tiempoLimite: int
   
   def __init__(self, idJugador, dni, nombre, apellido, alias, plan, importeBase, tiempoLimite):
      self.__idJugador = int(idJugador)
      self.__dni = dni
      self.__nombre = nombre
      self.__apellido = apellido
      self.__alias = alias
      self.__plan = plan
      self.__importeBase = float(importeBase)
      self.__tiempoLimite = int(tiempoLimite)
   
   def getId(self):
      return self.__idJugador
   
   def getDni(self):
      return self.__dni
   
   def getNombre(self):
      return self.__nombre
   
   def getApellido(self):
      return self.__apellido
   
   def getAlias(self):
      return self.__alias
   
   def getPlan(self):
      return self.__plan
   
   def getImporte(self):
      return self.__importeBase
  
   def getTiempoLimite(self):
      return self.__tiempoLimite
   
   def __str__(self):
      return "Nombre: " + f"{self.__nombre} {self.__apellido}" + f"; Alias: {self.__alias}" + f"; Plan: {self.__plan}"
   