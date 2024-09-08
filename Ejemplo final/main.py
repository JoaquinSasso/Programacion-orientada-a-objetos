from moduloGestor import Gestor

def main():
   gestor = Gestor()
   opcion = -1
   while opcion != 0:
      opcion = int(input("""\nMenu de opciones:
                         1) Mostrar polimorfismo
                         2) Mostrar sobre carga de operadores
                         0) Detener ejecucion
                         Ingrese una opcion: """))
      if opcion == 1:
         gestor.mostrarPolimorfismo()
         
      elif opcion == 2:
         gestor.mostrarSobrecarga()
         
      elif opcion == 0:
         print("Deteniendo ejecucion...")
   
if __name__ == "__main__":
   main()