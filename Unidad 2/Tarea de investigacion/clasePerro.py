class perro: #Se crea la clase perro
   #Se definen sus atributos
   __nombre: str
   __edad: int
   def __init__(self, nombre, edad): #Metodo para inicializar el objeto
      self.__nombre = nombre
      self.__edad = edad
   def getEdad(self): #Devuelve la edad del perro
      return self.__edad
   def getNombre(self): #Devuelve el nombre del perro
      return self.__nombre
   
   def __lt__(self, otro):
      #Sobrecargamos el operador < comparando la edad de los perros
      return self.__edad < otro.getEdad()
   def __gt__(self, numero):
      return self.__edad > numero
   
   
   #== __eq__
   #<  __lt__
   #>  __gt__
   #<= __le__
   #>= __ge__
   #!= __ne__