from moduloAntecendete import Antecedente
import numpy as np
class Persona:
   __nombre : str
   __apellido: str
   __nacimiento : str
   __dni: str
   __antecendentes: np.ndarray[Antecedente]
   __dimension :int
   __cantidad :int
   
   def __init__(self, ide, cargo, placa, password, nombre, apellido, nacimiento, dni, antecedentes = []) -> None:
      self.__nombre = nombre
      self.__apellido = apellido
      self.__nacimiento = nacimiento
      self.__dni = dni
      self.__antecendentes = np.empty(0, dtype= Antecedente)
      self.__dimension = 0
      self.__cantidad = 0
      if antecedentes != []:
         for a in antecedentes:
            datos = a["datos"]
            nuevoAntecedente = Antecedente(**datos)
            self.agregarAntecedente(nuevoAntecedente)
      
   def buscarAntecedenteNro(self, nro):
      i = 0
      while ((i < len(self.__antecendentes)) and (self.__antecendentes[i].getNro() != nro)):
         i += 1
      if (i == len(self.__antecendentes)):
         i = -1
      return i

   def buscarAntecedenteMotivo(self, motivo):
      i = 0
      while ((i < len(self.__antecendentes)) and (self.__antecendentes[i].getMotivo() != motivo)):
         i += 1
      if (i == len(self.__antecendentes)):
         i = -1
      return i
   
   def getAntecedente(self, nro):
      i = self.buscarAntecedente(nro)
      if i != -1:
         return self.__antecendentes[i]

   
   def listarAntecedentes(self):
      for a in self.__antecendentes:
         print(a)
   
   def getNombre(self):
      return self.__nombre
   
   def getApellido(self):
      return self.__apellido
   
   def getNacimiento(self):
      return self.__nacimiento
   
   def getDNI(self):
      return self.__dni
   
   def __lt__(self, otro):
      return self.__dni < otro.getDNI()

   def __eq__(self, otro):
      return self.__dni == otro.getDNI()

   def __ne__(self, otro):
      return self.__class__ != otro.__class__
   
   def __str__(self):
      return f"{self.__nombre} {self.__apellido}, DNI: {self.__dni}; nacido en {self.__nacimiento}"

   def agregarAntecedente(self, nuevo):
      if self.__cantidad == self.__dimension:
         self.__dimension += 1
         self.__antecendentes.resize(self.__dimension)
      self.__antecendentes[self.__cantidad] = nuevo
      self.__cantidad += 1
   
   def antecedentesJSON(self):
      lista = []
      for a in self.__antecendentes:
         lista.append(a.toJSON())
      return lista
   
   def toJSON(self):
      d = dict(
         clase = self.__class__.__name__,
               datos = dict(
                  nombre = self.__nombre,
                  apellido = self.__apellido, 
                  nacimiento = self.__nacimiento,
                  dni = self.__dni,
                  antecedentes = self.antecedentesJSON()
               ))
      return d