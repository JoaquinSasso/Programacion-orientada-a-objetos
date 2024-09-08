import sys
sys.dont_write_bytecode = True
from moduloGestorCalefactores import gestorCalefactores
from zope.interface import Interface
from interface import IArreglo
from moduloObjectEncoder import objectEncoder

def insertarElemento(interface : IArreglo):
   try:
         indice = int(input("Ingrese el indice"))
   except ValueError:
      print("EL valor debe ser un numero")
   else:
      if indice < 0:
         print("El indice se convertira en un numero positivo")
         indice *= -1
      interface.insertarElemento(indice)
      
def agregarCalefactor(interface : IArreglo):
   interface.agregarElemento()

def main():
   opcion = 1
   gestor = None
   encoder = objectEncoder()
   while opcion != 0:
      try:
         opcion = int(input("""Menu de opciones:
                            Opcion 1: Insertar un calefactor
                            Opcion 2: Agregar un calefactor
                            Opcion 3: Mostrar tipo de calefactor
                            Opcion 4: Mostrar calefactor a gas mas barato
                            Opcion 5: Mostrar todos los calefactores electricos de una marca
                            Opcion 6: Mostrar todos los calefactores en promocion
                            Opcion 7: Guardar los datos en un archivo JSON
                            Opcion 8: Cargar datos desde un archivo JSON
                            Opcion 9: Mostrar todos los calefactores
                            Opcion 0: Detener ejecucion
                            Ingrese una opcion: """))
      except ValueError:
         print("La opcion ingresada no es un numero")
      else:
         if opcion == 8:
            diccionario = encoder.cargarJSON()
            gestor= encoder.decodificarDiccionario(diccionario)
         else:
            if gestor == None:
               gestor = gestorCalefactores()
               print("Se inicializo el gestor vacio")
            if opcion == 1:
               insertarElemento(gestor)
            elif opcion == 2:
               agregarCalefactor(gestor)
            elif opcion == 3:
               indice = input("Ingrese el indice del calefactor: ")
               gestor.mostrarTipo(indice)
            elif opcion == 4:
               gestor.gasBarato()
            elif opcion == 5:
               marca = input("Ingrese la marca: ")
               gestor.mostrarMarca(marca)
            elif opcion == 6:
               gestor.mostrarPromociones()
            elif opcion == 7:
               d = gestor.toJSON()
               encoder.guardarJSON(d)
            elif opcion == 9:
               for calefactor in gestor:
                  print(calefactor)
            elif opcion == 0:
               print("Deteniendo la ejecucion...")
            if opcion not in [0,1,2,3,4,5,6,7,8,9]:
               print("La opcion ingresada es invalida")


if __name__ == "__main__":
   main()
   

"""Lote de prueba:
2
Samsung
SG-HeatPro 1
Corea del Sur
no
87654.12
1
E
2400
2
Samsung
SG-Warmer
Corea del Sur
si
98342.55
6
E
4000
2
Eskabe
S21 MX3 P
Argentina
si
146723.81
12
G
GN M 01-0406-06-104
3000
2
Longvie
Eca2s 2200
Argentina
no
146879.37
3
G
GN M 01-0406-11-765
2200
2
Peabody
PE-VC20RN
Argentina
si
99234.56
4
E
2000

"""