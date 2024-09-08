from moduloGestorCapacitaciones import gestorCapacitaciones
from moduloGestorEmpleados import gestorEmpleados
from moduloGestorMatriculas import gestorMatriculas
def main():
   opcion = 3
   empleados = gestorEmpleados()
   capacitaciones = gestorCapacitaciones()
   matriculas = gestorMatriculas(empleados, capacitaciones)
   while opcion != 0:
      opcion = int(input("""Ingrese la opcion que desee:
                         Opcion 1: Listar las capacitaciones de un empleado
                         Opcion 2: Mostrar los empleados matriculados a una capacitacion
                         Opcion 3: Mostrar empleados que no hayan realizado capacitaciones
                         Opcion 0: Detener ejecucion
                         Ingrese la opcion: """))
      if opcion in [0,1,2,3]:
         if opcion == 1:
            ide = int(input("Ingrese el id del empleado: "))
            matriculas.mostrarCapacitaciones(ide)
         if opcion == 2:
            capacitacion = input("Ingrese el nombre del programa de capacitacion: ")
            matriculas.mostrarEmpleados(capacitacion)
         if opcion == 3:
            empleados.empleadosSinMatricular(matriculas)
      else: print("La opcion es incorrecta")



if __name__ == "__main__":
   main()