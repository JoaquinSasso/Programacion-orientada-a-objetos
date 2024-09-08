from GestorClientes import GestorC
from GestorMovimientos import GestorM
GM=GestorM()
GC=GestorC()
def menu():
    GC.test()
    GM.test()
    k=-1
    while(k!=0):
        opcion=int(input("ingresar una opcion:\n1.Modificar saldo de cliente\n2.Informar movimientos de un cliente \n3. salir\n"))
        if opcion==3:
            k=0
        elif (opcion==1):
            GC.modifsaldo(GM)
        elif(opcion==2):
            GM.informar(GC)
        elif opcion == 4:
            GM.ordenar()
if __name__=='__main__':
    menu()