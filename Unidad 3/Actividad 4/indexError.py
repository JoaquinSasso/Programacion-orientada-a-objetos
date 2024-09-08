lista = [0,3,1]
indice = int(input("Ingrese el indice: "))
try:
   print(lista[indice])
except IndexError:
   print(f"El indice ingresado esta fuera de rango, ingrese uno dentro de: (0,{(len(lista))-1})")
   indice = int(input("Ingrese el indice: "))
   print(lista[indice])