import random

print("\n-----Sorteio de rifa-----\n")
nomes = []

while True:
    nome = input("Informe o nome do comprador: ")
    nomes.append(nome)
    resposta = input("Deseja informar um novo comprador [S|N]? ").upper()

    while resposta not in ["S", "N"]:
        print("Opção inválida.")
        resposta = input("Deseja informar um novo comprador [S|N]? ")

    if resposta == "N":
        break

random.shuffle(nomes)
sorteado = random.choice(nomes)

print(f"\nO nome sorteado foi: {sorteado}")