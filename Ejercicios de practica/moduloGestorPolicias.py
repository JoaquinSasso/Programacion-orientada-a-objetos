from moduloPolicia import Policia
from moduloPoliciaForense import PoliciaForense
from moduloForense import Forense
from moduloPersona import Persona
from moduloGestorPersonas import gestorPersonas
import csv

class gestorPolicias:
   __lista : list[Persona]
   __gestorPersonas : gestorPersonas
   
   def __init__(self, gestor):
      self.__lista = []
      self.__gestorPersonas = gestor
   
   def buscarPolicia(self, dni):
      i = 0
      while((i < len(self.__lista)) and (self.__lista[i].getDNI() != dni)):
         i += 1
      if i >= len(self.__lista):
         print("No se encontro al agente")
         i = -1
      return i
   
   def crearAgente(self):
      nombre = input("Ingrese el nombre: ")
      apellido = input("Ingrese el apellido: ")
      dni = input("Ingrese el DNI: ")
      nacimiento = input("Ingrese la fecha de nacimiento: ")
      nuevaPersona = Persona(nombre, apellido, nacimiento, dni)
      bandera = False
      while bandera == False:
         tipo = input("Ingrese el tipo (p = policia, f= forense, pf= policia forense): ").lower()
         if tipo == "p":
            cargo = input("Ingrese el cargo(oficial, teniente, capitan): ").lower()
            placa = input("Ingrese el placa: ")
            password = input("Ingrese el password: ")
            if cargo in ["oficial", "teniente", "capitan"]:
               nuevo = Policia(None, cargo, placa, password, nombre, apellido, nacimiento, dni)
               bandera = True
         elif tipo == "f":
            ide = input("Ingrese la identificacion: ")
            nuevo = Forense(ide, None, None, None, nombre, apellido, nacimiento, dni)
            bandera = True
         elif tipo == "pf":
            cargo = input("Ingrese el cargo(oficial, teniente, capitan): ").lower()
            placa = input("Ingrese el placa: ")
            password = input("Ingrese el password: ")
            ide = input("Ingrese la identificacion: ")
            caso = input("Ingrese el caso en el que trabaja: ")
            nuevo = PoliciaForense(caso, ide, cargo, placa, password, nombre, apellido, nacimiento, dni)
            bandera = True
      self.agregarAgente(nuevo, nuevaPersona)

   def agregarAgente(self, nuevo, nuevaPersona):
      self.__lista.append(nuevo)
      self.__gestorPersonas.agregarPersona(nuevaPersona)
      
   def validarCuenta(self, dni, password):
      i = self.buscarPolicia(dni)
      nivel = 0
      if i != -1:
         agente = self.__lista[i]
         if isinstance(agente, Policia):
            if password == agente.getPassword():
               if agente.getCargo() == "oficial":
                  nivel = 1
               elif agente.getCargo() == "teniente":
                  nivel = 2
               elif agente.getCargo() == "capitan":
                  nivel = 3
         else:
            print("El dni ingresado no es de un policia")
      return nivel

   def listarAgentes(self):
      for a in self.__lista:
         print(a)

   def guardarCSV(self):
      try:
         archivo = open("policias.csv", mode="w")
      except Exception as e:
         print(f"Hubo un error al guardar el archivo: {e}")
      writer = csv.writer(archivo, delimiter=";")
      for a in self.__lista:
         dni = a.getDNI()
         if isinstance(a, PoliciaForense):
            identificador = a.getIde()
            cargo = a.getCargo()
            placa = a.getPlaca()
            password = a.getPassword()
            caso = a.getCaso()
            writer.writerow([dni, identificador, cargo, placa, password, caso])
         elif isinstance(a, Policia):
            cargo = a.getCargo()
            placa = a.getPlaca()
            password = a.getPassword()
            writer.writerow([dni, cargo, placa, password])
         elif isinstance(a, Forense):
            identificador = a.getIde()
            writer.writerow([dni, identificador])
      archivo.close()
      print("El archivo se guardo exitosamente")