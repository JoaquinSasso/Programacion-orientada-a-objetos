class cliente:
    __nombre=str
    __apellido=str
    __dni=str
    __nrocuenta=int
    __saldoanterior=float
    def __init__(self,nomb,ap,dni,nro,saldo):
            self.__nombre=nomb
            self.__apellido=ap
            self.__dni=dni
            self.__nrocuenta=nro
            self.__saldoanterior=saldo

    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getdni(self):
        return self.__dni
    def getnro(self):
        return self.__nrocuenta
    def getsaldo(self):
        return self.__saldoanterior
    def modifsaldo(self, saldonuevo):
        self.__saldoanterior=saldonuevo