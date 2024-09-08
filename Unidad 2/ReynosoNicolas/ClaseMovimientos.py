class movimiento:
    __nrocuenta=int
    __fecha=str
    __descripcion=str
    __tipo=str
    __importe=float
    def __init__(self,nro,fecha,descripcion,tipo,importe):
        self.__nrocuenta=nro
        self.__fecha=fecha
        self.__descripcion=descripcion
        self.__tipo=tipo
        self.__importe=importe
    def getnro(self):
        return self.__nrocuenta
    def getfecha(self):
        return self.__fecha
    def getdescripcion(self):
        return self.__descripcion
    def gettipo(self):
        return self.__tipo
    def getimporte(self):
        return self.__importe
    def __lt__(self,otro):
        return (self.getnro()<otro.getnro())