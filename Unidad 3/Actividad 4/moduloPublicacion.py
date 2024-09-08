class publicacion:
   __titulo : str
   __categoria : str
   __precio : float
   
   
   def __init__(self, titulo, cat, precio):
      self.__titulo = titulo
      self.__categoria = cat
      self.__precio = precio
      
      
   def getTitulo(self):
      return self.__titulo
   def getCategoria(self):
      return self.__categoria
   def getPrecio(self):
      return self.__precio
   