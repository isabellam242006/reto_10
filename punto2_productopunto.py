primer_arreglo = [] 
segundo_arreglo = []

#Creación y entrada de datos del primer arreglo
while True:
  entrada1 = input("Ingrese un número entero para el primer arreglo(Vacío para terminar): ")
  if not entrada1:
     break
  numeros1=int(entrada1)
  primer_arreglo.append(numeros1)

#Creación y entrada de datos del segundo arreglo
while True:
  entrada2 = input("Ingrese un número entero para el segundo arreglo(Vacío para terminar): ")
  if not entrada2:
     break
  numeros2= int(entrada2)
  segundo_arreglo.append(numeros2)

if len(primer_arreglo) != len(segundo_arreglo):
  print("Los arreglos no tienen el mismo tamaño.")
else:
    producto_punto = 0
    for i in range(len(primer_arreglo)):                        
      producto_punto += primer_arreglo[i] * segundo_arreglo[i]    
    print("El producto punto de los dos arreglos es " + str(producto_punto))