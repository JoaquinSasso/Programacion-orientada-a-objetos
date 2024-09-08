from controladorCajas import controlador
from cajaDeAhorro import cajaDeAhorro

def main():
   gestor = controlador()
   gestor.crearCaja()
   gestor.crearCaja()
   gestor.crearCaja()
   gestor.mostrarCajas()
   cuilIngresado = input("Ingrese el cuil de la caja que desea buscar")
   apellido, nombre, saldo = gestor.obtenerDatos(cuilIngresado)
   print(f"La cuenta que busca esta a nombre de: {apellido} {nombre} y tiene un saldo de: {saldo}")

if __name__ == "__main__":
   main()
   
""""Lote de prueba
1
Sasso
Joaquin
186729
20-44991289-7
2
Reta
German
27346
20-44785986-4
3
Reynoso
Nicolas
123124
23-23732432-1
"""