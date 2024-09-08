import numpy as np
#Se importa la libreria numpy con el alias np
from clasePerro import perro as p

def main():
   perros = np.empty(4,  dtype= p) 
   #Se crea el arreglo y se inicializan los perro con los valores siguientes
   perros[0] = p("Coda",3)
   perros[1] = p("Firu",5)
   perros[2] = p("Tobi",7)
   perros[3] = p("Pelusa",1)
   perrosViejos = perros[perros > 4] #Se genera un subarreglo con los perros cuya edad es mayor a 4
   for perro in perrosViejos: #Se itera por todo el arreglo de perros para mostrar sus datos
      print(f"Nombre: {perro.getNombre()}, edad: {perro.getEdad()}")

if __name__ == "__main__":
   main()                       