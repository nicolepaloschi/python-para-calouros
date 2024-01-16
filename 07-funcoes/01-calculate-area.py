from areaFunctions import *

def escolher_nova_forma():
    while True:
        calcular_novo = input("Deseja escolher uma nova forma [S|N]? ").upper()
        if calcular_novo not in ["S", "N"]:
            print("Opção inválida.")
            continue
        elif calcular_novo == "S":
            return True
        else:
            print("\n-----Encerrando...-----")
            return False


continuar_calculo = True
while continuar_calculo:
    print("\n-----Cálculo de área-----")
    print("1 - Círculo\n2 - Triângulo\n3 - Quadrado\n4 - Retângulo\n5 - Losango\n6 - Trapézio\n7 - Pentágono\n")
    forma = int(input("Escolha a forma cuja área deseja calcular: "))
    
    if forma <= 0 or forma > 7:
        print("Opção inválida.")
        continue
    elif forma == 1:
        print("Você escolheu círculo.")
        r = float(input("Informe a medida do raio: "))
        print(f"A área do círculo de raio {r:.2f} é {float(calculate_circle_area(r)):.2f}.\n")
        
        continuar_calculo = escolher_nova_forma()

    elif forma == 2:
        print("-----Triângulos-----")
        print("1 - Escaleno\n2 - Isósceles\n3 - Equilátero\n")
        triangulo = int(input("Qual tipo de triângulo? "))
        if triangulo == 1:
            print("\nVocê escolheu escaleno.")
            b = float(input("Informe a medida da base: "))
            h = float(input("Informe a medida da altura: "))
            print(f"A área do triângulo escaleno de base {b:.2f} e altura {h:.2f} é {float(calculate_triangle_area(b, h)):.2f}.\n")
            
            continuar_calculo = escolher_nova_forma()

        elif triangulo == 2:
            print("\nVocê escolheu isósceles.")
            b = float(input("Informe a medida da base: "))
            h = float(input("Informe a medida da altura: "))
            print(f"A área do triângulo isósceles de base {b:.2f} e altura {h:.2f} é {float(calculate_triangle_area(b, h)):.2f}.\n")
            
            continuar_calculo = escolher_nova_forma()

        elif triangulo == 3:
            print("\nVocê escolheu equilátero.")
            s = float(input("Informe a medida da lateral: "))
            print(f"A área do triângulo equilátero de lateral {s:.2f} é {float(calculate_equilateral_triangle_area(s)):.2f}.\n")
            
            continuar_calculo = escolher_nova_forma()
            
        else:
            print("Opção inválida.")
            continue
    
    elif forma == 3:
        print("Você escolheu quadrado.")
        s = float(input("Informe a medida da lateral: "))
        print(f"A área do quadrado de {s:.2f} é {float(calculate_square_area(s)):.2f}.\n")

        continuar_calculo = escolher_nova_forma()
    
    elif forma == 4:
        print("Você esoclheu retângulo.")
        b = float(input("Informe a medida da base: "))
        h = float(input("Informe a medida da altura: "))
        print(f"A área do retângulo de base {b:.2f} e altura {h:.2f} é {float(calculate_rectangle_area(b, h)):.2f}.\n")

        continuar_calculo = escolher_nova_forma()
    
    elif forma == 5:
        print("Você escolheu losango.")
        while True:
            D = float(input("Informe a medida da diagonal maior: "))
            d = float(input("Informe a medida da diagonal menor: "))
            if d > D:
                print("A diagonal menor não pode ser menor do que a diagonal maior.")
                continue
            print(f"A área do losango de diagonais {D:.2f} e {d:.2f} é {float(calculate_rhombus_area(D, d)):.2f}.\n")
            break
        continuar_calculo = escolher_nova_forma()
    
    elif forma == 6:
        print("Você escolheu trapézio.")
        b = float(input("Informe a medida da base superior: "))
        B = float(input("Informe a medida da base inferior: "))
        h = float(input("Informe a altura: "))
        print(f"A área do trapézio de bases {b:.2f} e {B:.2f} é {float(calculate_trapezoid_area(B, b, h)):.2f}.\n")

        continuar_calculo = escolher_nova_forma()
    
    elif forma == 7:
        print("Você escolheu pentágono.")
        s = float(input("Informe a medida da lateral: "))
        print(f"O pentágono de lateral {s:.2f} é {float(calculate_penthagon_area(s)):.2f}.\n")

        continuar_calculo = escolher_nova_forma()

        