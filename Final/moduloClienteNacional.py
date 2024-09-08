from moduloClienteLocal import ClienteLocal
class ClienteNacional(ClienteLocal):
   __provincia : str
   __localidad : str
   __codigoPostal : str
   
   def __init__(self, nombre, apellido, email, contraseña, direccionPostal, telefono, provincia, localidad, codigoPostal,):
      super().__init__(nombre, apellido, email, contraseña, direccionPostal, telefono)
      self.__provincia = provincia
      self.__localidad = localidad
      self.__codigoPostal = codigoPostal
      
   def __str__(self):
      return f"El/la cliente {super().getNombre()} vive en la provincia de {self.__provincia}"