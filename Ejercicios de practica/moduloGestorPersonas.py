from moduloNodo import nodo
from moduloPersona import Persona
from moduloAntecendete import Antecedente
from zope.interface import implementer
from moduloInterface import InterfacePolicia
from moduloPoliciaForense import Policia, Forense, PoliciaForense

@implementer(InterfacePolicia)
class gestorPersonas:
   __cabeza : nodo
   __actual : nodo
   __indice : int
   __tope : int
   
   def __init__(self):
      self.__cabeza = None
      self.__tope = 0
      self.__indice = 0
      self.__actual = None
   
   def agregarPersona(self, nuevaPersona : Persona):
      nuevo = nodo(nuevaPersona, self.__cabeza)
      self.__cabeza = nuevo
      self.__actual = self.__cabeza
      self.__tope += 1
   
   def insertarPersona(self, nuevo: nodo, indice):
      if (indice-1) >= self.__tope:
         print("El indice esta fuera de rango")
      elif indice-1 == 0:
         self.agregarPersona(nuevo)
      else:
         i = 0
         actual = self.__cabeza
         while(i < indice-1):
            anterior = actual
            actual = actual.getSig()
         anterior.setSig(nuevo)
         nuevo.setSig(actual)
         self.__tope += 1
   
   def crearPersona(self):
      nombre = input("Ingrese el nombre: ")
      apellido = input("Ingrese el apellido: ")
      dni = input("Ingrese el DNI: ")
      nacimiento = input("Ingrese la fecha de nacimiento: ")
      nuevaPersona = Persona(None,None,None,None,nombre,apellido,nacimiento,dni)
      self.agregarPersona(nuevaPersona)

   def buscarPersona(self, dni) -> Persona:
      i = 0
      dato = None
      actual = self.__cabeza
      while ((i < self.__tope) and (actual.getDatos().getDNI() != dni)):
         actual = actual.getSig()
         i += 1
      if i >= self.__tope:
         print("No se encontro la persona")
      else: 
         dato = actual.getDatos()
      return dato
   
   def __iter__(self):
      return self
   
   def __next__(self):
      if self.__indice == self.__tope:
         self.__actual = self.__cabeza
         self.__indice = 0
         raise StopIteration
      else:
         self.__indice += 1
         dato = self.__actual.getDatos()
         self.__actual = self.__actual.getSig()
         return dato
   
   def crearAntecedente(self, dni):
      persona = self.buscarPersona(dni)
      if persona != None:
         nro = int(input("Ingrese el numero de antecedente: "))
         motivo = input("Ingrese el motivo del antecedente: ")
         fecha = input("Ingrese la fecha del antecedente: ")
         multa = float(input("Ingrese la multa del antecedente: "))
         condena = None
         while(condena == None):
            condena = input("Ingrese si cumplio cadena (si o no): ").lower()
            if condena == "si":
               condena = True
            elif condena == "no":
               condena = False
            else: 
               print("La respuesta debe ser si o no")
         antecedente = Antecedente(nro, motivo, fecha, multa, condena)
         persona.agregarAntecedente(antecedente)
   
   def agregarAntecedente(self, dni, antecedente : Antecedente):
      persona = self.buscarPersona(dni)
      if persona != None:
         persona.agregarAntecedente(antecedente)
   
   def listarAntecedentes(self, dni):
      persona = self.buscarPersona(dni)
      persona.listarAntecedentes()
          
          
   def listarPersonas(self):
      for p in self:
         print(p)
   
   def buscarPorAntecedente(self, motivo):
      for p in self:
         if p.buscarAntecedenteMotivo(motivo) != -1:
            print(p)

   def toJSON(self):
      lista = []
      for p in self:
         lista.append(p.toJSON())
      d = dict(
         clase = self.__class__.__name__,
         datos = lista
      )
      return d
   
   def crearAgente(self):
      nombre = input("Ingrese el nombre: ")
      apellido = input("Ingrese el apellido: ")
      dni = input("Ingrese el DNI: ")
      nacimiento = input("Ingrese la fecha de nacimiento: ")
      bandera = False
      while bandera == False:
         tipo = input("Ingrese el tipo (p = policia, f= forense, pf= policia forense): ").lower()
         cargo = ""
         if tipo == "p":
            while cargo not in ["oficial", "teniente", "capitan"]:
               cargo = input("Ingrese el cargo(oficial, teniente, capitan): ").lower()
            placa = input("Ingrese la placa: ")
            password = input("Ingrese el password: ")
            nuevo = Policia(None, cargo, placa, password, nombre, apellido, nacimiento, dni)
            bandera = True
         elif tipo == "f":
            ide = input("Ingrese la identificacion: ")
            nuevo = Forense(ide, None, None, None, nombre, apellido, nacimiento, dni)
            bandera = True
         elif tipo == "pf":
            while cargo not in ["oficial", "teniente", "capitan"]:
               cargo = input("Ingrese el cargo(oficial, teniente, capitan): ").lower()
            placa = input("Ingrese la placa: ")
            password = input("Ingrese el password: ")
            ide = input("Ingrese la identificacion: ")
            caso = input("Ingrese el caso en el que trabaja: ")
            nuevo = PoliciaForense(caso, ide, cargo, placa, password, nombre, apellido, nacimiento, dni)
            bandera = True
      self.agregarPersona(nuevo)
      
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
      for p in self:
         if isinstance(p, Policia) or isinstance(p, Forense):
            print(p)