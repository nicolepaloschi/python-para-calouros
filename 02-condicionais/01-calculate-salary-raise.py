cargo = input("Informe o seu cargo: ").lower()

if cargo == "programador" or cargo == "programadora":
    salario = float(input("Informe o seu salário atual: "))
    novoSalario = salario + (salario / 2)
    print(f"Seu novo salário será de R${novoSalario:.2f}.")
elif cargo == "analista de sistemas":
    salario = float(input("Informe o seu salário atual: "))
    novoSalario = salario + ((salario * 40) / 100)
    print(f"Seu novo salário será de R${novoSalario:.2f}.")
elif cargo == "analista de banco de dados":
    salario = float(input("Informe o seu salário atual: "))
    novoSalario = salario + ((salario * 30) / 100)
    print(f"Seu novo salário será de R${novoSalario:.2f}.")
else:
    print("O cargo informado é inválido.")
