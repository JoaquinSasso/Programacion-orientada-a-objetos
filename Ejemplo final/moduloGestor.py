from moduloHibrido import Combustion, Electrico, Hibrido
from moduloVehiculo import Vehiculo
from moduloPersona import Persona

class Gestor:
   __vehiculo : Vehiculo
   __electrico : Electrico
   __combustion : Combustion
   __hibrido : Hibrido
   __persona : Persona
   
   def __init__(self):
      self.__vehiculo = Vehiculo(5, 63, "Ford Ka")
      self.__combustion = Combustion(5, 153, "Chevrolet Cruze", combustible= 60)
      self.__electrico = Electrico(5, 170, "Tesla Model 3", 75)
      self.__hibrido = Hibrido(5, 122, "Toyota Corolla 1.8 SE-G Hybrid CVT", 1.3, 43, 486)
      self.__persona = Persona("Joaquin", "Sasso", "05/09/2003", "44991289")
   
   def mostrarSobrecarga(self):
      print(f""" Para hacer uso de la sobrecarga de operadores probaremos sobrecargar __eq__ o ==
            Tiene la persona cargada el dni 44991289?: {self.__persona == "44991289"}
            Y el DNI 27896764?: {self.__persona == "27896764"}""")
      
   def mostrarPolimorfismo(self):
      print("""Para mostrar la aplicacion de polimorfismo armaremos una lista con objetos de 3 clases distinas
Entre ellos hay un vehiculo y un vehiculo a combustible (Polimorfismo de subtipo), ademas una persona (Polimorfismo general)
Para todos ejecutaremos un metodo con el mismo nombre, en este caso polimorfismo
El resultado de cada metodo sera distinto, comprobando el polimorfismo""")
      lista = [self.__vehiculo, self.__persona, self.__combustion]
      for obj in lista:
         obj.polimorfismo()