import csv
from moduloGammer import gammer
from moduloGestorConexiones import gestorConexiones

class gestorGammers:
   __lista : list[gammer]
   
   def __init__(self):
      self.__lista = []
      archivo = open("gammers.csv")
      reader = csv.reader(archivo, delimiter=";")
      skip = False
      for fila in reader:
         if skip == False:
            skip = True
         else:
            idJugador = fila[0]
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            alias = fila[4]
            plan = fila[5]
            importeBase = fila[6]
            tiempoLimite = fila[7]
            nuevoGammer = gammer(idJugador, dni, nombre, apellido, alias, plan, importeBase, tiempoLimite)
            self.__lista.append(nuevoGammer)
      archivo.close()
      
   def buscarDni(self, dni):
      i = 0
      while((i < len(self.__lista)) and (dni != self.__lista[i].getDni())):
         i += 1
      if i == len(self.__lista):
         print("No se encontro a un gammer con ese DNI")
         i = -1
      return i 
   
   def emitirListado(self, dni, conexiones : gestorConexiones):
      i = self.buscarDni(dni)
      if i != -1:
         actual = self.__lista[i]
         print(f"""DNI: {dni}    Nombre y apellido: {actual.getNombre()} {actual.getApellido()}
Alias: {actual.getAlias()}    Plan: {actual.getPlan()}      Importe base: {actual.getImporte()}""")
         tiempoTotal = conexiones.emitirListado(actual.getId())
         tiempoExtra = tiempoTotal - actual.getTiempoLimite()
         importeBase = actual.getImporte()
         plan = actual.getPlan()
         if plan == "Extendio":
            porcentaje = 0.4
         elif plan == "Completo":
            porcentaje = 0.3
         elif plan == "Basico":
            porcentaje = 0.25
         if tiempoExtra > 0:
            print(f"Total de horas: {tiempoTotal}     Horas en exceso:{tiempoExtra}")
            importeTotal = importeBase + importeBase * (tiempoExtra * porcentaje)
         else:
            print(f"Total de horas: {tiempoTotal}     Horas en exceso: Ninguna")
            importeTotal = importeBase
         print(f"Importe a facturar: {importeTotal}")
         
   def mostrarDatos(self, id):
      print(self.__lista[id-1])
   
   
   def buscarPlan(self,id):
      return self.__lista[id-1].getPlan()
   
   def mostrarDatos(self, id):
      print(self.__lista[id-1])