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
