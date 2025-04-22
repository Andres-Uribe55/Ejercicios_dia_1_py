entrada = input("Ingresa tu peso: ")
peso = float(entrada.replace("kg", "").replace(" ", ""))
entrada_2 = input("Ingresa tu altura: ")
altura = float(entrada_2.replace("m", "").replace(" ", ""))
IMC = peso / (altura ** 2) 
if IMC < 18.5:
    print("Bajo peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
elif IMC >= 25 and IMC <= 29.9:
    print("Sobre peso")
elif IMC >= 30:
    print("Obesidad")

