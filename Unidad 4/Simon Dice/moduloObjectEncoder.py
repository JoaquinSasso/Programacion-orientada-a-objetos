import sys
sys.dont_write_bytecode = True
import json
from pathlib import Path
from moduloJugador import jugador
from moduloGestorJugadores import gestorJugadores

class objectEncoder:
   def guardarJSON(self, gestor: gestorJugadores):
      diccionario = gestor.toJSON()
      with Path("pysimonpuntajes.json").open("w", encoding="UTF-8") as destino:
         json.dump(diccionario, destino, indent=4)
         destino.close()
      
      
   def cargarJSON(self):
      with Path("pysimonpuntajes.json").open("r", encoding="UTF-8") as fuente:
         diccionario = json.load(fuente)
         fuente.close
      return diccionario
   
   
   def decodificarDiccionario(self, d):
      if "clase" not in d:
         return d
      else:
         class_name = d["clase"]
         class_ = eval(class_name)
         if class_name == "gestorJugadores":
            puntuaciones = d["datos"]
            gestor = gestorJugadores()
            for i in range(len(puntuaciones)):
               dJugador = puntuaciones[i]
               class_name = dJugador.pop("clase")
               class_=eval(class_name)
               atributos = dJugador["datos"]
               unJugador = class_(**atributos)
               gestor.agregarJugador(unJugador)
         return gestor