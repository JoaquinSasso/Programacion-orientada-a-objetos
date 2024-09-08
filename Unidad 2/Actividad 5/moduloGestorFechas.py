from moduloFecha import fecha
import csv
class gestorFechas:
   __fechas : list
   __fechas = []
   
   
   def __init__(self):
      saltar = False
      archivo = open("fechasFutbol.csv")
      reader = csv.reader(archivo, delimiter=";")
      for linea in reader:
         if saltar == False:
            saltar = True
         else:
            date = linea[0]
            idL = linea[1]
            idV = linea[2]
            gL = linea[3]
            gV = linea[4]
            unaFecha = fecha(date,idL, idV, gL, gV)
            self.__fechas.append(unaFecha)
      archivo.close()
   
   
   def listarFechas(self, ide):
      print("Fecha       GF    GC    DG    Puntos")
      totalGF = 0
      totalGC = 0
      totalPuntos = 0
      for unaFecha in self.__fechas:
         bandera = False
         if (int(unaFecha.getIdV() == ide)):
            gF = int(unaFecha.getGV())
            gC = int(unaFecha.getGL())
            bandera = True
         if (int(unaFecha.getIdL()) == ide):
            gC = int(unaFecha.getGV())
            gF = int(unaFecha.getGL())
            bandera = True
         if bandera == True:
            dG = gF - gC
            puntos = 0
            if gF > gC:
               puntos = 3
            if gF == gC:
               puntos = 1
            totalGF += gF
            totalGC += gC
            totalPuntos += puntos
            print(f"{unaFecha.getFecha()}    {gF}    {gC}     {dG}         {puntos}")
      print(f"Total:       {totalGF}    {totalGC}               {totalPuntos}")
      
   def obtenerLongitud(self):
      return len(self.__fechas)
   
      
   def obtenerFecha(self, indice):
      return self.__fechas[indice]
   
   
   def liberar(self):
      for fecha in self.__fechas:
         del fecha   