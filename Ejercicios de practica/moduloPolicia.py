from moduloPersona import Persona
class Policia(Persona):
   __cargo : str
   __placa : str
   __password: str
   
   def __init__(self,ide, cargo, placa, password, nombre, apellido, nacimiento, dni, antecedentes = []) -> None:
      super().__init__(ide, cargo, placa, password, nombre, apellido, nacimiento, dni, antecedentes = [])
      self.__cargo = cargo
      self.__placa = placa
      self.__password = password
      
   def getCargo(self):
      return self.__cargo
   
   def getPlaca(self):
      return self.__placa
   
   def getPassword(self):
      return self.__password
   
   def checkPassword(self, password):
      bandera = False
      if self.__password == password:
         bandera = True
      return bandera

   def __str__(self):
      return super().__str__() + f"\nCargo: {self.__cargo}"
   
   def toJSON(self):
      d = dict(
         clase = self.__class__.__name__,
               datos = dict(
                  ide = None,
                  cargo = self.__cargo,
                  placa = self.__placa,
                  password = self.__password,
                  nombre = super().getNombre(),
                  apellido = super().getApellido(), 
                  nacimiento = super().getNacimiento(),
                  dni = super().getDNI(),
                  antecedentes = super().antecedentesJSON()
               ))
      return d