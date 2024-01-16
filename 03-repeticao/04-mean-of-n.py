N = float(input("Informe o valor de N: "))
x = 0
sum = 0

while x < N:
    sum += float(input(f"Informe o {x + 1}º número: "))
    x += 1

media = sum / N

print(f"A média aritmética dos {N} valores informados é {media:.2f}.")