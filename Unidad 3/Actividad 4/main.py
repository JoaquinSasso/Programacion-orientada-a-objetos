from moduloGestorPublicaciones import gestorPublicaciones
def main():
   gestorP = gestorPublicaciones()
   #gestorP.test()
   opcion = 1
   while opcion != 0:
      try:
         opcion = int(input("""Menu de opciones
                           Opcion 1: Agregar una publicacion
                           Opcion 2: Mostrar tipo de publicacion
                           Opcion 3: Mostrar la cantidad de publicaciones de cada tipo
                           Opcion 4: Mostrar todas las publicaciones
                           Opcion 0: Detener la ejecucion: """))
      except ValueError:
         print("No se ingreso un numero")
         opcion = 5
      if opcion in [0,1,2,3,4]:
         if opcion == 1:
            gestorP.agregarPublicacion()
         elif opcion == 2:
            try:
               i = int(input("Ingrese el indice de la lista: "))
            except ValueError:
               print("No se ingreso un numero entero")
            else:
               gestorP.mostrarTipo(i)
         elif opcion == 3:
            gestorP.contarTipo()
         elif opcion == 4:
            gestorP.mostrarPublicaciones()
      else:
         print("La opcion ingresada no es valida")
   
if __name__ == "__main__":
   main()
   
"""Lote de prueba
Python para principiantes
Educativo
46335,765
L
Jordan Smith
1650
2017
"""