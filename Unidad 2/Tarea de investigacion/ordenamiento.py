import numpy as np
#Se importa la libreria numpy con el alias np
from clasePerro import perro as p

def main():
   perros = np.empty(4,  dtype= p)
   #Se inicializan los perro con los valores siguientes
   perros[0] = p("Coda",3)
   perros[1] = p("Firu",5)
   perros[2] = p("Tobi",7)
   perros[3] = p("Pelusa",1)
   #Utilizamos la funcion sort para ordenar el arreglo de perros
   perros.sort()
   #Iteramos por todo el arreglo de perros para mostrar sus datos
   for perro in perros:
      print(f"Nombre: {perro.getNombre()}, edad: {perro.getEdad()}")
   total = np.sum(perros[0].getEdad())
   print(total)
   
if __name__ == "__main__":
   main()                       