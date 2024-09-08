from moduloCalefactor import calefactor
class electrico(calefactor):
   __potencia : int
   
   def __init__(self, potencia, marca, modelo, origen, precio, cuotas, promocion):
      super().__init__(marca, modelo, origen, precio, cuotas, promocion)
      self.__potencia = potencia
   
   
   def getPrecio(self):
      precioLista = super().getPrecio()
      precio = precioLista
      if super().getPromocion() == True:
         precio -= precioLista * 0.15
      if self.__potencia > 1000:
         precio += precioLista * 0.01
      if super().getCuotas() > 1:
         precio += precioLista * 0.3
      return precio

   def getPotencia(self):
      return self.__potencia
   
   def __str__(self):
      return super().__str__() + "; Con un precio de venta de: $" + "{:0.2f}".format(self.getPrecio())
   
   
   def mostrarDatos(self):
      print(f"{super().getMarca()} con una potencia de {self.__potencia} y un precio de lista de ${super().getPrecio()}")
   
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
         potencia = self.__potencia
         )
      )
      return d