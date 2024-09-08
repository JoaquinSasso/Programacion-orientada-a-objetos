import numpy as np
import csv
from moduloMovimiento import movimiento

class gestorMovimientos:
   __movimientos : np.ndarray
   __dimension : int
   __incremento : int
   __cantidad : int
   
   
   def agregarMovimiento(self, movimiento):
      if self.__cantidad == self.__dimension:
         self.__dimension += self.__incremento
         self.__movimientos.resize(self.__dimension)
      self.__movimientos[self.__cantidad] = movimiento
      self.__cantidad += 1   
   
   
   def __init__(self):
      self.__cantidad = 0
      self.__dimension = 0
      self.__incremento = 1
      self.__movimientos = np.empty(0, dtype= movimiento)
      archivo = open("MovimientosAbril2024.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            num = int(fila[0])
            fecha = fila[1]
            descripcion = fila[2]
            tipo = fila[3]
            importe = float(fila[4])
            nuevoMovimiento = movimiento(num, fecha, descripcion, tipo, importe)
            self.agregarMovimiento(nuevoMovimiento)
      archivo.close()
      
      
   def ordenarMovimientos(self):
      self.__movimientos.sort()
      print("La lista de movimientos fue ordenada")
      

   def busquedaBinaria(self, nro):
      piso = 0
      techo = self.__cantidad
      medio = int((piso + techo) / 2)
      while((piso <= techo) and (self.__movimientos[medio].getNro() != nro)):
         if self.__movimientos[medio].getNro() > nro:
            techo = medio - 1
         elif self.__movimientos[medio].getNro() < nro:
             piso = medio + 1
         medio = int((piso + techo) / 2)
      if piso > techo:
         print("No hay ningun movimiento asociado al cliente")
         medio = -1
      return medio
   
   def primerCoincidencia(self, nro):
      i = self.busquedaBinaria(nro)
      if i != -1:
         while ((i-1 >= 0) and (self.__movimientos[i-1].getNro() == nro)):
            i -= 1
      return i


   def listarMovimientos(self, nroCuenta):
      total = 0
      print("Movimientos")
      print("Fecha    Descripcion          Importe        Tipo de movimiento")
      i = self.primerCoincidencia(nroCuenta)
      if i != -1:
         while((i < self.__cantidad) and (self.__movimientos[i].getNro() == nroCuenta)):
            print(f"{self.__movimientos[i].getFecha()}   {self.__movimientos[i].getDescripcion()}        {self.__movimientos[i].getImporte():0.2f}       {self.__movimientos[i].getTipo()}")
            if self.__movimientos[i].getTipo() == "C":
               total += self.__movimientos[i].getImporte()
            elif self.__movimientos[i].getTipo() == "P":
               total -= self.__movimientos[i].getImporte()
            i += 1
      return total
   
   
   def detectarMovimiento(self, nro):
      bandera = False
      for i in range(self.__cantidad):
         if self.__movimientos[i].getNro() == nro:
            bandera = True
      return bandera