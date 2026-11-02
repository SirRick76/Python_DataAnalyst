import math
def area_circulo(raio):
    return math.pi*raio**2

def area_triangulo(base,altura):
    return (base*altura)/2

def area_retangulo(comprimento,largura):
    return comprimento*largura

def menu_areas(insira):
    while True:
        print("\n--- CALCULO DE AREAS ---")
        print("1. Área do círculo")
        print("2. Área do triangulo")
        print("3. Área do retângulo ")
        print("4. Sair")
        insira=int(input("Insira uma opção(1-4): "))
        match insira:
            case 1:
                raio=float(input("Insira o valor do raio: "))
                print(f"O circulo tem de area {area_circulo(raio):.2f}")
                
            case 2:
                base=float(input("Insira o valor da base : "))
                altura=float(input("Insira o valor da altura:"))
                print(f"O triangulo tem de area {area_triangulo(base,altura):.2f}")
            case 3:
                comprimento=float(input("Insira o valor do comprimento: "))
                largura=float(input("Insira o valor da altura:"))
                print(f"O retangulo tem de area {area_retangulo(comprimento,largura):.2f}")    
            case 4:
                print("A sair do programa...")
                break
                        
            case _: # Caso o utilizador digite qualquer outra coisa
                print("Opção inválida! Tente novamente.")