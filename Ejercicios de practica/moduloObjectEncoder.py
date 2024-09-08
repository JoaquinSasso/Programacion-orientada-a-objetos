from moduloGestorPersonas import Persona, Antecedente, gestorPersonas, Policia, PoliciaForense, Forense
import json
from pathlib import Path
class objectEncoder:
   
   
   def guardarJSON(self, diccionario):
      with Path("personas.json").open("w", encoding="UTF-8") as destino:
         json.dump(diccionario, destino, indent=4)
         destino.close()
      print("Se guardo el archivo")
      
      
   def cargarJSON(self):
      with Path("personas.json").open("r", encoding="UTF-8") as fuente:
         diccionario = json.load(fuente)
         fuente.close
      print("Se leyo el archivo")
      return diccionario
   
   
   def decodificarDiccionario(self, d):
      if "clase" not in d:
         return d
      else:
         class_name = d["clase"]
         class_ = eval(class_name)
         if class_name == "gestorPersonas":
            personas = d["datos"]
            gestorC = gestorPersonas()
            for i in range(len(personas)):
               dPersona = personas[i]
               class_name = dPersona.pop("clase")
               class_=eval(class_name)
               atributos = dPersona["datos"]
               unaPersona = class_(**atributos)
               gestorC.agregarPersona(unaPersona)
         return gestorC