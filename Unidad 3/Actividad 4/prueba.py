arreglo = [6,2,3,1,4,0,5]
print(arreglo)
N = 7
cota = N - 1
k = 1
while(k != -1):
   k = -1
   for i in range(cota-1):
      if arreglo[i] > arreglo[i+1]:
         aux = arreglo[i]
         arreglo[i] = arreglo[i+1]
         arreglo[i+1] = aux
         k = i
   cota = k
print(arreglo)