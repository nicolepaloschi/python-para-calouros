sexo = input("Informe o seu sexo: M - masculino, F - Feminino, NB - Não-binário: ").upper()
altura = float(input("Informe sua altura, em metros: "))

if sexo == "M":
    resultado = (72.7 * altura) - 58.0
    print(f"O seu peso ideal é de {resultado:.2f}kg.")
elif sexo == "F":
    resultado = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é de {resultado:.2f}kg.")
else:
    print("Não foi possível calcular seu peso ideal.")
