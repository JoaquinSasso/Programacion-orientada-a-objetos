from moduloGestorEdificios import gestorEdificios
def main():
   gestor = gestorEdificios()
   opcion = 1
   while(opcion != 0):
      opcion = int(input("""Menu de opciones (0 para detener):
                              Opcion 1: Mostrar propietarios
                              Opcion 2: Mostrar superficie de un edificio
                              Opcion 3: Calcular porcentaje de superficie
                              Opcion 4: Contar departamentos con 3 habitaciones y mas de un baño
                              Ingrese la opcion: """))
      if opcion == 1:
         nombreEdificio = input("Ingrese el nombre del edificio: ")
         gestor.mostrarPropietarios(nombreEdificio)
      elif opcion == 2:
         nombreEdificio = input("Ingrese el nombre del edificio: ")
         gestor.mostrarSuperficie(nombreEdificio)
      elif opcion == 3:
         nombrePropietario = input("Ingrese el nombre del propietario: ")
         gestor.porcentajeSuperficie(nombrePropietario)        
      elif opcion == 4:
         nombreEdificio = input("Ingrese el nombre del edificio: ")
         piso = int(input("Ingrese el piso del edificio: "))
         gestor.contarDepartamentosLujosos(nombreEdificio, piso)

if __name__ == "__main__":
   main()