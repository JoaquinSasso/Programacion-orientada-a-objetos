from moduloEmpleado import empleado
from moduloCapacitacion import capacitacion
class matricula:
   __fecha : str
   __empleado : empleado
   __capacitacion: capacitacion
   
   
   def __init__(self, fecha, empleado, capacitacion):
      self.__fecha = fecha
      self.__empleado = empleado
      self.__capacitacion = capacitacion
      
   
   def setEmpleado(self, empleado):
      self.__empleado = empleado
   def setPrograma(self, capacitacion):
      self.__capacitacion = capacitacion
      
      
   def getFecha(self):
      return self.__fecha
   def getEmpleado(self):
      return self.__empleado
   def getCapacitacion(self):
      return self.__capacitacion
   def getDuracionCap(self):
      return self.__capacitacion.getDuracion()
   def getNombreCap(self):
      return self.__capacitacion.getNombre()
   def getNombreE(self):
      return self.__empleado.getNombre()
   def getIdE(self):
      return self.__empleado.getId()