from moduloGestorConexiones import gestorConexiones
from moduloGestorGammers import gestorGammers

def main():
   gammers = gestorGammers()
   conexiones = gestorConexiones()
   opcion = -1
   while (opcion != 0):
      opcion= int(input("""Menu de opciones:
            Opcion 1: Emitir listado factura
            Opcion 2: Mostrar gammers para un juego
            Opcion 3: Mostrar conexiones repetidas
            Opcion 0: Detener ejecucion
            Ingrese una opcion: """))
      if opcion == 1:
         dni = input("Ingrese el dni del gammer: ")
         gammers.emitirListado(dni, conexiones)
      elif opcion == 2:
         juego = input("Ingrese el nombre del juego: ")
         conexiones.mostrarJugadores(juego, gammers)
      elif opcion == 3:
         conexiones.conexionesRepetidas(gammers)
      elif opcion == 0:
         print("Deteniendo ejecucion")


if __name__ == "__main__":
   main()