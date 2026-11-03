#Exercicio 3 
import csv
#a)

def ler_ficheiro_csv():
    try:
        with open("dados_pessoais.csv", "r", encoding="utf-8") as ficheiro:
            conteudo = ficheiro.read()
        print(conteudo)
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")
#b)

def ler_nome_ficheiro_csv():
    registos = []
    with open("dados_pessoais.csv","r",encoding="utf-8") as ficheiro:
        lista = ficheiro.readlines()
    for linha in lista:
        dados = linha.strip().split(",")
        registos.append(dados)
    for registo in registos[1:]:
        nome = registo[0]
        print(nome)
#c)
def media_idade_csv():
    registos = []
    with open("dados_pessoais.csv","r",encoding="utf-8") as ficheiro:
        lista = ficheiro.readlines()
    for linha in lista:
        dados = linha.strip().split(",")
        registos.append(dados)
    idade = []
    for registo in registos[1:]:
        idade.append(int(registo[2]))
    media = sum(idade) / len(idade)
    print(f"Média de idade: {media:.2f}")
#d)
def adicionar_registo_csv():
    with open("dados_pessoais.csv","a",encoding="utf-8") as ficheiro:
        nome = input("Digite o nome: ")
        morada = input("Digite a morada: ")
        idade = int(input("Digite a idade: "))
        novo_registo = f"{nome},{morada},{idade}\n"
        ficheiro.write(novo_registo)
    print("Registo adicionado com sucesso!")