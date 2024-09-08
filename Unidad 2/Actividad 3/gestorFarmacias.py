import numpy as np

class gestorFarmacias:
   np.random.seed(40)
   __facturaciones = np.random.rand(5,7) * 3500
   def mostrarMatriz(self):
      print(self.__facturaciones)
   def agregarFactura(self, dia, farmacia, importe):
      self.__facturaciones[farmacia-1, dia-1] += importe
   def calcularTotalSucursal(self, farmacia):
      total = 0
      for dia in self.__facturaciones[farmacia-1]:
         total += dia
      print(f"El total de facturacion de la sucursal {farmacia} fue de: {total:0.2f}")
   # def buscarMaximo(self):
   #    maximo = 0
   #    totalActual = 0
   #    maxSucursal = 0
   #    fila = 1
   #    for sucursal in self.__facturaciones:
   #       for dia in sucursal:
   #          totalActual += dia
   #       if totalActual > maximo:
   #          maximo = totalActual
   #          maxSucursal = fila
   #       totalActual = 0   
   #       fila += 1
   #    print(f"La sucursal con mayor recaudacion semanal fue: {maxSucursal}")
   def buscarMin(self):
      minSucursal = np.argmin(np.sum(self.__facturaciones, axis=1))+1
      print(f"La sucursal con menor recaudacion semanal fue: {minSucursal}")
   def buscarMaximoEnDia(self, dia):
      maxSucursal = np.argmax(self.__facturaciones[:, dia-1]) + 1
      print(f"La sucursal con mayor recaudacion diaria fue: {maxSucursal}")
   def calcularTotal(self):
      print(f"El total recaudado entre todas las sucursales en la semana es de: {np.sum(np.sum(self.__facturaciones, axis = 1)):0.2f}")