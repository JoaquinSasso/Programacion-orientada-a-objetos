import datetime

class jugador:
   __nombre: str
   __puntaje : int
   __fecha : str
   __hora : str
   
   def __init__(self, nombre, puntaje, fecha = None, hora = None, dia = None) -> None:
      self.__nombre = nombre
      self.__puntaje = puntaje
      fecha = str(fecha)
      self.__fecha = fecha
      if hora == None:
         fecha = fecha.split(" ")
         dia = fecha[0].split("-")
         dia = dia[2] + "/" + dia[1] + "/" + dia[0]
         hora = fecha[1]
         hora = hora[:5]
         self.__fecha = dia
      self.__hora = hora
   
   def getNombre(self) -> str:
      return self.__nombre
   
   def getPuntaje(self) -> int:
      return self.__puntaje
   
   def getHora(self) -> str:
      return self.__hora
   
   def getFecha(self) -> str:
      return self.__fecha
   
   def toJSON(self) -> dict:
      diccionario = dict(
         clase = __class__.__name__,
         datos = dict(
            nombre = self.__nombre,
            puntaje = self.__puntaje,
            fecha = self.__fecha,
            hora = self.__hora
         )
      )
      return diccionario
   
   def __gt__(self, otro):
      return self.__puntaje > otro.getPuntaje()