from zope.interface import implementer
from zope.interface import interface
from interface import IArreglo
from moduloPersona import persona
import csv

@implementer(IArreglo)
class gestorPersonas:
   __personas : list
   
   def __init__(self):
      self.__personas = []
      archivo = open("personas.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            nombre,edad,genero = fila
            nuevo = persona(nombre, int(edad), genero)
            self.__personas.append(nuevo)
   
   def insertarElemento(self, indice):
      try:
         indice = int(indice)
      except ValueError:
         print("El indice ingresado no era un numero")
      else:
         nombre = input("Ingrese el nombre de la pesrona: ")
         try:
            edad = int(input("Ingrese la edad de la persona: "))
         except ValueError:
            print("La edad ingresada debe ser un numero")
         else:
            genero = input("Ingrese el genero de la persona: ")
            nuevo = persona(nombre, edad, genero)
            try:
               self.__personas[indice] = nuevo
            except IndexError:
               print(f"El indice ingresado no esta dentro del rango (0,{len(self.__personas)-1})")
            
   
   def agregarElemento(self):
      nombre = input("Ingrese el nombre de la pesrona: ")
      try:
         edad = int(input("Ingrese la edad de la persona: "))
      except ValueError:
         print("La edad ingresada debe ser un numero")
      else:
         genero = input("Ingrese el genero de la persona: ")
         nuevo = persona(nombre, edad, genero)
         self.__personas.append(nuevo)
      
      
   def mostrarElemento(self, indice):
      try:
         indice = int(indice)
      except ValueError:
         print("El indice ingresado no era un numero")
      else:
         try:
            print(self.__personas[indice])
         except IndexError:
            print(f"El indice ingresado no esta dentro del rango (0,{len(self.__personas)-1})")
   
   
   def mostrarTodos(self):
      for per in self.__personas:
         print(per)
   
