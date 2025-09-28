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