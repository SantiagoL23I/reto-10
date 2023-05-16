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
