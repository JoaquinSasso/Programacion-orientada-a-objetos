class visualizacion:
    __idmiembro:str
    __idpelicula:str
    __fecha:str
    __hora:str
    __min:int
    def __init__(self,idmiembro,idpelicula,feyho,min,hora):
        self.__idmiembro=idmiembro
        self.__idpelicula=idpelicula
        self.__fecha=feyho
        self.__min=min
        self.__hora = hora

    def getidmiembro(self):
        return self.__idmiembro
    def getidpelicula(self):
        return self.__idpelicula
    def getfecha(self):
        return self.__fecha
    def gethora(self):
        return self.__hora
    def getmin(self):
        return self.__min


    def __eq__(self, otro):
        bandera = False
        if self.__idmiembro == otro.getidmiembro():
            if self.__fecha == otro.getfecha():
                if self.__hora == otro.gethora():
                    bandera = True
        return bandera