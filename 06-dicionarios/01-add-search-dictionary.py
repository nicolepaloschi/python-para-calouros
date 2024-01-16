contatos = {"@nicolepaloschi": "Nicole Paloschi",
		    "@knob.andre": "André Knob"}

contatos.update({"@nicolepaloschi": "Nicole Gabriele Paloschi"})
contatos.update({"@alinefirak": "Aline Firak"})

while True:
    busca_contato = input("\nInforme o @ do contato que deseja buscar: ")
    
    if busca_contato in contatos:
        print(f"Este contato pertence a {contatos.get(busca_contato)}\n.")
    else:
        print(f"\"{busca_contato}\" não foi encontrado.")
        while True:
            adicionar_novo = input("\nDeseja adicionar um novo contato? [S|N] ").upper()
            if adicionar_novo not in ["S", "N"]:
                print("Opção inválida.")
            elif adicionar_novo == "S":
                novo_contato = input("Informe o novo contato, iniciado com @: ")
                novo_nome = input("Informe o nome da pessoa a quem o contato pertence: ")
                contatos.update({novo_contato:novo_nome})
                print("\n-----Contato adicionado com sucesso!-----")
            else:
                break

    resposta = input("Deseja realizar uma nova busca? [S|N] ")
    if resposta not in ["S", "N"]:
        print("Opção inválida.")
        resposta = input("Deseja realizar uma nova busca? [S|N] ")
    elif resposta == "N":
        print("\nEncerrando...")
        break
