import string
alunos = []

while True:
    aluno = string.capwords(input("\nInforme o nome do aluno: "))
    alunos.append(aluno)

    resposta = input("Deseja informar outro nome [S|N]? ").upper()
    if resposta == "N":
        break
    elif resposta == "S":
        continue
    else:
        print("\nOpção inválida.\n")

alunos.sort()

print(f"\nA lista contém {len(alunos)} alunos.")
print("\nNomes informados, em ordem alfabética:\n")
for aluno in alunos:
    print(aluno)
print("")