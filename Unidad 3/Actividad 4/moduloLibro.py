from moduloPublicacion import publicacion
class libro(publicacion):
   __autor: str
   __fecha : int
   __paginas : int
   
   
   def __init__(self, autor, fecha, paginas, titulo, cat, precio):
      self.__autor = autor
      self.__fecha = fecha
      self.__paginas = paginas
      super().__init__(titulo, cat, precio)
   
   def getAutor(self):
      return self.__autor
   def getFecha(self):
      return self.__fecha
   def getPaginas(self):
      return self.__paginas
   
   
   def getPrecioFinal(self):
      precioBase = super().getPrecio()
      porcentaje = ((2024 - self.__fecha) / 100)
      precioFinal =precioBase - (precioBase * porcentaje)
      return precioFinal
   
   
   def __str__(self):
      precio = self.getPrecioFinal()
      titulo = super().getTitulo()
      categoria = super().getCategoria()
      return "Titulo: "+ titulo + "; Categoria: " + categoria + "; Importe de venta: $" + "{:0.2f}".format(precio)
   
   
   
   