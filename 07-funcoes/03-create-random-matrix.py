import random

def generate_random_matrix(rows, cols):
    m = []
    for i in range(rows):
        row = []
        for j in range(cols):
            num = random.randint(1, 10)
            row.append(num)
        m.append(row)

    return m

def print_random_matrix(m):
    rows = len(m)
    cols = len(m[0])

    for i in range(rows):
        for j in range(cols):
            print(m[i][j], end = "\t")
        print("")
    print("")


print("\n-----Matriz de valores aleatórios [1 a 10]-----")
while True:
    rows = int(input("Informe a quantidade de linhas: "))
    if rows <= 0:
        print("A matriz deve ter pelo menos uma linha.")
        continue
    else:
        break

while True:
    cols = int(input("Informe a quantidade de colunas: "))
    if cols <= 0:
        print("A matriz deve ter pelo menos uma coluna.")
        continue
    else:
        break

m = generate_random_matrix(rows, cols)

print("")
print_random_matrix(m)
