from moduloEdificio import edificio
from moduloDepartamento import departamento
import csv

class gestorEdificios:
   __edificios: list
   
   def __init__(self):
      self.__edificios = []
      archivo = open("EdificioNorte.csv")
      reader = csv.reader(archivo, delimiter=";")
      id = -1
      for f in reader:
         if f[0] != id:
            id = f[0]
            nuevoEdificio = edificio(id = f[0], nombre=f[1], direccion=f[2], nombreConstructora=f[3], cantPisos=f[4], cantDptos=f[5])
            self.__edificios.append(nuevoEdificio)      
         else:
            self.__edificios[int(id)-1].agregarDpto(id=f[1], propietario=f[2], nroPiso=f[3], nroDpto=f[4], cantHabitaciones=f[5], banos=f[6], superficie=f[7])
      archivo.close()
   
   
   def buscarEdificio(self, nombreEdificio):
      i = 0
      while((i < len(self.__edificios)) and (nombreEdificio != self.__edificios[i].getNombre())):
         i += 1
      if i >= len(self.__edificios):
         print("No se encontro ese edificio")
         i = -1
      return i
   
   def mostrarPropietarios(self, nombreEdificio):
      i = self.buscarEdificio(nombreEdificio)
      if i != -1:
         self.__edificios[i].mostrarPropietarios()


   def mostrarSuperficie(self, nombreEdificio):
      i = self.buscarEdificio(nombreEdificio)
      if i != -1:
         total = self.__edificios[i].calcularSuperficie()
         print(f"El total de superficie cubierta del edificio es de: {total:0.1f} metros cuadrados")
   
   
   def buscarPropietario(self, propietario):
      i = 0
      bandera = False
      while((i < len(self.__edificios)) and (bandera == False)):
         idPropietario = self.__edificios[i].buscarPropietario(propietario)
         if idPropietario != -1:
            bandera = True
         else:
            i += 1
      if i >= len(self.__edificios):
         i = -1
      return i, idPropietario
         
   def porcentajeSuperficie(self, propietario):
      for edificio in self.__edificios:
         idPropietario = edificio.buscarPropietario(propietario)
         if idPropietario != -1:
            edificio.calcularPorcentaje(propietario)
   
   
   def contarDepartamentosLujosos(self, nombreEdificio, piso):
      i = self.buscarEdificio(nombreEdificio)
      if i != -1:
         self.__edificios[i].contarDptosLujosos(piso)
         