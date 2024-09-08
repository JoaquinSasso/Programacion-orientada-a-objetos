import sys
sys.dont_write_bytecode = True
from moduloCalefactorElectrico import electrico
from moduloCalefactorGas import gas
from moduloNodo import nodo
import json
from zope.interface import implementer
from interface import IArreglo
from pathlib import Path
@implementer(IArreglo)
class gestorCalefactores:
   __comienzo : nodo
   __actual : nodo
   __indice : int
   __tope : int
      
   
   def __init__(self):
      self.__comienzo = None
      self.__actual = None
      self.__tope = 0
      self.__indice = 0
   
   #Solicita todos los datos necesarios para crear un calefactor del tipo deseado y lo retorna
   def crearCalefactor(self):
      marca = input("Ingrese la marca del calefactor: ")
      modelo = input("Ingrese el modelo del calefactor: ")
      origen = input("Ingrese el pais de fabricacion del calefactor: ")
      promocion = input("El calefactor esta en promocion? Si/No : ")
      promocion = promocion.upper()   
      if promocion == "SI":
         promocion = True
      elif promocion == "NO":
         promocion = False
      try:
         precio = float(input("Ingrese el precio de lista del calefactor: "))
         cuotas = int(input("Ingrese la cantidad de cuotas: "))
         tipo = input("Ingrese el tipo de calefactor G: Gas ; E: Electrico: ")
         tipo = tipo.upper()
         if tipo == "E":
            potencia = int(input("Ingrese la potencia del calefactor: "))
         elif tipo == "G":
            matricula = input("Ingrese la matricula del calefactor: ")
            calorias = int(input("Ingrese la cantidad de calorias/m3: "))
         else:
            raise TypeError
      except ValueError:
         print("Se ingreso un valor que no es un numero")
      except TypeError:
         print("El tipo ingresado es incorrecto")
      else:
         if tipo == "E":
            calefactor = electrico(potencia, marca, modelo, origen, precio, cuotas, promocion)     
         elif tipo == "G":
            calefactor = gas(matricula, calorias, marca, modelo, origen, precio, cuotas, promocion)   
      return calefactor
   
   
   def agregarElemento(self, calefactor = None):
      if calefactor == None:
         calefactor = self.crearCalefactor()
      nuevoNodo = nodo(self.__comienzo, calefactor)
      self.__comienzo = nuevoNodo
      self.__actual = nuevoNodo
      self.__tope += 1
   
   
   def insertarElemento(self, indice):
      calefactor = self.crearCalefactor()
      i = 0
      anterior = None
      actual = self.__comienzo
      while((actual != None) and (i != indice)):
         anterior = actual
         actual = actual.sig()
         i += 1
      if anterior == None:
         self.agregarElemento(calefactor)
      else:
         nuevoNodo = nodo(actual, calefactor)
         anterior.setSig(nuevoNodo)
      self.__tope += 1
         
   
   def mostrarElemento(self, indice):
      i = 0
      actual = self.__comienzo
      while((actual != None) and (i != indice)):
         actual = actual.sig()
         i += 1
      if i == indice:
         print(actual)
      else:
         print("El indice ingresado esta fuera de rango")
   
   #Se definen los metodos iter y next para poder iterar la lista   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__indice == self.__tope:
         self.__actual = self.__comienzo
         self.__indice = 0
         raise StopIteration
      else:
         self.__indice += 1
         dato = self.__actual.datos()
         self.__actual = self.__actual.sig()
         return dato
      
   
   def calefactoresToJSON(self):
      lista = []
      for calefactor in self:
         lista.append(calefactor.toJSON())
      return lista
         
   
   
   def toJSON(self):
      d = dict(
         __class__ = self.__class__.__name__,
         datos = self.calefactoresToJSON()
      )
      return d
   
   
   def mostrarTipo(self, indice):
      i = 0
      try:
         indice = int(indice)
      except ValueError:
         print("El valor del indice debe ser un numero")
      else:
         if indice < 0:
            print("El indice era negativo, se convertira a positivo")
            indice *= -1
         actual = self.__comienzo
         while((actual != None) and (i != indice)):
            actual = actual.sig()
            i += 1
         if i == indice:
            print(actual.getTipo())
         else:
            print(f"El indice esta fuera de rango (0,{self.__tope - 1})")
            
   
   def gasBarato(self):
      barato = None
      precio = 99999999999
      for calefactor in self:
         if isinstance(calefactor, gas):
            precioActual = calefactor.getPrecio()
            if precioActual <  precio:
               precio = precioActual
               barato = calefactor
      print("El calefactor a gas mas barato es:")
      barato.mostrarDatos()
      
   
   def mostrarMarca(self, marca):
      bandera = False
      for calefactor in self:
         if (isinstance(calefactor, electrico)) and (calefactor.getMarca() == marca):
            print(calefactor)
            bandera = True
      if bandera == False:
         print("No hay calefones electricos de esa marca")
         
   
   def mostrarPromociones(self):
      for calefactor in self:
         if calefactor.getPromocion():
            print(calefactor)