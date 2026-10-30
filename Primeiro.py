"""@package docstring
Documentation for this module.
 
More details.
"""
print("Primeiras impressões")
nome = "Cesae"
saudacao= "Bom dia"
print(saudacao,nome)

def my_function():
  print("Ola, mundo!") 

my_function()

## Performs safe division.

def divide(c, d):
    return c / d

print(divide(10, 2))

def soma(c,d):
   return c+d

print(soma(10,2))

nome =input("Digite seu nome: ")
print("Olá",nome,"!")


##    Calcula o valor final de um produto com base no desconto aplicável.

#    @param preco: O valor original do produto.
#    @param percentagem: A taxa de desconto (0 a 100).
#    @return: O preço final com o desconto aplicado.

def calcular_desconto(preco: float, percentagem: float) -> float:
   
    return preco * (1 - (percentagem / 100))