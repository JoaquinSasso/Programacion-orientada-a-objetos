from moduloTransaccion import transaccion
import csv
class gestorTransacciones:
   __transcacciones = []
   
   
   def __init__(self):
      archivo = open("transaccionesBilletera.csv")
      datos = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in datos:
         if bandera == False:
            bandera = True
         else:
            cvu = int(fila[0])
            nro = int(fila[1])
            importe = float(fila[2])
            tipo = fila[3]
            objeto = transaccion(cvu, nro, importe, tipo)
            self.__transcacciones.append(objeto)
      archivo.close()
   
   
   def calcularImporte(self, cvu):
      total = 0
      for operacion in self.__transcacciones:
         if operacion.getCvu() == cvu:
            total += operacion.getImporte()
      return total
   
   def liberar(self):
      print("Eliminando transacciones...")
      for operacion in self.__transcacciones:
         del operacion