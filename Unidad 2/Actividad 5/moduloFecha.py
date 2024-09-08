class fecha: 
   __fecha : str
   __idLocal: int
   __idVisitante: int
   __golesLocal: int
   __golesVisitante: int
   
   
   def __init__(self, fecha, idL, idV, gL, gV):
      self.__fecha = fecha
      self.__idLocal = idL
      self.__idVisitante = idV
      self.__golesLocal = gL
      self.__golesVisitante = gV
      
   def getFecha(self):
      return self.__fecha
   def getIdV(self):
      return self.__idVisitante
   def getIdL(self):
      return self.__idLocal
   def getGL(self):
      return self.__golesLocal
   def getGV(self):
      return self.__golesVisitante
   