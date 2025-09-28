# POO-Reto-01
Solución del Reto #01 de la Asignatura Programación Orientada a Objetos - UNAL

## Punto 01
Se solicita al usuario dos numeros y el simbolo de la operacion que desea realizar, se define la funcion `calculadora()` que recibe los parametros como se solicita en el enunciado del problema, mediante una estructura `if` `elif` `else` se evalua el operador ingresado teniendo en cuenta que no es posible dividir por 0 y que se debe ingresar una operacion valida. si la entrada es valida, se realiza la operacion y retorna el resultado. Finalmente, se llama a la funcion para mostrar el resultado. 
```python
n1 = float(input(("Numero 1: ")))
n2 = float(input(("Numero 2: ")))
operacion = str(input(("Operacion +,-,*,/ : ")))

def calculadora(n1, n2, operacion):

    if operacion == "+":
        return n1 + n2

    elif operacion == "-":
        return n1 - n2

    elif operacion == "*":
        return n1 * n2

    elif operacion == "/":

        if n2 != 0:
            return n1 / n2
        else: return "Error: division por 0"

    else: return "Error: entrada no valida"

resultado = calculadora(n1, n2, operacion)
print(resultado)
```
## Punto 02
Se solicita al usuario la palabra, se convierte a minuscula y se eliminan los espacios con los metodos correspondientes haciendo posible evaluar palabras con errores de entrada. se define la funcion `palindromo()` que recibe la palabra y con un bucle `while` recorremos la palabra hacia atras y la concatenamos, al final, `invertida` contiene la palabra invertida, que mediante un `if` evalua si `palabra` y `invertida` son iguales, retornando un mensaje correspondiente. Al llamar a la funcion esta indica si la palabra es un palindromo o no.
```python
palabra = str(input(("Palabra: "))).lower().replace(" ", "")

def palindromo(palabra):

    i = len(palabra) - 1  
    invertida = ""

    while i >= 0:
        invertida += palabra[i]
        i -= 1

    if palabra == invertida:
        return "Es palindromo"

    else: return "No es palindromo"
    
resultado = palindromo(palabra)
print(resultado)
```
## Punto 03
La funcion `primos()` recibe la lista con numeros, se crea una lista que guarda los primos encontrados. con un bucle `for` recorremos la lista y evaluamos solo los numeros mayores que 1 ya que los numeros negativos, 0 y 1 no pueden ser primos. comprobamos mediante un `if` anidado en un `for` si el numero tiene un divisor distinto de 1 y el mismo, si el numero es primo, lo añade a la lista. Al llamar a la funcion, devuelve una lista con los numeros que son primos.
```python
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
```
## Punto 04
La funcion `mayorsumaconsecutivos()` recibe una lista de numeros y, si la lista tiene dos o mas elementos calcula la suma del primer par como punto de partida y con un bucle `for` se recorre la lista y se suma cada par consecutivo. con un bucle `if` se actualiza la variable si se encuentra una suma mayor a la registrada. Al llamar a la funcion, se imprime la suma mas grande entre dos elementos consecutivos que se encuentre en la lista.
```python
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
```
## Punto 05
La funcion `anagramas()` (palabras que tienen las mismas letras en diferente orden) recibe una lista de `str`. El primer bucle `for` toma una palabra en la posición `i` mientras que el segundo bucle `for` toma otra palabra en la posicion `j` (`j = i+1`) mediante un `if` se ordenan con el metodo `sorted()` los caracteres de las palabras y se evalua si son iguales. Se agrega la pareja encontrada en la lista `resultado`, asegurandose de no repetir palabras. Al llamar a la funcion, retorna unicamente aquellos elementos que tengan los mismos caracteres.
```python
palabras = ["amor", "perro", "roma"]

def anagramas(palabras):

    resultado = []

    for i in range(len(palabras)):

        for j in range(i+1, len(palabras)):

            if sorted(palabras[i]) == sorted(palabras[j]):

                if palabras[i] not in resultado:
                    resultado.append(palabras[i])

                if palabras[j] not in resultado:
                    resultado.append(palabras[j])

    return resultado

resultado = anagramas(palabras)
print(resultado)
```
