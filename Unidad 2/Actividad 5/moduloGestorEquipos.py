from moduloEquipo import equipo
from moduloGestorFechas import gestorFechas
import csv
class gestorEquipos:
   __equipos : list
   __equipos = []
   
   
   def __init__(self):
      saltar = False
      archivo = open("equipos2024.csv")
      reader = csv.reader(archivo, delimiter=";")
      for linea in reader:
         if saltar == False:
            saltar = True
         else:
            ide = linea[0]
            nombre = linea[1]
            gA = linea[2]
            gC = linea[3]
            dG = linea[4]
            puntos = linea[5]
            unEquipo = equipo(ide, nombre, gA, gC, dG, puntos)
            self.__equipos.append(unEquipo)
      archivo.close()
      
   def buscarEquipo(self, ide): #Queda en desuso porque es mas facil ordenarlos por identificador y hacer acceso directo
      i = 0
      while ((i < (len(self.__equipos)+1)) and (self.__equipos[i].getIdE() != ide)):
         i += 1
      if (self.__equipos[i].getIdE() != ide):
         i = -1
      return i
   
   
   def ordenarPorID(self):
      self.__equipos.sort()
      
            
   def listarFechas(self,fechas, ide):
      self.ordenarPorID()
      print(f"El nombre del equipo es: {self.__equipos[ide-1].getNombre()}")
      fechas.listarFechas(ide)
   
   
   def ordenarPorPuntaje(self):
      n = len(self.__equipos)
      for i in range(n):
         for j in range(0, n-i-1):
            if self.__equipos[j] > self.__equipos[j+1]:
                  auxiliar = self.__equipos[j]
                  self.__equipos[j]= self.__equipos[j+1]
                  self.__equipos[j+1] = auxiliar
            
            elif self.__equipos[j] == self.__equipos[j+1]:
               if self.__equipos[j].getDG() > self.__equipos[j+1].getDG():
                  auxiliar = self.__equipos[j]
                  self.__equipos[j]= self.__equipos[j+1]
                  self.__equipos[j+1] = auxiliar
               
               elif self.__equipos[j].getDG() == self.__equipos[j+1].getDG():
                  if self.__equipos[j].getGF() > self.__equipos[j+1].getGF():
                     auxiliar = self.__equipos[j]
                     self.__equipos[j]= self.__equipos[j+1]
                     self.__equipos[j+1] = auxiliar
      self.__equipos.reverse()
      
   
   def mostrarTabla(self):
      for club in self.__equipos:
         print(f"""Nombre: {club.getNombre()}
                           Puntaje: {club.getPuntos()}, DG: {club.getDG()}, GF: {club.getGF()}""")      
      
   def actualizarTablas(self, fechas):
      for i in range(fechas.obtenerLongitud()):
         partido = fechas.obtenerFecha(i)
         idL = int(partido.getIdL()) -1
         idV = int(partido.getIdV()) -1
         gL = int(partido.getGL())
         gV = int(partido.getGV())
         self.__equipos[idL].agregarGF(gL)
         self.__equipos[idL].agregarGC(gV)
         self.__equipos[idV].agregarGF(gV)
         self.__equipos[idV].agregarGC(gL)
         self.__equipos[idL].actualizarDG()
         self.__equipos[idV].actualizarDG()
         if gV == gL:
            self.__equipos[idV].agregarPuntos(1)
            self.__equipos[idL].agregarPuntos(1)
         if gV > gL:
            self.__equipos[idV].agregarPuntos(3)
         if gL > gV:
            self.__equipos[idL].agregarPuntos(3)
            
            
   def guardarTabla(self):
      archivo = open("tablaActualizada.csv", mode="w", newline='')
      writer = csv.writer(archivo, delimiter =";")
      writer.writerow(["Identificador", "Nombre", "Goles A Favor", "Goles en Contra", "Diferencia de Goles", "Puntos"])
      for i in range(len(self.__equipos)):
         arreglo = []
         ide = self.__equipos[i].getIdE()
         nombre = self.__equipos[i].getNombre()
         gA = self.__equipos[i].getGF()
         gC = self.__equipos[i].getGC()
         dG = self.__equipos[i].getDG()
         puntos = self.__equipos[i].getPuntos()
         arreglo.append(ide)
         arreglo.append(nombre)
         arreglo.append(gA)
         arreglo.append(gC)
         arreglo.append(dG)
         arreglo.append(puntos)
         writer.writerow(arreglo)
      archivo.close()
      print("El archivo se guardo exitosamente")   
      
   def liberar(self):
      for equipo in self.__equipos:
         del equipo
      