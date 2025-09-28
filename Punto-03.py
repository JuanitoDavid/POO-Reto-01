numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def primos(numeros):

    primos = []

    for num in numeros:
        
        if num > 1:

            esprimo = True

            for i in range(2, num):

                if num % i == 0:
                    esprimo = False
                    break

            if esprimo:
                primos.append(num)

    return primos

resultado = primos(numeros)
print(resultado)