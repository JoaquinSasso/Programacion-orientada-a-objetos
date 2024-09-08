from moduloCongelado import congelado
from moduloRefrigerado import refrigerado
import csv
class gestorProductos:
   __productos : list
   
   def __init__(self):
      self.__productos = []
      archivo = open("productos.csv")
      reader = csv.reader(archivo, delimiter=";")
      bandera = False
      for fila in reader:
         if bandera == False:
            bandera = True
         else:
            tipo = fila[0]
            nombre = fila[1]
            fechaEnvase = fila[2]
            fechaVencimiento = fila[3]
            temperatura = float(fila[4])
            paisOrigen = fila[5]
            nroLote = fila[6]
            costoBase = float(fila[7])
            if tipo == "C":
               nitro = fila[8]
               oxigeno = fila[9]
               dioxido = fila[10]
               vapor = fila[11]
               metodo = fila[12]
               producto = congelado(nombre, fechaEnvase, fechaVencimiento, temperatura, paisOrigen, nroLote, costoBase, nitro, oxigeno, dioxido, vapor, metodo)
            elif tipo == "R":
               codigoOrganismo = fila[8]
               producto = refrigerado(nombre, fechaEnvase, fechaVencimiento, temperatura, paisOrigen, nroLote, costoBase, codigoOrganismo)
            self.__productos.append(producto)
   
   def agregarProducto(self):
      tipo = input("""Ingrese el tipo de producto:
                   C: Congelado
                   R: Refrigerado
                   Ingrese una opcion: """)
      nombre = input("Ingrese el nombre del producto: ")
      print("Ingrese las fechas con formato DD/MM/AAAA")
      fechaEnvase = input("Ingrese la fecha de envase  del producto: ")
      fechaVencimiento = input("Ingrese la fecha de vencimiento del producto: ")
      temperatura = float(input("Ingrese la temperatura de mantenimiento del producto: "))
      paisOrigen = input("Ingrese el pais de origen del producto: ")
      numeroLote = input("Ingrese el numero de lote del producto: ")
      costoBase = float(input("Ingrese el costo base del producto: "))
      tipo = tipo.upper()
      if tipo == "C":
         nitrogeno = input("Ingrese el porcentaje de nitrogeno en la composicion: ")
         oxigeno = input("Ingrese el porcentaje de oxigeno en la composicion: ")
         dioxido = input("Ingrese el porcentaje de dioxido de carbono en la composicion: ")
         vapor = input("Ingrese el porcentaje de vapor en la composicion: ")
         metodo = input("Ingrese el metodo de congelamiento (mecanico o criogenico): ")
         metodo = metodo.lower()
         if((metodo != "criogenico") and (metodo != "mecanico")):
            raise ValueError
         producto = congelado(nombre, fechaEnvase, fechaVencimiento, temperatura, paisOrigen, numeroLote, costoBase, nitrogeno, oxigeno, dioxido, vapor, metodo)
         self.__productos.append(producto)
      elif tipo == "R":
         codigoOrganismo = input("Ingrese el codigo del organismo de supervicion: ")
         producto = refrigerado(nombre, fechaEnvase, fechaVencimiento, temperatura, paisOrigen, numeroLote, costoBase, codigoOrganismo)
         self.__productos.append(producto)
      else:
         print("No se pueden cargar productos de ese tipo")
      
      
   def mostrarTipo(self, indice):
      if isinstance(self.__productos[indice], congelado):
         print("El producto es un congelado")
      elif isinstance(self.__productos[indice], refrigerado): 
         print("El producto es un refrigerado")
         
   
   def contarTipos(self):
      refri = 0
      conge = 0
      for producto in self.__productos:
         if isinstance(producto, congelado):
            conge += 1
         elif isinstance(producto, refrigerado):
            refri += 1
      print(f"Hay {conge} productos congelados y {refri} refrigerados")
      
      
   def mostrarDatos(self):
      for producto in self.__productos:
         print()
         print(producto)