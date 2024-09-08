from gestorherra import gestorherra
def main():
   opcion = 1
   gestor = gestorherra()
   gestor.carga()
   while(opcion != 0):
      opcion = int(input("""\nIngrese la opcion:
                         1) Mostrar el tipo de un equipo
                         2) Mostrar todos las maquinas electricas fabricadas en una año
                         3) Mostrar todas las maquinas pesadas con capacidad menor a la ingresada
                         4) Mostrar datos de todos los equipos
                         0) Detener
                         Ingrese una opcion: """))
      if opcion == 1:
         try:
            indice = int(input("Ingrese el indice: "))
            gestor.inciso1(indice)
         except ValueError:
            print("El indice debe ser un numero")
         except IndexError:
            print("Indice fuera de rango")
      elif opcion == 2:
         anio = input("Ingrese el año de fabricacion: ")
         gestor.inciso2(anio)
      elif opcion == 3:
         capa = int(input('Ingrese la capacidad de carga: '))
         gestor.inciso3(capa)
      elif opcion == 4:
         gestor.inciso4()



if __name__ == "__main__":
   main()