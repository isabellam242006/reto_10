# reto_10
1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

```python
lista=[]                            #Lista vacía
while True:                         #Este bucle permite imprimir el mensaje varias veces hasta que no se ingrese ningún valor
  entrada = input("Ingrese un número real(Vacío para terminar): ")  
  if not entrada:
     break
  numeros=float(entrada)   
  lista.append(numeros)             #Se llena la lista con los números ingresados

promedio = sum(lista)/len(lista)    #Se calcula el promedio teniendo en cuenta el número de elementos de la lista
print("El promedio de los números ingresados es: " + str(promedio))
```
2. Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

*Los pasos a seguir fueron los siguientes:*

- Se crean dos arreglos de la misma forma que se hizo en el punto 1
- Si los dos arreglos tienen longitudes distintas, se imprime un mensaje ya que no es posible hacer ninguna operación
- Se realiza una iteración por cada elemento del primer arreglo
- Se multiplica cada elemento de la lista 1 con la lista 2 y luego se van sumando los resultados iterativamente
```python
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
```
3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
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
```
4. Revisar que son los algoritmos de sorting, entender bubble-sort (enlace a implementación).

**Algoritmos de sorting:**
Los algoritmos de ordenamiento nos permite, como su nombre lo dice, ordenar información de una manera especial basándonos en un criterio de ordenamiento.

**Existen dos tipos de algoritmos de ordenamiento**:

*Algoritmos estables*:

- Ordenamiento por inserción
- Ordenamiento de burbuja (Bubble-sort)*
- Ordenamiento de burbuja bidireccional
- Ordenamiento Gnome
- Ordenamiento por mezcla

*Algoritmos inestables*:

- Ordenamiento por selección.
- Ordenamiento peine.
- Ordenamiento Shell.
- Ordenamiento por montículos.
-	Ordenamiento rápido.

**Bubble Sort**:

*En este algoritmo:*

- Recorra desde la izquierda y compare los elementos adyacentes y el superior se coloca en el lado derecho. 
- De esta manera, el elemento más grande se mueve primero hacia el extremo derecho. 
- Luego se continúa con este proceso para encontrar el segundo más grande y colocarlo y así sucesivamente hasta que se ordenen los datos.

**Código ejemplo:**
```python
def bubble_sort(arr):
    n = len(arr)  # Calcula la longitud de la lista
    for i in range(n):  # Bucle externo para controlar los pases
        for j in range(0, n-i-1):  # Bucle interno para comparar elementos
            if arr[j] > arr[j+1]:  # Compara elementos adyacentes
                # Si el elemento actual es mayor que el siguiente, intercámbialos
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lista)  # Llama a la función de ordenamiento de burbuja
print("Lista ordenada:", lista)  # Imprime la lista ordenada
```
El código anterior ejemplifica el uso de iteraciones para ordenar cierta cantidad de elementos de una lista. Si un número es mayor que el otro y se encuentra a la izquierda de éste, lo que se hará es intercambiar las posiciones. Esto se hará de forma iterativa hasta llegar al último elemento, el cual tendrá que ser mayor que los demás.

**Enlaces de referencia**:

https://www.geeksforgeeks.org/bubble-sort/

http://lwh.free.fr/pages/algo/tri/tri_es.htm




