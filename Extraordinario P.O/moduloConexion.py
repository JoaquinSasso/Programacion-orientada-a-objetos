class conexion:
   __idJugador: int
   __ip: str
   __juego: str
   __fecha: str
   __horaInicio: int
   __horaFin: int
   
   def __init__(self, id, ip, juego, fecha, inicio, fin):
      self.__idJugador = int(id)
      self.__ip = ip
      self.__juego = juego
      self.__fecha = fecha
      self.__horaInicio = int(inicio)
      self.__horaFin = int(fin)
      
   def getId(self):
      return self.__idJugador
   
   def getIp(self):
      return self.__ip
   
   def getJuego(self):
      return self.__juego
   
   def getFecha(self):
      return self.__fecha
   
   def getInicio(self):
      return self.__horaInicio
   
   def getFin(self):
      return self.__horaFin
   
   def __lt__(self,otrconex):
      return self.__fecha < otrconex.getFecha() and self.__horaInicio<otrconex.getInicio() and self.__ip<otrconex.getIp()
   def __eq__(self,otrconex):
      return self.__fecha == otrconex.getFecha() and self.__horaInicio==otrconex.getInicio() and self.__ip!=otrconex.getIp()