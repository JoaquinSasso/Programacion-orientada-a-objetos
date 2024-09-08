from moduloPolicia import Policia
from moduloForense import Forense
class PoliciaForense(Policia, Forense):
   __caso : str
   
   def __init__(self,caso, ide, cargo, placa, password, nombre, apellido, nacimiento, dni, antecedentes= []) -> None:
      super().__init__(ide, cargo, placa, password, nombre, apellido, nacimiento, dni, antecedentes)
      self.__caso = caso
   
   def getCaso(self):
      return self.__caso

   def toJSON(self):
      d = dict(
         clase = self.__class__.__name__,
               datos = dict(
                  caso = self.__caso,
                  ide = super().getIde(),
                  cargo = super().getCargo(),
                  placa = super().getPlaca(),
                  password = super().getPassword(),
                  nombre = super().getNombre(),
                  apellido = super().getApellido(), 
                  nacimiento = super().getNacimiento(),
                  dni = super().getDNI(),
                  antecedentes = super().antecedentesJSON()
               ))
      return d