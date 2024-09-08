from cajaDeAhorro import cajaDeAhorro
from typing import List
class controlador:
   __cajas : List[cajaDeAhorro]
   def __init__(self):
      self.__cajas = [] 
      
      
   def crearCaja(self):
      nro = input("Ingrese el nro de la caja de ahorro: ")
      apellido = input("Ingrese el apellido del cliente: ")
      nombre = input("Ingrese el nombre del cliente: ")
      saldo = float(input("Ingrese el saldo de la caja de ahorro: "))
      cuil = input("Ingrese el cuil del cliente: ")
      objeto = cajaDeAhorro(nro,cuil,apellido, nombre, saldo)
      self.__cajas.append(objeto)
      
      
   def mostrarCajas(self):
      for caja in self.__cajas:
         print(f"La caja tiene cuil: {caja.getCuil()}")
   def obtenerDatos(self, cuilIngresado):
      i = 0
      cuil = self.__cajas[i].getCuil()
      while (i < len(self.__cajas)) and (cuil != cuilIngresado):
         i += 1
         cuil = self.__cajas[i].getCuil()
      if cuil == cuilIngresado:
         apellido = self.__cajas[i].getApellido()
         nombre = self.__cajas[i].getNombre()
         saldo = self.__cajas[i].getSaldo()
      return apellido, nombre, saldo
