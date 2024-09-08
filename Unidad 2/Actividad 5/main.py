from moduloGestorEquipos import gestorEquipos
from moduloGestorFechas import gestorFechas
def main():
   fechas : gestorFechas
   equipos : gestorEquipos
   opcion = 1
   while opcion > 0:
      opcion = int(input("""Inserte la opcion del menu:
                              1. Leer el archivo equipos2024.csv y cargarlo al gestor de equipos
                              2. Leer el archivo fechasFutbol.csv y cargarlo al gestor de fechas
                              3. Listar los datos de un equipo
                              4. Actualizar la tabla con las fechas disputadas (Esta funcion podria desordenar la tabla)
                              5. Ordenar la tabla segun el puntaje de los equipos
                              6. Almacenar la tabla de posiciones en un archivo .csv
                              7. Mostrar tabla
                              Ingrese una opcion (0 para detener): """))
      if opcion == 1:
         equipos = gestorEquipos()
      if opcion == 2:
         fechas = gestorFechas()
      if opcion == 3:
         id = int(input("Ingrese el identificador del equipo: "))
         equipos.listarFechas(fechas, id)
      if opcion == 4:
         equipos.actualizarTablas(fechas)
         print("La tabla fue actualizada correctamente")
      if opcion == 5:
         equipos.ordenarPorPuntaje()
         print("La tabla fue ordenada correctamente")
      if opcion == 6:
         equipos.guardarTabla()
      if opcion == 7:
         equipos.mostrarTabla()
      if opcion == 8:
         equipos.liberar()
         fechas.liberar()
         del equipos
         del fechas         
   

if __name__ == "__main__":
   main()