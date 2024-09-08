class vector:
   #Se crea la clase vector con sus atributos
   x : int
   y : int
   def __init__(self, xx, yy):
      #Metodo para inicializar una instancia
      self.x = xx
      self.y = yy
   def obtenerY(self):
      #Metodo para obtener el valor del atributo X
      return self.y
   def obtenerX(self):
      #Metodo para obtener el valor del atributo Y
      return self.x
   def mostrarDatos(self):
      print("{},{}".format(self.x,self.y))