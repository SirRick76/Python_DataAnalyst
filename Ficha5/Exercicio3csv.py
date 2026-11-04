#Exercicio 3 
import csv
#a)

def ler_ficheiro_csv1():
    try:
        with open("dados_pessoais.csv", "r", encoding="utf-8",newline='') as ficheiro:
            conteudo = csv.reader(ficheiro,delimiter=",")
            for linha in conteudo:
                print(linha) 
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")
#b)

def ler_nome_ficheiro_csv1():
    with open("dados_pessoais.csv", "r", encoding="utf-8",newline='') as ficheiro:
            conteudo = csv.reader(ficheiro,delimiter=",")
            for linha in conteudo:
                print(linha[0]) 
#c)
def media_idade_csv1():
    with open("dados_pessoais.csv", "r", encoding="utf-8",newline='') as ficheiro:
        idades=[]
        conteudo = csv.reader(ficheiro,delimiter=",")
        next(conteudo)
        for linha in conteudo:
            idade=int(linha[2])
            idades.append(idade)
    media = sum(idades) / len(idades)
    print(f"Média de idade: {media:.2f}")
#d)
def adicionar_registo_csv1():
    with open("dados_pessoais.csv","a",encoding="utf-8") as ficheiro:
        nome = input("Digite o nome: ")
        morada = input("Digite a morada: ")
        idade = int(input("Digite a idade: "))
        escrita = csv.writer(ficheiro)
        escrita.writerow([nome, morada, idade])
    print("Registo adicionado com sucesso!")