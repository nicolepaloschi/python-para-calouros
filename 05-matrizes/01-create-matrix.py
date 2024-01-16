import random

while True:
    rows = int(input("Informe a quantidade de linhas: "))
    
    if rows <= 0:
        print("O número de linhas deve ser maior do que zero.")
    else:
        break

while True: 
    cols = int(input("Informe a quantidade de colunas: "))
    
    if cols <= 0:
        print("O número de colunas deve ser maior do que zero.")
    else:
        break

m = []
for i in range(rows):
    row = []
    for j in range(cols):
        num = random.randint(1, 11)
        row.append(num)
    m.append(row)
    
for i in range(rows):
    for j in range(cols):
        print(m[i][j], end = "\t")
    print("")