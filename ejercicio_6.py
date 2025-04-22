numero_secreto = 7
intento = None
while intento != numero_secreto:
    intento = int(input("Adivina el número secreto (entre 1 y 20): "))
    if intento < numero_secreto:
        print("Demasiado bajo")
    elif intento > numero_secreto:
        print("Demasiado alto")
    else:
        print("¡Adivinaste!")