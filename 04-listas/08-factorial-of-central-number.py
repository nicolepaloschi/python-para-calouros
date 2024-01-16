while True:
    try:
        n = int(input("Quantos elementos deseja informar?\n Deve ser um número ímpar, inteiro, maior do que 1: "))
        if n <= 1:
            print("A quantidade de elementos deve ser maior do que 1.\n")
        elif n % 2 == 0:
            print("A quantidade de elementos deve ser ímpar.\n")
        else:
            break
    except ValueError:
        print("A quantidade de elementos deve ser um número inteiro.\n")

numeros = []

for i in range(n):
    try:
        numero = int(input("Informe um número inteiro positivo: "))
        if numero < 0:
            print("O número deve ser positivo.")
        else:
            numeros.append(numero)
    except ValueError:
        print("O número deve ser inteiro.")

index_centro = int(len(numeros) / 2)
print(f"O elemento central é {numeros[index_centro]}.")
    
fatorial = 1
for n in range(1, numeros[index_centro] + 1):
    fatorial = fatorial * n
print(f"{numeros[index_centro]}! é igual a {fatorial}.")
