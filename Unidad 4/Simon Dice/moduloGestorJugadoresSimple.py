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
      tamypos = "400x250"
      ventana.geometry(tamypos)
      ventana.resizable(0,0)
      ventana.title("Galeria de puntajes")
      
      encabezado = ttk.Labelframe(ventana)
      encabezado.pack(side = TOP)
      jugador = ttk.Label(encabezado, text="Jugador")
      jugador.grid(row=0, column=0, padx = 30, sticky=E)
      fecha = ttk.Label(encabezado, text="Fecha")
      fecha.grid(row=0, column=1, padx = 37)
      hora = ttk.Label(encabezado, text="Hora")
      hora.grid(row=0, column=2, padx = 40)
      puntaje = ttk.Label(encabezado, text="Puntaje")
      puntaje.grid(row=0, column=3, padx = 18)
      
      
      
      boton = ttk.Button(ventana, text="Salir", command= ventana.destroy)
      boton.pack(side=BOTTOM)
        
      cuerpo = ttk.LabelFrame(ventana, height=460, width=300)
      cuerpo.config()
      cuerpo.pack(side = BOTTOM)
      
      for i in range(len(self.__jugadores)):
         textos = [self.__jugadores[i].getNombre(), self.__jugadores[i].getFecha(), self.__jugadores[i].getHora(), self.__jugadores[i].getPuntaje()]
         for j in range(4):
            primero = ttk.Label(cuerpo, text = textos[j])
            primero.grid(row = i, column = j, padx=30)
      
      for i in range(4):
         cuerpo.grid_rowconfigure(i, minsize=10)
         cuerpo.grid_columnconfigure(i, weight=1)
         
      
      