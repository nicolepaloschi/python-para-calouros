n = int(input("Quantos elementos deseja na sua lista? "))
lista = []

for x in range(n):
    elem = int(input(f"Informe o {x + 1}º elemento: "))
    lista.append(elem)

resposta = input("Digite P para remover os elementos pares ou I para remover os elementos ímpares: ").upper()

if resposta == "P":
    lista = [elem for elem in lista if elem % 2 != 0]
    if len(lista) == n:
        print("Não há elementos pares na lista.")
    elif len(lista) == 0:
        print("Todos os elementos eram pares, portanto, a lista está vazia.")
    elif len(lista) == 1:
        print("Número ímpar da lista:", lista)
    else:
        print("Números ímpares da lista:", lista)
elif resposta == "I":
    lista = [elem for elem in lista if elem % 2 == 0]
    if len(lista) == n:
        print("Não há elementos ímpares na lista.")
    elif len(lista) == 0:
        print("Todos os elementos eram ímpares, portanto, a lista está vazia.")
    elif len(lista) == 1:
        print("Número par da lista:", lista)
    else:
        print("Números pares da lista:", lista)
else:
    print("A opção selecionada é inválida.")


