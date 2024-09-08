import datetime
from moduloJugador import jugador
from tkinter import *
from tkinter import ttk

class gestorJugadores:
   __jugadores : list[jugador]
   
   def __init__(self) -> None:
      self.__jugadores = []
   
   def crearJugador(self, nombre, puntaje, fecha = None):
      if fecha == None:
         fecha = datetime.datetime.now()
      nuevo = jugador(nombre, puntaje, fecha)
      self.agregarJugador(nuevo)
   
   
   def agregarJugador(self, nuevo):
      self.__jugadores.append(nuevo)
   
   def ordenarJugadores(self):
      self.__jugadores.sort(reverse=True)
   
   def puntuacionesToJSON(self) -> list:
      lista = []
      for puntuacion in self.__jugadores:
         lista.append(puntuacion.toJSON())
      return lista
   
   def toJSON(self) -> dict:
      diccionario = dict(
         clase = __class__.__name__,
         datos = self.puntuacionesToJSON()
      )
      return diccionario
   
   def tablaPuntuaciones(self):
      ventana = Toplevel()
      ventana.geometry("400x300")
      ventana.resizable(0,0)
      ventana.title("Galeria de puntajes")
      
      cuerpo = ttk.Frame(ventana)
      cuerpo.pack(side = BOTTOM, fill=BOTH, expand=True)

      scrollbar = ttk.Scrollbar(cuerpo)
      scrollbar.pack(side=RIGHT, fill=Y)

      tabla = ttk.Treeview(cuerpo, yscrollcommand=scrollbar.set)
      tabla.pack(side=LEFT, fill=BOTH, expand=True)

      scrollbar.config(command=tabla.yview)

      tabla["columns"] = ("Jugador", "Fecha", "Hora", "Puntaje")
      tabla.column("#0", width=60, anchor="center")
      tabla.column("Jugador", width=60, anchor="center")
      tabla.column("Fecha", width=60, anchor="center")
      tabla.column("Hora", width=60, anchor="center")
      tabla.column("Puntaje", width=60, anchor="center")

      tabla.heading("#0", text="")
      tabla.heading("Jugador", text="Jugador")
      tabla.heading("Fecha", text="Fecha")
      tabla.heading("Hora", text="Hora")
      tabla.heading("Puntaje", text="Puntaje")
      

      for i in range(len(self.__jugadores)):
         tabla.insert("", "end", text=str(i+1), values=(
               self.__jugadores[i].getNombre(),
               self.__jugadores[i].getFecha(),
               self.__jugadores[i].getHora(),
               str(self.__jugadores[i].getPuntaje())
         ))
            
      
      