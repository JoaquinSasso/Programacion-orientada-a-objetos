from moduloCalefactor import calefactor
class gas(calefactor):
   __matricula : str
   __calorias : int
   
   def __init__(self, matricula, calorias, marca, modelo, origen, precio, cuotas, promocion):
      super().__init__(marca, modelo, origen, precio, cuotas, promocion)
      self.__calorias = calorias
      self.__matricula = matricula
   
   def getPrecio(self):
      precioLista = super().getPrecio()
      precio = precioLista
      if super().getPromocion() == True:
         precio -= precioLista * 0.15
      if self.__calorias > 3000:
         precio += precioLista * 0.01
      if super().getCuotas() > 1:
         precio += precioLista * 0.4
      return precio
   
   def getMatricula(self):
      return self.__matricula
   
   def getCalorias(self):
      return self.__calorias
   
   def __str__(self):
      return super().__str__() + "; Con un precio de venta de: $" + "{:0.2f}".format(self.getPrecio())
   
   
   def mostrarDatos(self):
      print(f"{super().getMarca()} {super().getModelo()} con {self.getCalorias()} calorias")
   
   
   def toJSON(self):
      d = dict(
         __class__ = self.__class__.__name__,
         __atributos__ = dict(
         marca = super().getMarca(),
         modelo = super().getModelo(),
         origen = super().getOrigen(),
         precio = super().getPrecio(),
         cuotas = super().getCuotas(),
         promocion = super().getPromocion(),     
         matricula = self.__matricula,
         calorias = self.__calorias
         )
      )
      return d