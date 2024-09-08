from moduloProducto import producto
class congelado(producto):
   __nitrogeno : int
   __oxigeno : int
   __co2 : int
   __vapor : int
   __metodoCongelacion : str
   
   def __init__(self, nombre, fechaEnvsado, fechaVencimiento, temperatura, paisOrigen, numeroLote, costoBase, nitrogeno, oxigeno, co2, vapor, metodoCongelacion):
      super().__init__(nombre, fechaEnvsado, fechaVencimiento, temperatura, paisOrigen, numeroLote, costoBase)
      self.__nitrogeno = nitrogeno
      self.__oxigeno = oxigeno
      self.__co2 = co2
      self.__vapor = vapor
      self.__metodoCongelacion = metodoCongelacion
   
   def getComposicion(self):
      return self.__nitrogeno, self.__oxigeno, self.__co2, self.__vapor
   
   def getMetodoCongelacion(self):
      return self.__metodoCongelacion
   
   def getPrecio(self):
      precioBase = super().getCostoBase()
      if self.__metodoCongelacion == "mecanico":
         precio = precioBase * 1.15
      elif self.__metodoCongelacion == "criogenico":
         precio = precioBase * 1.15
      return precio
   
   
   def __str__(self):
      return super().getNombre() + ". Hecho en: " + super().getPaisOrigen() + f". Se recomienda conservar a {super().getTemperatura()} grados" + "\nImporte de venta: $" + f"{self.getPrecio():0.2f}" 