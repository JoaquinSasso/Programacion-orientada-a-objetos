from moduloGestorPersonas import gestorPersonas
from interface import IArreglo

def insertarElemento(interface : IArreglo):
   indice = input("Ingrese el indice donde desea ingresar una nueva persona: ")
   interface.insertarElemento(indice)

def agregarElemento(interface: IArreglo):
   interface.agregarElemento()

def mostrarElemento(interface: IArreglo):
   indice = input("Ingrese el indice de la persona: ")
   interface.mostrarElemento(indice)
def main():
   gestorP = gestorPersonas()
   opcion = -1
   manejarGestor : IArreglo
   while opcion != 0:
      try:
         opcion = int(input("""Menu de opciones:
                           Opcion 1: Insertar elemento
                           Opcion 2: Agregar elemento
                           Opcion 3: Mostrar elemento
                           Opcion 4: Mostrar todos los elementos
                           Opcion 0: Detener ejecucion
                           Ingrese una opcion: """))
      except ValueError:
         print("La opcion debe ser un numero")
      else:
         if opcion in [0,1,2,3,4]:
            if opcion == 1:
               insertarElemento(gestorP)
            
            if opcion == 2:
               agregarElemento(gestorP)
            
            if opcion == 3:
               mostrarElemento(gestorP)
            
            if opcion == 4:
               gestorP.mostrarTodos()
         else:
            print("La opcion ingresada es incorrecta")

if __name__ == "__main__":
   main()