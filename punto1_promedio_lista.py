lista=[]                            #Lista vacía
while True:                         #Este bucle permite imprimir el mensaje varias veces hasta que no se ingrese ningún valor
  entrada = input("Ingrese un número real(Vacío para terminar): ")  
  if not entrada:
     break
  numeros=float(entrada)   
  lista.append(numeros)             #Se llena la lista con los números ingresados

promedio = sum(lista)/len(lista)    #Se calcula el promedio teniendo en cuenta el número de elementos de la lista
print("El promedio de los números ingresados es: " + str(promedio))