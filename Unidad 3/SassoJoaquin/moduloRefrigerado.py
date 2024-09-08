from moduloProducto import producto
class refrigerado(producto):
   __codigoOrganismo = str
   
   def __init__(self, nombre, fechaEnvsado, fechaVencimiento, temperatura, paisOrigen, numeroLote, costoBase, codigoOrganismo):
      super().__init__(nombre, fechaEnvsado, fechaVencimiento, temperatura, paisOrigen, numeroLote, costoBase)
      self.__codigoOrganismo = codigoOrganismo
   
   def getCodigoOrganismo(self):
      return self.__codigoOrganismo
   
   def getPrecio(self):
      precioBase = super().getCostoBase()
      vencimiento = super().getFechaVencimiento()
      vencimiento = vencimiento.split("/")
      vencimiento = vencimiento[1]
      vencimiento = int(vencimiento)
      mesActual = 5
      if((vencimiento - mesActual) <= 2):
         precio = precioBase - (precioBase * 0.1)
      else:
         precio = precioBase * 1.01
      return precio
   
   
   def __str__(self):
      return super().getNombre() + ". Hecho en: " + super().getPaisOrigen() + f". Se recomienda conservar a {super().getTemperatura()} grados" + "\nImporte de venta: $" + f"{self.getPrecio():0.2f}" 