from moduloMatricula import capacitacion
import csv
class gestorCapacitaciones: 
   __capacitaciones: list
   

   def __init__(self):
      self.__capacitaciones = []
      archivo = open("Capacitaciones.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            nombre, cod, duracion = fila
            nuevo = capacitacion(nombre, cod, duracion)
            self.__capacitaciones.append(nuevo)
      archivo.close()
      
   
   def obtenerCapacitacion(self, codi: int):
      i = 0
      while((i < len(self.__capacitaciones)) and (self.__capacitaciones[i].getCod() != codi)):
         i += 1
      if i >= len(self.__capacitaciones):
         retorno = None
         print("No se encontro al empleado")
      else:
         retorno = self.__capacitaciones[i]
      return retorno
   
   
   # def buscarCapacitacion(self, cod):
   #    i = 0
   #    while((i < len(self.__capacitaciones)) and (self.__capacitaciones[i].getId() != cod)):
   #       i += 1
   #    if i >= len(self.__capacitaciones):
   #       i = -1
   #       print("No se encontro al empleado")
   #    return i