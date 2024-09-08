from tkinter import *
from tkinter import ttk
from moduloBoton import boton   
import random
import datetime
from moduloObjectEncoder import objectEncoder
from moduloGestorJugadores import gestorJugadores
   
class Aplicacion():
   __ventana : Tk
   __botones : list[boton]
   __colores : list[str]
   __resaltados : list[str]
   __jugador : str
   __encoder : objectEncoder
   __jugadores: gestorJugadores
   
   def __init__(self, __jugador):
      self.__jugador = __jugador
      self.pulsados = []
      self.__botones = []
      self.secuencia = []
      
      self.__colores = ["green", "red4", "yellow3", "blue4"]
      self.__resaltados = ["green2", "red", "yellow","blue2"]
      self.teclas = ["<Key-KP_1>", "<Key-KP_4>", "<Key-KP_2>", "<Key-KP_5>"]
      self.eventos = [self.botonVerde, self.botonRojo, self.botonAmarillo, self.botonAzul]
      
      self.__ventana = Tk()
      self.__ventana.geometry("275x420")
      self.__ventana.title("Py-Simon Game")
      self.__ventana.resizable(0, 0)
      
      self.puntos = IntVar(self.__ventana)
      self.textoPuntaje = ttk.Label(self.__ventana, text=self.__jugador)
      self.textoPuntaje.grid(row=0, column=0)
      self.puntaje = ttk.Label(self.__ventana, textvariable= self.puntos)
      self.puntaje.grid(row = 0, column = 0, sticky=E)
      
      for i in range(len(self.__colores)):
         unBoton = boton(self.__ventana, self.eventos[i], self.__colores[i])
         self.__botones.append(unBoton)
         
      self.__botones[0].canvas.grid(row = 1, column= 0)
      self.__botones[1].canvas.grid(row = 1, column= 1)
      self.__botones[2].canvas.grid(row = 2, column= 0)
      self.__botones[3].canvas.grid(row = 2, column= 1)

      for i in range(2):
        self.__ventana.grid_rowconfigure(i, minsize=10)
        self.__ventana.grid_columnconfigure(i, weight=1)

      
      barraMenu = Menu(self.__ventana)
      menuPuntuaciones = Menu(barraMenu, tearoff=0)
      menuPuntuaciones.add_command(label="Tabla de puntuaciones", command= self.tablaPuntuaciones)
      menuPuntuaciones.add_command(label="Salir", command= self.__ventana.destroy)
      barraMenu.add_cascade(label= "Puntajes", menu=menuPuntuaciones)
      self.__ventana.config(menu=barraMenu)
      
      self.__ventana.after(10, self.juego)
      self.__ventana.mainloop()
   
   
   def botonVerde(self):
      self.pulsados.append(0)
      self.feedback(0)
      i = len(self.pulsados)-1
      try:
         if self.pulsados[i] != self.secuencia[i]:
            self.derrota = True
      except IndexError:
         self.derrota = True

   def botonRojo(self):
      self.pulsados.append(1)
      self.feedback(1)
      i = len(self.pulsados)-1
      try:
         if self.pulsados[i] != self.secuencia[i]:
            self.derrota = True
      except IndexError:
         self.derrota = True

   def botonAmarillo(self):
      self.pulsados.append(2)
      self.feedback(2)
      i = len(self.pulsados)-1
      try:
         if self.pulsados[i] != self.secuencia[i]:
            self.derrota = True
      except IndexError:
         self.derrota = True
      
   def botonAzul(self):
      self.pulsados.append(3)
      self.feedback(3)
      i = len(self.pulsados)-1
      try:
         if self.pulsados[i] != self.secuencia[i]:
            self.derrota = True
      except IndexError:
         self.derrota = True
   
   def feedback(self, color):
      tiempo = 200
      self.__botones[color].cambiarColor(self.__resaltados[color])
      self.__ventana.update()
      self.__ventana.after(tiempo, self.__botones[color].recuperarColor())
      
   def mostrarSecuencia(self, color):
      #self.__botones[color].cambiarColor("thistle3")
      self.__botones[color].cambiarColor(self.__resaltados[color])
      
   def recuperarColor(self):
      for boton in self.__botones:
         boton.recuperarColor()
   
   def generarColor(self):
      self.__ventana.update()
     
      semilla = str(datetime.datetime.now())
      random.seed(semilla)
      numero = random.randint(0, 3)
      self.secuencia.append(numero)
      
   def reiniciarJuego(self):
      self.gameOver.destroy()
      self.__jugadores.crearJugador(self.__jugador, self.rondas)
      self.__jugadores.ordenarJugadores()
      self.__encoder.guardarJSON(self.__jugadores)
      self.__ventana.after(2000, self.juego)
      
      
   def mensajeDerrota(self):
      self.gameOver = Toplevel()
      tamypos = "300x100"
      self.gameOver.geometry(tamypos)
      self.gameOver.resizable(0,0)
      self.gameOver.title("Has perdido")
      mensaje = ttk.Label(self.gameOver, text= "Game over!")
      mensaje.pack(side = TOP, padx=15, pady=5)
      puntaje = ttk.Label(self.gameOver, text= "Tu puntaje fue de: " + str(self.rondas))
      puntaje.pack(side = TOP, pady= 5)
      boton = ttk.Button(self.gameOver, text="Reiniciar", command= self.reiniciarJuego)
      boton.pack(side=BOTTOM, padx=20, pady= 5)
      self.gameOver.transient(master=self.__ventana)
      self.gameOver.grab_set()
      self.__ventana.wait_window(self.gameOver)
      
   def tablaPuntuaciones(self):
      self.__jugadores.tablaPuntuaciones()
   
   def salir(self):
      self.__ventana.destroy()
   
   def juego(self):
      self.secuencia = []
      self.derrota = False
      self.rondas = 0
      self.puntos.set(self.rondas)
      self.__encoder = objectEncoder()
      d = self.__encoder.cargarJSON()
      self.__jugadores = self.__encoder.decodificarDiccionario(d)
      while not self.derrota:
         self.pulsados = []
         self.generarColor()
         print(f"La secuencia es: {self.secuencia}")
         self.__ventana.after(300)
         for color in self.secuencia:
            self.mostrarSecuencia(color)
            self.__ventana.after(400)
            self.__ventana.update()
            self.recuperarColor()
            self.__ventana.after(200)
            self.__ventana.update()
         while len(self.pulsados) != len(self.secuencia):
            self.__ventana.after(50)
            self.__ventana.update()
            if self.derrota == True:
               break
         if len(self.secuencia) == len(self.pulsados) or self.derrota:
            try:
               for i in range(len(self.secuencia)):
                  if self.secuencia[i] != self.pulsados[i]:
                     self.mensajeDerrota()
                     self.derrota = True
               else:
                  self.rondas += 1
                  self.puntos.set(self.rondas)
                  self.__ventana.update()
            except IndexError:
               self.mensajeDerrota()
               self.derrota = True