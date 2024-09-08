from gestormiembro import gestormiembros
from gestorvizualizaciones import gestorvizualizacion
def main():
    opcion = 1
    gestorM = gestormiembros()
    gestorV = gestorvizualizacion()
    while opcion != -1:
        opcion= int(input(""" MENU DE OPCIONES
                        1 minutos de vizualizacion de un usuario
                        2  vizualizaciones simultaneas
                        3 finalizar con -1: """))
        if opcion==1:
            correo = input("Ingrese el correo del miembro: ")
            gestorM.minutosVisualizados(gestorV, correo)
        if opcion==2:
            gestorV.visualizacionesSimultaneas(gestorM)

if __name__ == "__main__":
    main()