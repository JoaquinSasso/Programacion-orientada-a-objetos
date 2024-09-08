from moduloDepartamento import departamento
class edificio:
   __id: int
   __nombre: str
   __direccion: str
   __nombreConstructora: str
   __cantPisos: int
   __cantDptos: int
   __departamentos: list
   
   def __init__(self, **kwargs):
      self.__id = int(kwargs["id"])
      self.__nombre = kwargs["nombre"]
      self.__direccion = kwargs["direccion"]
      self.__nombreConstructora = kwargs["nombreConstructora"]
      self.__cantPisos = int(kwargs["cantPisos"])
      self.__cantDptos = int(kwargs["cantDptos"])
      self.__departamentos = []
      
      
   def agregarDpto(self, **kwargs):
      dpto = departamento(**kwargs)
      self.__departamentos.append(dpto)
      
      
   def mostrarPropietarios(self):
      for dpto in self.__departamentos:
         dpto.mostrarPropietario()
         
   def calcularSuperficie(self):
      total = 0
      for dpto in self.__departamentos:
         total += dpto.getSuperficie()
      return total
      
      
   def buscarPropietario(self, propietario):
      i = 0
      while((i < len(self.__departamentos)) and (propietario != self.__departamentos[i].getPropietario())):
         i += 1
      if i >= len(self.__departamentos):
         print("No se encontro el propietario")
         i = -1
      return i
      
   
   def calcularPorcentaje(self, propietario):
      superficieEdificio = self.calcularSuperficie()
      for dpto in self.__departamentos:
         if dpto.getPropietario() == propietario:
            superficieDpto = dpto.getSuperficie()
            porcentaje = (superficieDpto / superficieEdificio) * 100
            print(f"La superficie del departamento es {superficieDpto:0.1f} y representa el {porcentaje:0.2f}% del edificio {self.getNombre()}")
            
   
   def contarDptosLujosos(self, piso):
      cant = 0
      for dpto in self.__departamentos:
         banos = dpto.getBanos()
         habitaciones = dpto.getHabitaciones()
         pisoActual = dpto.getPiso()
         if((banos > 1) and (habitaciones == 3) and (piso == pisoActual)):
            cant += 1
      print(f"La cantidad de departamentos de que cumplen las condiciones es de {cant}")
  
   
   def getNombre(self):
      return self.__nombre