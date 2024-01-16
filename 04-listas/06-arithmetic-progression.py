print("\n-----Cálculo de Progressão Aritmética-----")

pa = []
primeiro_termo = float(input("\nInforme o valor do primeiro termo: "))
n = int(input("Informe a quantidade de termos: "))
r = float(input("Informe a razão da PA: "))

for i in range(n):
    termo_atual = primeiro_termo + i * r
    pa.append(termo_atual)

soma = sum(pa)

print(f"\nTermos da PA: {pa}.")
print(f"Soma dos termos da PA: {soma}.")