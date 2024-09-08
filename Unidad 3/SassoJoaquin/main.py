from moduloGestor import gestorProductos

def main():
   opcion = 1
   gestor = gestorProductos()
   while(opcion != 0):
      try:
         opcion = int(input("""Ingrese una opcion:
                           1) Agregar un producto
                           2) Mostrar tipo de producto en una posicion
                           3) Mostrar la cantidad de productos de cada tipo
                           4) Mostrar datos de todos los productos
                           0) Detener ejecucion
                           Ingrese una opcion: """))
      except ValueError:
         print("La opcion debe ser un numero")
      else:
         if opcion == 1:
            try:
               gestor.agregarProducto()
            except ValueError:
               print("El valor ingresado es invalido")
         elif opcion == 2:
            try:
               indice = int(input("Ingrese el indice: "))
               gestor.mostrarTipo(indice)
            except IndexError:
               print("El indice ingresado esta fuera de rango")
         elif opcion == 3:
            gestor.contarTipos()
         elif opcion == 4:
            gestor.mostrarDatos()
         elif opcion == 0:
            print("Deteniendo ejecucion...")


if __name__ == "__main__":
   main()
   
"""Lote de prueba
1
R
Queso cremoso
10/5/2024
15/7/2024
5
Argentina
ZM345
8300
AR-K934
1
C
Medallon de hamburgesa
23/4/2024
7/9/2024
-12.3
Brasil
BM-2132
8343
90
6
1
3
criogenico
"""