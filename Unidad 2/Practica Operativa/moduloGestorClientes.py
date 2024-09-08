import csv
from moduloCliente import cliente
from moduloGestorMovimientos import gestorMovimientos
class gestorClientes:
   __clientes : list
   
   
   def __init__(self):
      self.__clientes = []
      archivo = open("ClientesFarmaCiudad.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            nombre = fila[0]
            apellido = fila[1]
            dni = fila[2]
            numCuenta = int(fila[3])
            saldoAnterior = float(fila[4])
            nuevoCliente = cliente(nombre, apellido, dni, numCuenta, saldoAnterior)
            self.__clientes.append(nuevoCliente)
      archivo.close()
      
   
   def buscarCliente(self, dni):
      i = 0
      while((i < len(self.__clientes)) and (self.__clientes[i].getDni() != dni)):
         i += 1
      if i >= len(self.__clientes):
         i = -1
         print("No se encontro el cliente")
      return i
   
   
   def emitirMovimientos(self, gestorMovimientos, dni):
      i = self.buscarCliente(dni)
      if i != -1:
         print(f"\nCliente: {self.__clientes[i].getApellido()} {self.__clientes[i].getNombre()}               Numero de cuenta: {self.__clientes[i].getNro()}") 
         print(f"Saldo anterior: {self.__clientes[i].getSaldo()}") 
         importeTotal = gestorMovimientos.listarMovimientos(self.__clientes[i].getNro())
         saldoAnterior = self.__clientes[i].getSaldo()
         saldoActualizado = importeTotal + saldoAnterior
         print(f"Saldo actualizado: {saldoActualizado:0.2f}")
         self.__clientes[i].setSaldo(saldoActualizado) #Cada vez que se ejecuta este metodo se actualiza el saldo anterior, los resultados cambian en cada ejecucion
         
   
   def informarMovimientos(self, movimientos, dni):
      i = self.buscarCliente(dni)
      if i != -1:
         if movimientos.detectarMovimiento(self.__clientes[i].getNro()) == False:
            print(f"{self.__clientes[i].getApellido()} {self.__clientes[i].getNombre()} no tuvo movimientos durante Abril de 2024")
         else:
            print(f"{self.__clientes[i].getApellido()} {self.__clientes[i].getNombre()} tuvo al menos un movimiento durante Abril de 2024")
         