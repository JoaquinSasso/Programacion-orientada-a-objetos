from moduloAudio import cd
from moduloLibro import libro
import csv

class gestorPublicaciones:
   __publicaciones: list
   
   def __init__(self):
      self.__publicaciones = []
      try:
         archivo = open("publicaciones.csv")
         reader = csv.reader(archivo, delimiter=";")
      except FileNotFoundError:
         print("No se encontro el archivo en la ruta indicada")
      else:
         bandera = False
         for fila in reader:
            if bandera == False:
               bandera = True
            else:
               titulo = fila[0]
               categoria = fila[1]
               precio = float(fila[2])
               tipo = fila[3]
               if tipo == "A":
                  narrador = fila[4]
                  duracion = int(fila[5])
                  objeto = cd(titulo, categoria, precio, duracion, narrador)
               elif tipo == "L":
                  autor = fila[4]
                  paginas = int(fila[5])
                  fecha = int(fila[6])
                  objeto = libro(autor, fecha, paginas, titulo, categoria, precio)
               if tipo in ["L", "A"]:
                  self.__publicaciones.append(objeto)
         archivo.close()
   
   
   def agregarPublicacion(self):
      titulo = input("Ingrese el titulo: ")
      categoria = input("Ingrese la categoria: ")
      precio = input("Ingrese el precio base: ")
      precio = precio.replace(",", ".")
      try:
         precio = float(precio)
      except ValueError:
         print("El valor ingresado no era un numero")
         precio = input("Ingrese el precio base: ")
         precio = precio.replace(",", ".")
         precio = float(precio)
      tipo = input("""A para Audiolibro
L para Libro
Ingrese la opcion: """)
      tipo = tipo.upper()
      if tipo == "A":
         narrador = input("Ingrese el nombre del narrador: ")
         duracion = int(input("Ingrese la duracion en minutos: "))
         objeto = cd(titulo,categoria,precio,narrador,duracion)
         self.__publicaciones.append(objeto)
      elif tipo == "L":
         autor = input("Ingrese el nombre del autor: ")
         try:
            paginas = int(input("Ingrese la cantidad de paginas: "))
         except ValueError:
            print("El valor ingresado no era un numero entero")
            paginas = int(input("Ingrese la cantidad de pagina: "))
         try:
            fecha = int(input("Ingrese el año de lanzamiento: "))
         except ValueError:
            print("El valor ingresado no era un numero entero")
            fecha = int(input("Ingrese el año de lanzamiento: "))
         objeto = libro(autor, fecha, paginas, titulo, categoria, precio)
         self.__publicaciones.append(objeto)
      else:
         print("El tipo de publicacion ingresado no es valido")
         
         
   
   def mostrarPublicaciones(self):
      for publicacion in self.__publicaciones:
         print(publicacion)
         
   def mostrarTipo(self, i):
      try:
         if isinstance(self.__publicaciones[i], libro):
            print("La publicacion es un libro")
         elif isinstance(self.__publicaciones[i], cd):
            print("La publicacion es un audiolibro")
      except IndexError:
         print(f"El indice ingresado esta fuera de rango, ingresa un indice entre 0 y {(len(self.__publicaciones))-1}")
   
         
   def contarTipo(self):
      libros = 0
      audiolibros = 0
      for publicacion in self.__publicaciones:
         if isinstance(publicacion, libro):
            libros += 1
         elif isinstance(publicacion, cd):
            audiolibros += 1
      print(f"Hay {libros} libros y {audiolibros} audiolibros")