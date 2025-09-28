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