import random    #argar el módulo estándar random de Python, que permite generar valores aleatorios.

cantidad_letras = 5

# Lista de palabras válidas (todas de 5 letras)
palabras_validas = [
    "calor",
    "perro",
    "gatos",
    "nubes",
    "fuego",
    "playa",
    "raton",
    "luces"
]
# hacemos la funcion de verificador de palabra 
def verificador_palabra(palabra_ingresada, palabra_secreta):
    letras_verificadas = []

    for i in range(cantidad_letras):
        if palabra_ingresada[i] == palabra_secreta[i]:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")  # correcta
        elif palabra_ingresada[i] in palabra_secreta:
            letras_verificadas.append(f"({palabra_ingresada[i]})")  # existe, mal lugar
        else:
            letras_verificadas.append(palabra_ingresada[i])         # no existe

    return letras_verificadas


#  Palabra secreta elegida al azar
palabra_secreta = random.choice(palabras_validas)

intentos = 0
max_intentos = 6

while intentos < max_intentos:
    print(f"Te quedan {max_intentos - intentos} intentos")
    palabra_ingresada = input("Ingrese una palabra: ").lower()

    # Validación básica
    if len(palabra_ingresada) != cantidad_letras:
        print(f"La palabra debe tener {cantidad_letras} letras")
        continue

    if palabra_ingresada == palabra_secreta:
        print("¡Ganaste! Adivinaste la palabra")
        break

    resultado = verificador_palabra(palabra_ingresada, palabra_secreta)
    print("Resultado:", " ".join(resultado))

    intentos += 1
else:
    print(f"Perdiste. La palabra era: {palabra_secreta}")
