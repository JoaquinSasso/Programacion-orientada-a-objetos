from moduloGestorClientes import gestorClientes
from moduloClienteLocal import ClienteLocal
from moduloClienteNacional import ClienteNacional

def main():
   gestor = gestorClientes()
   
   opcion = -1
   while opcion != 0:
      opcion = int(input("""\nMenu de opciones:
                         1) Agregar un cliente
                         2) Mostrar nombre y provincia de los clientes nacionales
                         3) Indicar el tipo de cliente de una posicion
                         4) Cargar clientes de prueba
                         0) Detener ejecucion
                         Ingrese una opcion: """))
      if opcion == 1:
         gestor.crearCliente()
      elif opcion == 2:
         gestor.listarNacionales()
      elif opcion == 3:
         posicion = int(input("Ingrese la posicion: "))
         gestor.mostrarTipo(posicion)
      elif opcion == 4:
         cliente = ClienteLocal("Joaquin", "Sasso", "joasasso@gmail.com", "1234", "Av. Ignacio de la Roza 120 Oeste", "2645288667")
         gestor.agregarCliente(cliente)
         cliente = ClienteNacional("Monica", "Vargas", "mevargas@outlook.com", "monica", "Italia 992", "2302348675", "Cordoba", "Villa Allende", "3650")
         gestor.agregarCliente(cliente)
         cliente = ClienteLocal("Ana", "Rodriguez", "anarodriguez@yahoo.com.ar", "contraseñasegura", "Meglioli 560 Sur", "2648875031")
         gestor.agregarCliente(cliente)
         cliente = ClienteNacional("Maria", "Sanchez", "mariasanchez@hotmail.com", "pass", "9 de Julio 980", "1503324541", "CABA", "Recoleta", "2100")
         gestor.agregarCliente(cliente)
      elif opcion == 0:
         print("Deteniendo ejecucion...")

if __name__ == "__main__":
   main()

"""Bloque de prueba
1
Raul
Castelli
raulcastelli@gmail.com
rauuul
Las Heras 1283
2637709321
N
Mendoza
Maipu
5300
"""