import sys
sys.dont_write_bytecode = True
import json
from moduloGestorCalefactores import gestorCalefactores
from pathlib import Path
from moduloCalefactorElectrico import electrico
from moduloCalefactorGas import gas
class objectEncoder:
   
   
   def guardarJSON(self, diccionario):
      with Path("calefactores.json").open("w", encoding="UTF-8") as destino:
         json.dump(diccionario, destino, indent=4)
         destino.close()
      print("Se guardo el archivo")
      
      
   def cargarJSON(self):
      with Path("calefactores.json").open("r", encoding="UTF-8") as fuente:
         diccionario = json.load(fuente)
         fuente.close
      print("Se leyo el archivo")
      return diccionario
   
   
   def decodificarDiccionario(self, d):
      if "__class__" not in d:
         return d
      else:
         class_name = d["__class__"]
         class_ = eval(class_name)
         if class_name == "gestorCalefactores":
            calefactores = d["datos"]
            gestorC = gestorCalefactores()
            for i in range(len(calefactores)):
               dCalecator = calefactores[i]
               class_name = dCalecator.pop("__class__")
               class_=eval(class_name)
               atributos = dCalecator["__atributos__"]
               unCalefactor = class_(**atributos)
               gestorC.agregarElemento(unCalefactor)
         return gestorC