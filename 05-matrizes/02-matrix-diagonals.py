import random

order = int(input("Informe a ordem da matriz: "))
if order >= 2:
    while True:
        m = []
        for i in range(order):
            row = []
            for j in range(order):
                num = random.randint(1, 11)
                row.append(num)
            m.append(row)
        break

    main = []
    secondary = []
    
    for i in range(order):
        for j in range(order):
            print(m[i][j], end = " ")
            if i == j:
                main.append(m[i][j])
            elif i + j == (order - 1):
                secondary.append(m[i][j])
        print("")
    
    max_main = max(main)
    min_secondary = min(secondary)
    avg = (max_main + min_secondary) / 2

    print(f"A média da matriz é {avg:.2f}")

else:
    print("Informe uma ordem válida.")