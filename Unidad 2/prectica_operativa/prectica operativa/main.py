from gestorcliente import gestorcliente
from gestormovimiento import gestormovimiento
def main():
    option:int
    option=1
    movimientos=gestormovimiento()
    clientes=gestorcliente()
    while option!=-1:
        option=int(input("""ingrese la opcion
                         1 actualizar saldo
                         2 informar si un cliente tuvo movimientos
                         3 ordenar movimientos
                         -1 detener"""))
        if option==1:
            dni=input("ingrese dni")
            clientes.actualizar(dni,movimientos)
if __name__=="__main__":
    main()            