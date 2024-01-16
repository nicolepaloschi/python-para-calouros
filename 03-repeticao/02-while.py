print("COVID-19")

suspeitos = 0
num_pac = int(input("Informe a quantidade de pacientes: "))
cont = 0
print("\nInforme os sintomas:")

while cont <= num_pac:
    print(f"\n-----Paciente {cont + 1}-----\n")
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nResposta: "))
    febre = int(input("\nFebre? \n1. Sim \n2. Não \nResposta: "))
    dispneia = int(input("\nDispnéia? \n1. Sim \n2. Não \nResposta: "))


    if tosse == 1 and febre == 1 and dispneia == 1:
        suspeitos += 1
    
    cont += 1

print(f"\n{suspeitos} dos {num_pac} pacientes estão com suspeita de COVID-19.")