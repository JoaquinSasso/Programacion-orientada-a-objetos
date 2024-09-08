from moduloPublicacion import publicacion

class cd(publicacion):
   __duracion : int
   __narrador : str
   
   def __init__(self, titulo, cat, precio, duracion, narrador):
      self.__duracion = duracion
      self.__narrador = narrador
      super().__init__(titulo, cat, precio)
      
   def getDuracion(self):
      return self.__duracion
   def getNarrador(self):
      return self.__narrador
   
   
   def getPrecioFinal(self):
      precioBase = super().getPrecio()
      precioFinal = precioBase * 1.1
      return precioFinal
   
   
   def __str__(self):
      precio = self.getPrecioFinal()
      titulo = super().getTitulo()
      categoria = super().getCategoria()
      return "Titulo: "+ titulo + "; Categoria: " + categoria + "; Importe de venta: $" + "{:0.2f}".format(precio)
      