x = 0
n = 0
even = 0

while x < 5:
    n = int(input(f"Informe o {x + 1}º número: "))
    
    if n < 0 or not n.is_integer():
        print("O número deve ser um inteiro positivo.\n")
        continue
    elif n % 2 == 0:
        even += 1

    x += 1

if even == 5:
    print("Todos os números informados são pares.")
elif even == 0:
    print("Nenhum número informado é par.")
else:
    print(f"{even} dos números informados são pares.")