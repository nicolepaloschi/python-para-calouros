produtos = []

while True:
    produto = input("Informe o nome do produto: ")
    produtos.append(produto)
    resposta = input("Deseja informar um novo produto [S|N]? ").upper()
    
    while resposta not in ["S", "N"]:
        print("Opção inválida.")
        resposta = input("Deseja informar um novo produto [S|N]? ")

    if resposta == "N":
        break

for index, valor in enumerate(produtos):
	print(f"O índice {index} contém o produto {valor}.")
