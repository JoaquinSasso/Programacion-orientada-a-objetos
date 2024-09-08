"""Registro civil de la policia
Las personas y los antecedentes deben poder cargarse desde personas.json
Los policias se cargan mediante policias.csv filtrar por dni
Se desea registrar personas y los antecedentes penales de cada una
De cada persona se registra: Nombre, Apellido, Fecha de Nacimiento, DNI y los antecedentes (arreglo numpy)
De cada forense se registra: Identificacion
De cada policia se registra: Cargo y numero de placa
De cada policia forense se registra: Caso en el que esta trabajando
De cada antecedente se registra: Motivo, fecha, multa, y si se cumplio condena
1) Crear un gestor de personas (registro civil) basado en una lista definida por el programador
1.5) Crear un gestor de policias basado en una lista python
2) Se deben poder agregar nuevas personas y antecedentes
3) Para un motivo de antecendente se debe listar todas las personas que lo tengan
4) Un agente puede cargar una persona y un teniente puede cargar un antecedente y un capitan ambas cosas (interfaz)
5) Hacer una opcion de testing automatizado
6) Se deben guardar las personas en un archivo personas.json
7) Se deben guardar los policias en un archivo policia.csv
Hacer manejo de excepciones en las consignas 1, 2 y 3 
"""
from moduloGestorPersonas import gestorPersonas
from moduloGestorPolicias import gestorPolicias
from moduloInterface import InterfacePolicia
from moduloObjectEncoder import objectEncoder

def oficial(personas: InterfacePolicia):
   opcion = -1
   while opcion != 0:
      opcion = int(input("""Menu de opciones:
                         1) Agregar una nueva persona
                         0) Cerrar sesion
                         Ingrese una opcion: """))
      if opcion == 1:
         personas.crearPersona()
      elif opcion == 0:
         print("Cerrando sesion...")

def teniente(personas: InterfacePolicia):
   opcion = -1
   while opcion != 0:
      opcion = int(input("""Menu de opciones:
                         1) Agregar un nuevo antecedente
                         0) Cerrar sesion
                         Ingrese una opcion: """))
      if opcion == 1:
         personas.crearAntecedente()
      elif opcion == 0:
         print("Cerrando sesion...")
         
def capitan(personas: InterfacePolicia):
   opcion = -1
   while opcion != 0:
      opcion = int(input("""Menu de opciones:
                         1) Agregar una nueva persona
                         2) Agregar un nuevo antecedente
                         0) Cerrar sesion
                         Ingrese una opcion: """))
      if opcion == 1:
         personas.crearPersona()
      if opcion == 2:
         personas.crearAntecedente()
      elif opcion == 0:
         print("Cerrando sesion...")

def iniciarSesion(personas: gestorPersonas):
   usuario = input("Ingrese el DNI del policia: ")
   password = input("Ingrese la contraseña: ")
   nivel = personas.validarCuenta(usuario, password)
   if nivel == 1:
      print("Accediste como oficial")
      oficial(personas)
   elif nivel == 2:
      print("Accediste como teniente")
      teniente(personas)
   elif nivel == 3:
      print("Accediste como capitan")
      capitan(personas)
   

def main():
   encoder = objectEncoder()
   personas = None
   opcion = -1
   while opcion != 0:
      try:
         opcion = int(input("""\nMenu de opciones:
                        1) Crear una persona
                        2) Listar personas
                        3) Crear antecedente
                        4) Listar antecedentes
                        5) Crear agente
                        6) Listar todos los agentes
                        7) Buscar personas por motivo de antecedente
                        8) Iniciar sesion como policia
                        9) Guardar personas como JSON
                        10) Cargar personas desde el csv
                        0) Detener ejecucion
                        Ingrese una opcion: """))
      except ValueError:
         print("El valor ingresado no era un numero")
         opcion = -1
      if opcion == 10:
         d = encoder.cargarJSON()
         personas = encoder.decodificarDiccionario(d)
      if personas == None:
         personas = gestorPersonas()
      if opcion == 1:
         try:
            personas.crearPersona()
         except ValueError:
            print("El valor ingresado es invalido")
      elif opcion == 2:
         personas.listarPersonas()
      elif opcion == 3:
         dni = input("Ingrese el dni de la persona: ")
         try:
            personas.crearAntecedente(dni)
         except ValueError:
            print("El valor ingresado es invalido")
      elif opcion == 4:
         dni = input("Ingrese el dni de la persona: ")
         personas.listarAntecedentes(dni)
      elif opcion == 5:
         personas.crearAgente()
      elif opcion == 6:
         personas.listarAgentes()
      elif opcion == 7:
         motivo = input("Ingrese el motivo de antecedente: ")
         personas.buscarPorAntecedente(motivo)
      elif opcion == 8:
         iniciarSesion(personas)
      elif opcion == 9:
         d = personas.toJSON()
         encoder.guardarJSON(d)
      elif opcion == 0:
         print("Deteniendo ejecucion...")
      


if __name__ == "__main__":
   main()
   
"""Lote de prueba
1
Joaquin
Sasso
44991289
05/09/2003
1
Valentin
Vilches
45635995
01/05/2004
3
44991289
1
Exceso de facha
25/07/2024
20.01
si
5
Noel
Tejada
45876754
24/05/2005
p
capitan
31
gustavoceratti2004
5
Lucas
Valiente
44982342
20/08/2003
pf
teniente
87
luquinha
13
Narcotrafico
"""