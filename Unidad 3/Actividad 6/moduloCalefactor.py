class calefactor:
   __marca: str
   __modelo: str
   __origen: str
   __precio: float
   __cuotas: int
   __promocion: bool
   
   
   def __init__(self, marca, modelo, origen, precio, cuotas, promocion):
      self.__marca = marca
      self.__modelo = modelo
      self.__origen = origen
      self.__precio = precio
      self.__cuotas = cuotas
      self.__promocion = promocion
      
   def getMarca(self):
      return self.__marca
   
   def getModelo(self):
      return self.__modelo
   
   def getOrigen(self):
      return self.__origen
   
   def getPrecio(self):
      return self.__precio
   
   def getCuotas(self):
      return self.__cuotas
   
   def getPromocion(self):
      return self.__promocion
   
   def __str__(self):
      return self.__marca + " " + self.__modelo + "; Fabricado en: " + self.__origen