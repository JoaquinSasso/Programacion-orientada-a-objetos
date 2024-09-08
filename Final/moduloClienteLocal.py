class ClienteLocal:
   __nombre : str
   __apellido : str
   __email : str
   __contraseña : str
   __direccionPostal : str
   __telefono : str
   
   def __init__(self, nombre, apellido, email, contraseña, direccionPostal, telefono):
      self.__nombre = nombre
      self.__apellido = apellido
      self.__email = email
      self.__contraseña = contraseña
      self.__direccionPostal = direccionPostal
      self.__telefono = telefono
   
   def getNombre(self):
      return self.__nombre