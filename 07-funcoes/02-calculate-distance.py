import math

def calculate_distance(x1, y1, x2, y2):
    distancia = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return distancia

print("\n-----Cálculo de distância entre dois pontos-----")
x1 = float(input("Informe a longitude do primeiro ponto: "))
y1 = float(input("Informe a latitude do primeiro ponto: "))

x2 = float(input("\nInforme a longitude do segundo ponto: "))
y2 = float(input("Informe a latitude do segundo ponto: "))

print(f"A distância entre os pontos ({x1:.2f}, {y1:.2f}) e ({x2:.2f}, {y2:.2f}) é de {float(calculate_distance(x1, y1, x2, y2)):.2f}\n")