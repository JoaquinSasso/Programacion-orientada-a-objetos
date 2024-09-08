class nodo:
   __datos : object
   __sig : object
   
   def __init__(self, datos, sig = None):
      self.__datos = datos
      self.__sig = sig
   
   def getDatos(self):
      return self.__datos
   
   def getSig(self):
      return self.__sig
   
   def setSig(self, nuevo):
      self.__sig = nuevo