class persona:
   __nombre: str
   __edad: int
   __genero: str
   
   
   def __init__(self, nombre, edad, genero):
      self.__nombre = nombre
      try:
         if edad < 0:
            raise ValueError
      except ValueError:
         print("La edad se cambiara por un numero positivo")
         edad *= -1
      finally:
         self.__edad = edad
      self.__genero = genero

   def __str__(self):
      return self.__nombre + "; tiene " +str( self.__edad) + " años y es: " + self.__genero