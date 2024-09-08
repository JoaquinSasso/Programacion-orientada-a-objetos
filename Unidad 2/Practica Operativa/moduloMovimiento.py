class movimiento:
   __nroCuenta : int
   __fecha : str
   __descripcion: str
   __tipo : str
   __importe: float
   
   
   def __init__(self, nro, fecha, descripcion, tipo, importe):
      self.__nroCuenta = nro
      self.__fecha = fecha
      self.__descripcion = descripcion
      self.__tipo = tipo
      self.__importe = importe
      
      
   def getNro(self):
      return self.__nroCuenta
   def getFecha(self):
      return self.__fecha
   def getDescripcion(self):
      return self.__descripcion
   def getTipo(self):
      return self.__tipo
   def getImporte(self):
      return self.__importe
   
   
   def __lt__(self, otro):
      return self.__nroCuenta < otro.getNro()