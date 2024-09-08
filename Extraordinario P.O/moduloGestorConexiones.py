import csv
import numpy as np
from moduloConexion import conexion

class gestorConexiones:
   __lista : np.ndarray[conexion]
   __tamaño = 0
   __dimension = 0
   __aumento = 1
   
   def __init__(self):
      self.__lista = np.empty(0, conexion)
      archivo = open("conexiones.csv")
      reader = csv.reader(archivo, delimiter=";")
      skip = False
      for fila in reader:
         if skip == False:
            skip = True
         else:
            id = fila[0]
            ip = fila[1]
            juego = fila[2]
            fecha = fila[3]
            inicio = fila[4]
            fin = fila[5]
            nuevaConexion = conexion(id, ip, juego, fecha, inicio, fin)
            self.agregar(nuevaConexion)
      archivo.close()
   
   def agregar(self, nuevo):
      if self.__tamaño == self.__dimension:
         self.__dimension += self.__aumento
         self.__lista.resize(self.__dimension)
      self.__lista[self.__tamaño] = nuevo
      self.__tamaño += 1
   
   def emitirListado(self, idG):
      tiempoTotal = 0
      print("Ip de conexion      Juego          Fecha        Hora Inicio   Hora Fin")
      for i in range(self.__tamaño):
         actual : conexion = self.__lista[i]
         if actual.getId() == idG:
            print(f"{actual.getIp()}     {actual.getJuego()}   {actual.getFecha()}     {actual.getInicio()}           {actual.getFin()}")
            tiempoTotal += actual.getFin() - actual.getInicio()
      return tiempoTotal
   
   def mostrarJugadores(self, juego, gammers):
      i = 0
      while((i < self.__tamaño) and (juego != self.__lista[i].getJuego())):
         i += 1
      if i == self.__tamaño:
         print("No existe el juego")
      else:
         for i in range(self.__tamaño):
            if self.__lista[i].getJuego() == juego:
               print(f"Direccion ip: {self.__lista[i].getIp()}", end= " ")
               gammers.mostrarDatos(self.__lista[i].getId())
   
   def conexionesRepetidas(self,gammers):
      self.__lista.sort()
      for i in range(0,len(self.__lista)):
         for j in range(0, len(self.__lista)):
            servicio = gammers.buscarPlan(self.__lista[i].getId())
            if servicio == 'Basico' and j < i:
               if self.__lista[i] == self.__lista[j]:
                  gammers.mostrarDatos(self.__lista[i].getId())