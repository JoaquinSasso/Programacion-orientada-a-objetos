from moduloGestorPersonas import gestorPersonas
from moduloPersona import Persona
from moduloAntecendete import Antecedente
import unittest
 
class testing(unittest.TestCase):
   __personas : gestorPersonas
   
   def setUp(self):
      self.__personas =  gestorPersonas()
      nuevaPersona = Persona(None,None,None,None,"Joaquin", "Sasso", "05/09/2003", "44991289")
      self.__personas.agregarPersona(nuevaPersona)
      nuevaPersona = Persona(None,None,None,None,"Valentin", "Vilches", "01/05/2004", "45635995")
      self.__personas.agregarPersona(nuevaPersona)
      nuevoAntecedente = Antecedente(1, "Exceso de facha", "25/07/2024", 20.01, True)
      self.__personas.agregarAntecedente("44991289", nuevoAntecedente)
 
   def test_buscar(self):
      nuevaPersona = Persona(None,None,None,None,"Joaquin", "Sasso", "05/09/2003", "44991289")
      self.assertEqual(nuevaPersona, self.__personas.buscarPersona("44991289"))

if __name__ == "__main__":
   unittest.main()