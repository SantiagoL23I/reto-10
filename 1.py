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
