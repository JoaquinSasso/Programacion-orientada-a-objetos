from cajaDeAhorro import cajaDeAhorro

def test():
   nro: str
   cuil: str
   apellido: str
   nombre: str
   saldo: float
   importe: float
   nro = input("Ingrese el nro de la caja de ahorro: ")
   apellido = input("Ingrese el apellido del cliente: ")
   nombre = input("Ingrese el nombre del cliente: ")
   saldo = float(input("Ingrese el saldo de la caja de ahorro: "))
   cuil = input("Ingrese el cuil del cliente: ")
   objeto = cajaDeAhorro(nro,cuil,apellido, nombre, saldo)
   objeto.mostrarDatos()
   importe = float(input("Ingrese el importe que desea extraer: "))
   saldoRestante = objeto.extraer(importe)
   if saldoRestante >= 0:
      print(f"La operacion fue exitosa, el saldo restante es de: {saldoRestante}")
   else:
      print(f"No se pudo realizar la operacion, se requieren ${saldoRestante} pesos")
   importe= float(input("Ingrese el importe que desea depositar: "))
   objeto.depositar(importe)
   objeto.validarCUIL()

def main():
   for i in range(1):
      test()
if(__name__ == "__main__"):
   main()

''''Lote de prueba
2734283
Vilches
Valentin
236547.65
20-45635995-4
76453.34
'''