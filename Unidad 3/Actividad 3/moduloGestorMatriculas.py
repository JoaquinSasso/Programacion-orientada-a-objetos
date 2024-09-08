from moduloMatricula import matricula
from moduloGestorEmpleados import gestorEmpleados
from moduloGestorCapacitaciones import gestorCapacitaciones
import csv
class gestorMatriculas:
   __matriculas : list
   
   
   def __init__(self, gestorE : gestorEmpleados, gestorC : gestorCapacitaciones):
      self.__matriculas = []
      archivo = open("Matriculas.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            fecha = fila[0]
            id = int(fila[1])
            codi = int(fila[2])
            empleado = gestorE.obtenerEmpleado(id)
            capacitacion = gestorC.obtenerCapacitacion(codi)
            if ((capacitacion != None) and (empleado != None)):
               nuevo = matricula(fecha, empleado, capacitacion)
               self.__matriculas.append(nuevo)
            else:
               print("No se pudo cargar la matricula por algun error en la busqueda")
      archivo.close()
      
      
   def mostrarCapacitaciones(self, ide):
      for mat in self.__matriculas:
         if mat.getIdE() == ide:
            print(f"Participo en el programa de capacitacion: {mat.getNombreCap()} con una duracion de: {mat.getDuracionCap()} horas")
            
            
   def mostrarEmpleados(self, nombreCap):
      bandera = False
      for mat in self.__matriculas:
         if mat.getNombreCap() == nombreCap:
            bandera = True
            print(f"{mat.getNombreE()} realizo el programa de capacitacion")
      if bandera == False:
         print("No hay empleados que hayan realizado esta capacitacion o no existe")
         
         
   
   def existeEmpleado(self, empleado):
      i = 0
      while((i < len(self.__matriculas)) and (self.__matriculas[i].getEmpleado() != empleado)):
         i += 1
      if(i >= len(self.__matriculas)):
         i = -1
      return i