from operator import itemgetter

produtos = {1:["Monitor LED 24\"", 599.99, 1],
            2: ["Teclado wireless", 309.59, 1],
            3: ["Mouse wireless", 89.90, 1],
            4: ["Mouse pad", 35.99, 2]
            }

# print(produtos)
carrinho = {}

while True:
    print("\n-----Tabela de produtos-----")
    print("1 - Monitor\n2 - Teclado sem fio\n3 - Mouse sem fio\n4 - Mouse pad\n")
    novo_codigo = int(input("Infome o código do produto que deseja adquirir: "))
    if novo_codigo not in produtos.keys():
        print("Código inválido.")
        continue
   
    novo_nome, preco_unitario, _ = produtos[novo_codigo]
    
    nova_qtde = int(input("Informe quantos itens deseja adquirir: "))
    if nova_qtde <= 0:
        print("Você deve escolher pelo menos um item de cada produto.\n")
        continue

    carrinho.update({novo_codigo: [novo_nome, preco_unitario, nova_qtde]})
    print("\n-----Carrinho-----")
    total = 0
    for item, detalhes in carrinho.items():
        nome, preco, qtde = detalhes
        subtotal = preco * qtde
        total += subtotal
        print(f"{nome}\nPreço unitário: R${preco:.2f}\nQuantidade: {qtde}\nSubtotal: R${subtotal:.2f}\n")
    print("--------------------------\n")

    continuar_comprando = input("Deseja adquirir um novo item [S|N]? ").upper()
    if continuar_comprando not in ["S", "N"]:
        print("Opção inválida.")
        continuar_comprando = input("Deseja adquirir um novo item [S|N]? ").upper()
    elif continuar_comprando == "N":
        break
    
print("\n-----Resumo da compra-----")
for item, detalhes in sorted(carrinho.items(), key = itemgetter(1)):
    nome, preco, qtde = detalhes
    subtotal = preco * qtde
    print(f"{nome}\nPreço unitário: R${preco:.2f}\nQuantidade: {qtde}\nSubtotal: R${subtotal:.2f}\n")
print("-----Total da compra-----")
print(f"R${total:.2f}")

