from moduloMaterial import materialRefractario
import csv

class gestorMateriales:
   __materiales : list
   
   
   def __init__(self):
      archivo = open("MaterialesRefractarios.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            material = fila[0]
            caract = fila[1]
            cant = fila[2]
            costoAd = fila[3]
            nuevoMaterial = materialRefractario(material, caract, cant, costoAd)
            self.__materiales.append(nuevoMaterial)
            