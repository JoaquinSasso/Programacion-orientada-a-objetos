class equipo:
  __ide : int
  __nombre : str
  __golesAFavor : int
  __golesEnContra : int 
  __diferencia : int
  __puntos : int


  def __init__(self, ide, nombre, gf, gc, dg, puntos):
    self.__ide = int(ide)
    self.__nombre = nombre
    self.__golesAFavor = int(gf)
    self.__golesEnContra = int(gc)
    self.__diferencia = int(dg)
    self.__puntos = int(puntos)
  
  
  def actualizarDG(self):
    self.__diferencia = self.__golesAFavor - self.__golesEnContra
  
  def agregarGF(self, goles):
    self.__golesAFavor += goles
    
  def agregarGC(self, goles):
    self.__golesEnContra += goles  
    
  def agregarPuntos(self, puntos):
    self.__puntos += puntos
  
  def getIdE(self):
    return self.__ide
  
  def getNombre(self):
    return self.__nombre
  
  def getGF(self):
    return self.__golesAFavor
  
  def getGC(self):
    return self.__golesEnContra
  
  def getDG(self):
    return self.__diferencia
  
  def getPuntos(self):
    return self.__puntos
  
  def __gt__(self, otro):
    return self.__puntos > otro.getPuntos()
  
  def __lt__(self, otro):
    return self.__ide < otro.getIdE()
  
  def __eq__(self, otro):
    return self.__puntos == otro.getPuntos()