class transaccion:
   __cvu: str
   __nro: int
   __importe: float
   __tipo: str


   def __init__(self, cvu, nro, importe, tipo):
      self.__cvu = cvu
      self.__nro = nro
      self.__importe = importe
      self.__tipo = tipo
      
   
   def getCvu(self):
      return self.__cvu
   def getImporte(self):
      return self.__importe
   def getNro(self):
      return self.__nro
   def getTipo(self):
      return self.__tipo