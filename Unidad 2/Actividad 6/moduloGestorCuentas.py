from moduloCuenta import cuenta
from moduloGestorTransacciones import gestorTransacciones
import numpy as np
import csv
class gestorCuentas:
   __cuentas = np.array([],dtype=cuenta)
      
   
   def __init__(self):
      archivo = open("cuentasBilletera.csv")
      datos = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in datos:
         if bandera == False:
            bandera = True
         else:
            cvu = int(fila[0])
            apellido = fila[1]
            nombre = fila[2]
            dni = int(fila[3])
            telefono = int(fila[4])
            saldo = float(fila[5])
            objeto = cuenta(cvu,apellido,nombre,dni,telefono,saldo)
            self.__cuentas = np.append(self.__cuentas, objeto)  
      archivo.close()
      
   def buscarCuenta(self, cvu):
      i = 0
      while((i < len(self.__cuentas) and (self.__cuentas[i].getCvu() != cvu))):
         i += 1
      if (i >= len(self.__cuentas)):
         i = -1
         print(f"No se encontro una cuenta con cvu: {cvu}")
      return i
   
   
   def mostrarDatos(self, cvu):
      i = self.buscarCuenta(cvu)
      if i != -1:
         print(f"""\nTitular: {self.__cuentas[i].getApellido()} {self.__cuentas[i].getNombre()}, DNI: {self.__cuentas[i].getDni()}
Telefono: {self.__cuentas[i].getTelefono()}        Saldo: ${self.__cuentas[i].getSaldo():0.2f}    Rendimientos: {self.__cuentas[i].getRendimiento()}%\n""")


   def actualizarRendimientos(self, rendimiento):
      cuenta.actualizarRendimiento(rendimiento)
      
      
   def otorgarRendimiento(self):
      for cuenta in self.__cuentas:
         rendimientoDiario = (cuenta.getRendimiento() / 365) / 100
         saldo = cuenta.getSaldo()
         gananciaDiaria = saldo * rendimientoDiario
         cuenta.actualizarSaldo(gananciaDiaria)
         rendimientoDiario = rendimientoDiario * 100
         print(f"El saldo de {cuenta.getNombre()} era de: {saldo:0.2f}, ganancia de {gananciaDiaria:0.2f} con un {rendimientoDiario:0.3f}% diario")
         
         
   
   def actualizarSaldo(self, cvu, transacciones):
      i = self.buscarCuenta(cvu)
      if i != -1:
         saldo = self.__cuentas[i].getSaldo()
         print(f"\nEl saldo actual de la cuenta es de: {saldo:0.2f}")
         importeTotal = transacciones.calcularImporte(cvu)
         saldo -= importeTotal
         print(f"El saldo actualizado es de: {saldo:0.2f}")
         self.__cuentas[i].setSaldo(saldo)
   
   
   def guardarCuentas(self):
      archivo = open("cuentasActualizadas.csv", mode="w", newline="")
      writer = csv.writer(archivo, delimiter=";")
      writer.writerow(["Cvu", "Apellido", "Nombre", "DNI", "Telefono", "Saldo"])
      for cuenta in self.__cuentas:
         arreglo = []
         arreglo.append(cuenta.getCvu())
         arreglo.append(cuenta.getApellido())
         arreglo.append(cuenta.getNombre())
         arreglo.append(cuenta.getDni())
         arreglo.append(cuenta.getTelefono())
         arreglo.append(cuenta.getSaldo())
         writer.writerow(arreglo)
      archivo.close()
      print("El archivo se guardo exitosamente")
      
   
   def liberar(self):
      print("Eliminando cuentas...")
      for cuenta in self.__cuentas:
         del cuenta