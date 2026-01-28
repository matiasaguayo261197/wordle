cantidad_letras = 5

def verificador_palabra(palabra_ingresada, palabra_secreta):
    letras_verificadas = []

    for i in range(cantidad_letras):
        if palabra_ingresada[i] == palabra_secreta[i]:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")  # letra correcta
        elif palabra_ingresada[i] in palabra_secreta:
            letras_verificadas.append(f"({palabra_ingresada[i]})")  # existe pero mal lugar
        else:
            letras_verificadas.append(palabra_ingresada[i])         # no existe

    return letras_verificadas


palabra_secreta = "calor"
intentos = 0
max_intentos = 6

while intentos < max_intentos:
    print(f"Te quedan {max_intentos - intentos} intentos")
    palabra_ingresada = input("Ingrese una palabra: ").lower()

    if palabra_ingresada == palabra_secreta:
        print(" ¡Ganaste! Adivinaste la palabra ")
        break

    resultado = verificador_palabra(palabra_ingresada, palabra_secreta)
    print("Resultado:", " ".join(resultado))

    intentos += 1

else:
    print(f" Perdiste. La palabra era: {palabra_secreta}")