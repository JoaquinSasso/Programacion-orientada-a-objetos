from moduloClienteLocal import ClienteLocal
from moduloClienteNacional import ClienteNacional
from moduloNodo import nodo
class gestorClientes:
   __cabeza : nodo
   __tope : int
   
   def __init__(self):
      self.__cabeza = None
      self.__tope = 0
   
   def crearCliente(self):
      nombre = input("Ingrese el nombre del cliente: ")
      apellido = input("Ingrese el apellido del cliente: ")
      email = input("Ingrese el email del cliente: ")
      contraseña = input("Ingrese la contraseña del cliente: ")
      direccionPostal = input("Ingrese la direccion postal del cliente: ")
      telefono = input("Ingrese el telefono del cliente: ")
      tipo = " "
      while tipo not in ["n", "l"]:
         tipo = input("Ingrese L para local o N para nacional: ").lower()
      if tipo == "l":
         cliente = ClienteLocal(nombre, apellido, email, contraseña, direccionPostal, telefono)
      elif tipo == "n":
         provincia = input("Ingrese la provincia del cliente: ")
         localidad = input("Ingrese la localidad del cliente: ")
         codigoPostal = input("Ingrese el codigo postal del cliente: ")
         cliente = ClienteNacional(nombre, apellido, email, contraseña, direccionPostal, telefono, provincia, localidad, codigoPostal)
      self.agregarCliente(cliente)
   
   
   def agregarCliente(self, cliente):
      nuevoNodo =nodo(cliente)
      if self.__cabeza == None:
         self.__cabeza = nuevoNodo
         self.__actual = self.__cabeza
      else:
         actual = self.__cabeza
         while actual != None:
            anterior = actual
            actual = actual.getSig()
         anterior.setSig(nuevoNodo)
      self.__tope += 1
   
   def listarNacionales(self):
      actual = self.__cabeza
      while actual != None:
         cliente = actual.getDatos()
         if isinstance(cliente, ClienteNacional):
            print(cliente)
         actual = actual.getSig()
   
   def mostrarTipo(self, posicion):
      posicion -= 1
      if posicion < self.__tope and posicion >= 0:
         actual = self.__cabeza
         indice = 0
         while posicion != indice:
            actual = actual.getSig()
            indice += 1
         cliente = actual.getDatos()
         if isinstance(cliente, ClienteNacional):
            print("El cliente es nacional")
         else:
            print("El cliente es local")
      else:
         print("EL indice esta fuera de rango")