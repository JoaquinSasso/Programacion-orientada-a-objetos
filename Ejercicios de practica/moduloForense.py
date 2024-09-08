from moduloPersona import Persona
class Forense(Persona):
   __ide : str
   
   def __init__(self,ide, cargo, placa, password, nombre, apellido, nacimiento, dni, antecedentes = []) -> None:
      super().__init__(ide, cargo, placa, password, nombre, apellido, nacimiento, dni, antecedentes = [])
      self.__ide = ide
      
   def getIde(self):
      return self.__ide

   def toJSON(self):
      d = dict(
         clase = self.__class__.__name__,
               datos = dict(
                  ide = self.__ide,
                  cargo = None,
                  placa = None,
                  password = None,
                  nombre = super().getNombre(),
                  apellido = super().getApellido(), 
                  nacimiento = super().getNacimiento(),
                  dni = super().getDNI(),
                  antecedentes = super().antecedentesJSON()
               ))
      return d