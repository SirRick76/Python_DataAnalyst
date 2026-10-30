import conversores
import areas
import math

# Exercicio 1
'''
def calcule_Perimetro(lado):
    perimetro=lado * 4
    return perimetro

lado=int(input("Insira o tamanho do lado"))
print(calcule_Perimetro(lado))
'''

# Exercicio 2 -- IFS
'''
def Calculadora(x,y,z):
    if z =="*":
        return x*y
    elif z == "+":
        return x+y
    elif z =="-":
        return x-y
    elif z =="/":
        if y == 0:
            return "Erro: Divisão por zero!"
        return x / y
    else:
        return "Não existe essa função"

z=input("Insira a função(/,-,*,+)")
x = float(input("Insira um valor "))
y = float(input("Insira outro valor "))
print (Calculadora(x,y,z))
'''
# Exercicio 2-- CASES
operacoes_validas = ["/", "-", "*", "+"]

z = input("Insira a função (/,-,*,+): ")

if z not in operacoes_validas:
  print("Não existe essa função")
else:
  x = float(input("Insira o primeiro valor: "))
  y = float(input("Insira o segundo valor: "))


  # Função simplificada apenas com as operações válidas
  def Calculadora(x, y, z):
    match z:
      case "*":
        return x * y
      case "+":
        return x + y
      case "-":
        return x - y
      case "/":
        if y == 0:
          return "Erro: Divisão por zero!"
        return x / y


  print(Calculadora(x, y, z))


#Exercicio 3

'''
nome=str(input("Insira o nome do aluno: "))
def mediaAluno(nota1,nota2,nota3):
        media=(nota1+nota2+nota3)/3
        return media

while True:
    nota1= float(input("Insira a primeira nota: "))
    if 0 <= nota1 <= 20:
        break  
    print("Nota inválida! Por favor, insira uma nota entre 0 e 20.")
while True:
    nota2= float(input("Insira a segunda nota: "))
    if 0 <= nota2 <= 20:
        break  
    print("Nota inválida! Por favor, insira uma nota entre 0 e 20.")
while True:
    nota3= float(input("Insira a terceira nota: "))
    if 0 <= nota3 <= 20:
        break  
    print("Nota inválida! Por favor, insira uma nota entre 0 e 20.")

media_final=mediaAluno(nota1,nota2,nota3)

def classificacao_Aluno(media):
    if media>=10:
        return "Aprovado"
    else:
        return "Reprovado"
print(f"O aluno {nome}  tem {media_final:.2f}  de media e encontra-se {classificacao_Aluno(media_final)}")
'''
# Exercicio 4
'''

while True:
    print("\n--- CONVERSOR DE MOEDAS ---")
    print("1. Converter para dolar(taxa 1.12)")
    print("2. Converter para libra(taxa 0.85)")
    print("3. Definir nova moeda")
    print("4. Sair")
    insira=int(input("Insira uma opção(1-4)"))
    match insira:
        case 1:
            taxa=1.12
            valor=float(input("Insira o valor que quer converter:"))
            print(f"{conversores.converter_moeda(valor,taxa):.2f}")
            
        case 2:
            taxa=0.85
            valor=float(input("Insira o valor que quer converter:"))
            print(f"{conversores.converter_moeda(valor,taxa):.2f}")
        case 3:
            taxa=float(input("Insira o valor da taxa de conversão:"))
            valor=float(input("Insira o valor que quer converter:"))
            print(f"{conversores.converter_moeda(valor,taxa):.2f}")    
        case 4:
            print("A sair do programa...")
            break
                    
        case _: # Caso o utilizador digite qualquer outra coisa
            print("Opção inválida! Tente novamente.")
'''

# Exercicio 5
'''
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
            print(f"O circulo tem de area {areas.area_circulo(raio):.2f}")
            
        case 2:
            base=float(input("Insira o valor da base : "))
            altura=float(input("Insira o valor da altura:"))
            print(f"O triangulo tem de area {areas.area_triangulo(base,altura):.2f}")
        case 3:
            comprimento=float(input("Insira o valor do comprimento: "))
            largura=float(input("Insira o valor da altura:"))
            print(f"O retangulo tem de area {areas.area_retangulo(comprimento,largura):.2f}")    
        case 4:
            print("A sair do programa...")
            break
                    
        case _: # Caso o utilizador digite qualquer outra coisa
            print("Opção inválida! Tente novamente.")
'''