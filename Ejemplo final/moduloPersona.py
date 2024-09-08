
class Persona:
   __nombre : str
   __apellido: str
   __nacimiento : str
   __dni: str

   
   def __init__(self, nombre, apellido, nacimiento, dni):
      self.__nombre = nombre
      self.__apellido = apellido
      self.__nacimiento = nacimiento
      self.__dni = dni
   
   def getNombre(self):
      return self.__nombre
   
   def getApellido(self):
      return self.__apellido
   
   def getNacimiento(self):
      return self.__nacimiento
   
   def getDNI(self):
      return self.__dni

   def __eq__(self, otro):
      return self.__dni == otro
   
   def polimorfismo(self):
      print("\nEsta es la funcion polimorfismo de una persona")
      num1 = int(input("Ingrese un numero entero: "))
      num2 = int(input("Ingrese otro numero entero: "))
      print(f"La suma entre los dos es {num1 + num2}")