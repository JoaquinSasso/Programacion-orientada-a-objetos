class ladrillo:
   __alto = 7
   __largo = 25
   __ancho = 15
   __cantidad: int
   __identificador: int
   __kgMatPrimUtil: float
   __costo: float
   
   
   def __init__(self, cant, id, kg, costo):
      self.__cantidad = cant
      self.__identificador = id
      self.__kgMatPrimUtil = kg
      self.__costo = costo      
   
   @classmethod
   def getAlto(cls):
      return cls.__alto
   @classmethod
   def getAncho(cls):
      return cls.__ancho
   @classmethod
   def getAlto(cls):
      return cls.__largo
   