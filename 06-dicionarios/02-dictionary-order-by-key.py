contatos = {}

while True:
    novo_contato = input("Informe o @ do contato que deseja adicionar: ")
    novo_nome = input("Informe o nome da pessoa a quem esse contato pertence: ")
    contatos.update({novo_contato: novo_nome})
    print("\n-----Contato adicionado com sucesso!-----")
    
    resposta = input("\nDeseja adicionar um novo contato? [S|N] ").upper()
    if resposta not in ["S", "N"]:
        print("Opção inválida.")
        resposta = input("Deseja adicionar um novo contato? [S|N] ")
    elif resposta == "N":
        break

print("\n-----Lista de contatos ordenada por nome-----\n")
for contato, nome in sorted(contatos.items()):
    print(f"{contato} pertence a {nome}.")
