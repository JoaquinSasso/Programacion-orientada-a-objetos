import datetime

class objTransporte:
   __numero : int
   __fechaHoraSalida : datetime
   __fechaHoraLLegada : datetime
   __sucursal : object
   __paquetes : list
   
   
   def __init__(self, numero, fechaSalida, fechaLlegada, sucursal = None):
      self.__sucursal = sucursal
      self.__numero = numero
      self.__fechaHoraLLegada = fechaLlegada
      self.__fechaHoraSalida = fechaSalida
   
   
   def getNumero(self):
      return self.__numero
   
   def getFechaLlegada(self):
      return self.__fechaHoraLLegada
   
   def getFechaSalida(self):
      return self.__fechaHoraSalida
   
   def getSucursal(self):
      return self.__sucursal
   
   def getPaquetes(self):
      return self.__paquetes
   
   def setSucursal(self, sucural):
      self.__sucursal = sucural
      
   def agregarPaquete(self, paquete):
      self.__paquetes.append(paquete)