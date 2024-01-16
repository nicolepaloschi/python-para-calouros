masc = 0
fem = 0
total = 0
sum = 0

while True:
    idade = int(input("Informe a idade: "))
    sexo = input("Informe o sexo [M|F|NB]: ").upper()
    
    if sexo not in ["M", "F", "NB"]:
        print("Opção inválida.")
        continue
    total += 1

    if sexo == "M" and idade > 18:
        masc += 1
    elif sexo == "F":
        sum += idade
        fem += 1
    

    add_new = input("\nDeseja informar um novo registro [S|N]? ").upper()
    if add_new not in ["S", "N"]:
        print("Opção inválida.")
        add_new = input("\nDeseja informar um novo registro [S|N]? ")
    elif add_new == "N":
        print("Encerrando a contagem...")
        break

if masc == 0:
    print(f"Dos {total} alunos, nenhum é do sexo masculino.")
elif masc == 1:
    print(f"Dos {total} alunos, 1 é do sexo masculino e acima de 18 anos.")
else:
    print(f"Dos {total} alunos, {masc} são do sexo masculino e acima de 18 anos.")

if fem == 0:
    print(f"Dos {total} alunos, nenhum é do sexo feminino.")
else: 
    avg = sum / fem
    if avg == 1:
        print(f"A média de idade do sexo feminino é 1 ano.")
    else:
        print(f"A média de idade do sexo feminino é {avg:.2f} anos.")
    
