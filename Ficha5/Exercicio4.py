#Exercicio 4
#Parte A
#1)
import csv

#2)
def ler_ficheiro_despesascsv():
    try:
        with open("despesas.csv", "r", encoding="utf-8") as ficheiro:
            conteudo = ficheiro.read()
        print(conteudo)
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")

#3 e 4)
def ler_ficheiro_despesascsvreader():
    try:
        with open("despesas.csv", "r", encoding="utf-8") as ficheiro:
            conteudo = csv.reader(ficheiro)
            for linha in conteudo:
                print(linha)
    except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")
    print("a continuar o programa...")
#Alinea 2

#Alinea 3

#Alinea 4

#Alinea 5

