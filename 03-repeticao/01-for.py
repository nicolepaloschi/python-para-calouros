print("COVID-19")

suspeitos = 0

num_pac = int(input("Informe a quantidade de pacientes: "))
print("\nInforme os sintomas:")

for x in range(num_pac):
    print("\n-----Paciente {}-----\n".format(x + 1))
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nResposta: "))
    febre = int(input("\nFebre? \n1. Sim \n2. Não \nResposta: "))
    dispneia = int(input("\nDispnéia? \n1. Sim \n2. Não \nResposta: "))


    if tosse == 1 and febre == 1 and dispneia == 1:
        suspeitos += 1

print(f"\n{suspeitos} dos {num_pac} pacientes estão com suspeita de COVID-19.")