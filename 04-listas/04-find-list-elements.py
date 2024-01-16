n = int(input("Quantos competidores deseja informar? "))
nomes = []
tempos = []

for i in range(n):
    nome = input(f"Informe o nome do {i + 1}º competidor: ")
    nomes.append(nome)
    t = float(input("Informe o tempo (s): "))
    tempos.append(t)

index_melhor = tempos.index(min(tempos))
index_pior = tempos.index(max(tempos))

if index_melhor == index_pior:
    print(f"\nO melhor e o pior tempo são iguais: {tempos[index_melhor]}s.")
else:
    print(f"\n{nomes[index_melhor]} fez o melhor tempo: {tempos[index_melhor]}s.")
    print(f"{nomes[index_pior]} fez o pior tempo: {tempos[index_pior]}s")