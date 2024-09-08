from moduloApp import Aplicacion
from tkinter import *
from tkinter import ttk

class venatanaInicio():
   __ventana : Tk
   __nombre : StringVar
   __jugador : str
   
   def __init__(self):
      self.__ventana = Tk()
      self.__ventana.geometry("250x100")
      self.__ventana.title("Py-Simon Game")
      self.__ventana.resizable(0, 0)
      
      self.__nombre = StringVar()
      
      mensaje = ttk.Label(self.__ventana, text="Datos del Jugador")
      mensaje.grid(row=0, column=0, padx=5, pady=5)
      
      boton = ttk.Button(self.__ventana, text="Iniciar Juego", command= self.destruir)
      boton.grid(columnspan=2, row=3)
      
      mensaje2 = ttk.Label(self.__ventana, text="Jugador")
      mensaje2.grid(row=1, column=0,padx=5)
      respuesta = ttk.Entry(self.__ventana, textvariable= self.__nombre)
      respuesta.grid(row=1, column=1, padx=5, pady=5)
      respuesta.bind("<Return>", self.destruir)
      respuesta.focus()
      
      self.__jugador = ""
      while self.__jugador == "":
         self.__ventana.after(200)
         self.__ventana.update()
      self.juego = Aplicacion(self.__jugador)
      
      self.__ventana.mainloop()
      
   def destruir(self, event = None) -> str:
      self.__jugador = self.__nombre.get()
      self.__ventana.destroy()
        

if __name__ == "__main__":
   venatanaInicio()