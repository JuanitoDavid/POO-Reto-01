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