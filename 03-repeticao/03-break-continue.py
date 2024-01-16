print("COVID-19")

suspeitos = 0
num_pac = 0
print("\nInforme os sintomas:")

while True:
    num_pac += 1
    tosse = int(input("Tosse? \n1. Sim \n2. Não \nResposta: "))
    febre = int(input("\nFebre? \n1. Sim \n2. Não \nResposta: "))
    dispneia = int(input("\nDispnéia? \n1. Sim \n2. Não \nResposta: "))


    if tosse == 1 and febre == 1 and dispneia == 1:
        suspeitos += 1
    
    resposta = input("\nDeseja informar um novo paciente [S|N]? \nResposta: ")
    
    if resposta.upper() == "S":
        continue
    else:
        break


print(f"\n{suspeitos} dos {num_pac} pacientes estão com suspeita de COVID-19.")