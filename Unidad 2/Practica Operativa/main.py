from moduloGestorClientes import gestorClientes
from moduloGestorMovimientos import gestorMovimientos

def main():
   clientes = gestorClientes()
   movimientos = gestorMovimientos()
   opcion = 1
   while opcion != 0:
      opcion = int(input("""\nMenu de opciones:
                         Opcion 1: Emitir listado de movimientos actualizado
                         Opcion 2: Informar si un cliente tuvo movimientos
                         Opcion 3: Ordenar movimientos por numero de cuenta
                         Opcion 0: Detener ejecucion
                         Ingrese una opcion: """))
      if opcion == 1:
         print("Si la opcion 3 no fue ejecutada anteriormente el resultado sera erroneo")
         dni = input("Ingrese el dni de la cuenta: ")
         clientes.emitirMovimientos(movimientos, dni)
      if opcion == 2:
         dni = input("Ingrese el dni de la cuenta: ")
         clientes.informarMovimientos(movimientos, dni)
      if opcion == 3:
         movimientos.ordenarMovimientos()
if __name__ == "__main__":
   main()