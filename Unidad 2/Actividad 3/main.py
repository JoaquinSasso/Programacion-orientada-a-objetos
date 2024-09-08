from gestorFarmacias import gestorFarmacias
def main():
   opcion = 5
   gestor = gestorFarmacias()
   gestor.mostrarMatriz()
   while opcion > 0:
      print("""Menú de opciones:
            Opcion 1: Cargar una factura
            Opcion 2: Calcular la facturacion total de una sucursal
            Opcion 3: Buscar farmacia con mayor facturacion para un dia
            Opcion 4: Buscar la farmacia con la menor facturacion en la semana
            Opcion 5: Calcular el total facturado entre todas las sucursales en la semana
            Opcion 0: Detener la ejecucion""")
      opcion = int(input("Ingrese la opcion: "))
      if opcion == 1:
         farmacia = int(input("Ingrese numero de sucursal: "))
         dia = int(input("Ingrese el dia: "))
         importe = float(input("Ingrese el importe de la factura: "))
         gestor.agregarFactura(dia, farmacia, importe)
      elif opcion == 2:
         farmacia = int(input("Ingrese numero de sucursal: "))
         gestor.calcularTotalSucursal(farmacia)
      elif opcion == 3:
         dia = int(input("Ingrese el dia: "))
         gestor.buscarMaximoEnDia(dia)
      elif opcion == 4:
         gestor.buscarMin()
      elif opcion == 5:
         gestor.calcularTotal()
         
if __name__ == "__main__":
   main()