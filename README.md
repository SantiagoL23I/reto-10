# reto-10
##1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```pseudocode
def calcularPromedio(arreglo):
    if len(arreglo) == 0: # Verificar si el arreglo está vacío
        print("El arreglo está vacío.")
        return
    suma = sum(arreglo)  # Calcular la suma de los elementos del arreglo
    promedio = suma / len(arreglo)  # Calcular el promedio dividiendo la suma entre la longitud del arreglo
    return promedio # Devolver el promedio calculado
arreglo = [2.5, 3.7, 1.8, 4.2, 2.1]
promedio = calcularPromedio(arreglo)
print("El promedio del arreglo es:" +str(promedio))
```
##2.Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.
```pseudocode
def calcularProductoPunto(arreglo1, arreglo2):
    if len(arreglo1) != len(arreglo2): # Verificar si los arreglos tienen la misma longitud
        print("Los arreglos no tienen la misma longitud.")
        return 
    productoPunto = 0 # Inicializar la variable para el producto punto
    for i in range(len(arreglo1)): # Calcular el producto punto
        productoPunto += arreglo1[i] * arreglo2[i]
    return productoPunto   # Devolver el resultado del producto punto
arreglo1 = [1, 2, 3]
arreglo2 = [4, 5, 6]
resultado = calcularProductoPunto(arreglo1, arreglo2) #llamar función del producto punto
print("El producto punto de los arreglos es:"+str(resultado))
```
3.Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```pseudocode
def moverCeros(arreglo):
    ceros = []  # Crear una lista para almacenar los ceros
    for num in arreglo:# Recorrer el arreglo y separar los ceros
        if num == 0:
            ceros.append(num)
    arreglo = [num for num in arreglo if num != 0]   # Eliminar los ceros del arreglo original
    arreglo.extend(ceros)    # Agregar los ceros al final del arreglo
    return arreglo
arreglo = [2, 0, 4, 0, 1, 0, 3]
arregloResultante = moverCeros(arreglo) #llamar función de mover ceros
print("Arreglo resultante:" +str(arregloResultante))
```
