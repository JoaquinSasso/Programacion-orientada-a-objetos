class Antecedente:
   __nro : int
   __motivo: str
   __fecha: str
   __multa: float
   __condena : bool
   
   def __init__(self,nro, motivo, fecha, multa, condena):
      self.__nro = nro
      self.__motivo = motivo
      self.__fecha = fecha
      self.__multa = multa
      self.__condena = condena
   
   
   def getMotivo(self):
      return self.__motivo
   
   def getFecha(self):
      return self.__fecha
   
   def getMulta(self):
      return self.__multa
   
   def getCondena(self):
      return self.__condena
   
   def getNro(self):
      return self.__nro
   
   def __str__(self) -> str:
      return "Antecedente por: *" + self.__motivo + "* en el dia: " + self.__fecha + f". \nCon una multa de: $ {self.__multa:0.2f}. Condena : {self.__condena}"

   def toJSON(self):
      d = dict(clase = self.__class__.__name__,
               datos = dict(
                  nro = self.__nro,
                  motivo = self.__motivo,
                  fecha = self.__fecha,
                  multa = self.__multa,
                  condena = self.__condena
               ))
      return d
   