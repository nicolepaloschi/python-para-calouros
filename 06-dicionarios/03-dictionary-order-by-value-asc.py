from operator import itemgetter

nomes = {}

while True:
    novo_nome = input("Informe o nome: ")
    nova_idade = input("Informe a idade: ")
    nomes.update({novo_nome: nova_idade})

    resposta = input("\nDeseja registrar mais dados? [S|N] ").upper()
    if resposta not in ["S", "N"]:
        print("Opção inválida.")
        resposta = input("\nDeseja registrar mais dados? [S|N] ").upper()
    elif resposta == "N":
        break

print("\n-----Lista de contatos por idade, em ordem crescente-----\n")
for nome, idade in sorted(nomes.items(), key=itemgetter(1)):
    print(f"{nome} tem {idade} anos.")
print("")