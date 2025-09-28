numeros = [3, 4, 5, 6, 7, 8, 9]

def mayorsumaconsecutivos(numeros):

    if len(numeros) < 2:
        
        print("Error: no hay suficientes elementos para comparar")
        return None
    
    mayorsuma = numeros[0] + numeros[1]
    
    for i in range(1, len(numeros) - 1):

        suma = numeros[i] + numeros[i + 1]

        if suma > mayorsuma:
            mayorsuma = suma
    
    return mayorsuma

resultado = mayorsumaconsecutivos(numeros)
print(resultado)