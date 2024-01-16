n = int(input("Informe o número de elementos na lista: "))
lista = []
x = 0

for x in range(n):
    elem = int(input(f"Informe o valor do {x + 1}º elemento: "))
    lista.append(elem)
    x += 1

print("\n---------------------------------")
print(f"O menor elemento da lista é {min(lista)}.")
print(f"O maior elemento da lista é {max(lista)}.")

media = (sum(lista) / len(lista))
print(f"A soma dos elementos é {sum(lista)}.")
print(f"A média dos elementos é {media}.")
print("---------------------------------")