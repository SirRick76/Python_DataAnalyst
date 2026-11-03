from random import randint
#Exercicio 2
#Parte A
#a)
def numero_aleatorio(a, b):
    return randint(a, b)
#b)
quantidade_numeros = numero_aleatorio(5, 20)
#c)
def gravar_numeros_aleatorios():
    with open("numeros_aleatorios.txt", "w", encoding="utf-8") as ficheiro:
        for _ in range(quantidade_numeros):
            numero = numero_aleatorio(1, 100)
            ficheiro.write(str(numero) + "\n")
        print("Ficheiro gravado com sucesso!")
#Parte B
#a)
def contar_linhas():
    with open("numeros_aleatorios.txt", "r", encoding="utf-8") as ficheiro:
        linhas = ficheiro.readlines()
        quantidade_linhas = len(linhas)
    print("Quantidade de linhas no ficheiro:", quantidade_linhas)
#b)
def contar_media():
     with open("numeros_aleatorios.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        conteudo_lista = conteudo.splitlines()
        for i in range(len(conteudo_lista)):
            conteudo_lista[i] = int(conteudo_lista[i])
        media = sum(conteudo_lista) / len(conteudo_lista)
        print(f"Média dos números no ficheiro: {media:.2f}")
#c)
def contar_maior_menor():
    with open("numeros_aleatorios.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        conteudo_lista = conteudo.splitlines()
        for i in range(len(conteudo_lista)):
            conteudo_lista[i] = int(conteudo_lista[i])
        maior_numero = max(conteudo_lista)
        menor_numero = min(conteudo_lista)
    print("Maior número no ficheiro:", maior_numero)
    print("Menor número no ficheiro:", menor_numero)