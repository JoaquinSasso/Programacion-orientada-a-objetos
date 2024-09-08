from moduloEmpleado import empleado
import csv
class gestorEmpleados:
   __empleados: list
   
   
   def __init__(self):
      self.__empleados = []
      archivo = open("Empleados.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            ide, nombre, puesto = fila
            nuevo = empleado(ide, nombre, puesto)
            self.__empleados.append(nuevo)
      archivo.close()
      
      
   def obtenerEmpleado(self, ide: int):
      i = 0
      while((i < len(self.__empleados)) and (self.__empleados[i].getId() != ide)):
         i += 1
      if i >= len(self.__empleados):
         retorno = None
         print("No se encontro al empleado")
      else:
         retorno = self.__empleados[i]
      return retorno
   
   def buscarEmpleado(self, ide):
      i = 0
      while((i < len(self.__empleados)) and (self.__empleados[i].getId() != ide)):
         i += 1
      if i >= len(self.__empleados):
         i = -1
         print("No se encontro al empleado")
      return i
   
   
   def empleadosSinMatricular(self, gestorM):
      bandera = False
      for empleado in self.__empleados:
         i = gestorM.existeEmpleado(empleado)
         if i == -1:
            print(f"El empleado: {empleado.getNombre()} no realizo ninguna capacitacion")
            bandera = True
      if bandera == False:
         print("Todos los empleados realizaron al menos una capacitacion")