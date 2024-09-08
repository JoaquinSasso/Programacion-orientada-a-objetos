from moduloGestorCuentas import gestorCuentas
from moduloGestorTransacciones import gestorTransacciones
def main():
   cuentas = gestorCuentas()
   transacciones = gestorTransacciones()
   opcion = 1
   while opcion > 0:
      opcion = int(input("""\nOpcion 1: Mostrar datos de un cliente
Opcion 2: Actualizar porcentaje anual de rendimiento
Opcion 3: Otorgar rendimientos diarios
Opcion 4: Aplicar transacciones pendientes
Opcion 5: Almacenar datos y detener ejecución
Opcion 0: Detener ejecución
         Ingrese la opcion deseada: """))
      if opcion == 1:
         cvu = int(input("Ingrese el CVU de la cuenta: "))
         cuentas.mostrarDatos(cvu)
      elif opcion == 2:
         rendimiento = float(input("Ingrese el nuevo rendimiento anual: "))
         cuentas.actualizarRendimientos(rendimiento)
      elif opcion == 3:
         cuentas.otorgarRendimiento()
      elif opcion == 4:
         cvu = int(input("Ingrese el CVU de la cuenta: "))
         cuentas.actualizarSaldo(cvu, transacciones)
      elif opcion == 5:
         cuentas.guardarCuentas()
         cuentas.liberar()
         transacciones.liberar()
         print("Borrando gestores...")
         del cuentas
         del transacciones
         opcion = 0
      else:
         if not(opcion in [0,1,2,3,4,5]):
            print("La opcion ingresada es incorrecta")
      
if __name__ == "__main__":
   main()