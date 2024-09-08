from tkinter import *

class boton:
   __canvas : Canvas
   __color : str
   __master : Tk
   def __init__(self, master, comando, color):
      self.__color = color
      self.__master = master
      self.canvas = Canvas(master, width= 150, height= 200)
      
      self.boton = self.canvas.create_rectangle(5, 5, 130, 185, fill = color, outline= "black", width= 2)
      self.canvas.tag_bind(self.boton, "<Button-1>", lambda e: comando())
   
   
   def cambiarColor(self, color):
      self.canvas.itemconfig(self.boton, fill=color)

   def recuperarColor(self):
      self.canvas.itemconfig(self.boton, fill = self.__color)