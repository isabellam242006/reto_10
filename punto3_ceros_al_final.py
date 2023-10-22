lista1 = []
while True:
  entrada = input("Ingrese un número(Vacío para tertminar): ")
  if not entrada:
    break
  numeros = float(entrada)
  lista1.append(numeros)

lista1_copia = list(lista1)        #La copia se realiza con el fin de tener intactos los elementos iniciales de la lista 1
lista2= []
num_ceros = lista1_copia.count(0)  #Cuenta el número de ceros

for i in range(num_ceros):         #Se ejecuta el número de veces que se encuentre un 0
    lista1_copia.remove(0)         #Remueve todos los ceros de la lista 1
    lista2.append(0)               #Agrega todos los ceros a la lista 2

lista3 =  lista1_copia + lista2    #Concatena la lista 1 (Sin los ceros) y la lista 2(Con todos los ceros, quedando al final de la lista 3)

print("La lista dada es: ")
print(lista1)
print("La lista con todos los ceros al final es: ")
print(lista3)