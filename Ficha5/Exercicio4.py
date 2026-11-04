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

def despesas_superior_100():
    with open("despesas.csv", "r", encoding="utf-8") as ficheiro:
        contagem_despesas = 0
        resultado = ""

        conteudo = ficheiro.read()
        conteudo_lista = conteudo.splitlines()

        for linha in conteudo_lista[1:]:
            linha = linha.strip().split(";")
            despesas = float(linha[4])

            if despesas > 100:
                resultado += f"Id: {linha[0]}, Data: {linha[1]}, Categoria: {linha[2]}, Descrição: {linha[3]}, Despesas: {despesas:.2f}\n"
                contagem_despesas += 1

        resultado += f"\nQuantidade de despesas superiores a 100: {contagem_despesas}\n"

        return resultado
        
#Alinea 3
def calculos_estatisticos():
    with open("despesas.csv", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        conteudo_lista = conteudo.splitlines()
        despesas = []
        for linha in conteudo_lista[1:]:
            linha = linha.strip().split(";")
            valor_despesa = float(linha[4])
            despesas.append(valor_despesa)
        despesa_total = sum(despesas)
        despesa_media = despesa_total / len(conteudo_lista[1:])
        maior_despesa = max(despesas)
        menor_despesa = min(despesas)
        return(f"Valor total das despesas: {despesa_total:.2f}\nValor médio das despesas: {despesa_media:.2f} \nDespesa de valor mais elevado: {maior_despesa:.2f}\nDespesa de valor mais reduzido: {menor_despesa:.2f}")

#Alinea 4
def analise_categoria():
    with open("despesas.csv", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        conteudo_lista = conteudo.splitlines()
        totais_categoria = {}
        resultado = ""

        for linha in conteudo_lista[1:]:
            linha = linha.strip().split(";")

            categoria_nome = linha[2]
            valor_despesa = float(linha[4])

            if categoria_nome not in totais_categoria:
                totais_categoria[categoria_nome] = 0

            totais_categoria[categoria_nome] += valor_despesa

        for categoria, total in totais_categoria.items():
            resultado += f"{categoria}: {total:.2f} €\n"

        return resultado
#Alinea 5
#calculo auxiliar
def calculos_totaldespesas():
    with open("despesas.csv", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
        conteudo_lista = conteudo.splitlines()
        contagem_despesas=0
        for linha in conteudo_lista[1:]:
            linha = linha.strip().split(";")
            contagem_despesas=contagem_despesas + 1
        return(f"Contagem de despesas:{contagem_despesas}")
                       
def escrever_ficheiro_relatorio():
    try:
        with open("relatorio_despesas.txt", "x", encoding="utf-8") as ficheiro:
            pass
    except FileExistsError:
        print("O ficheiro já existe!")
        
def adicionarinfo_ficheiro_relatorio():
    with open("relatorio_despesas.txt", "w", encoding="utf-8") as ficheiro:
        ficheiro.write(str(calculos_totaldespesas()) + "\n")
        ficheiro.write("\n")
        ficheiro.write(str(calculos_estatisticos()) + "\n")
        ficheiro.write("\n")
        ficheiro.write("Despesas superiores a 100:"+ "\n")
        ficheiro.write(str(despesas_superior_100()) + "\n")
        ficheiro.write("Total de despesas por categoria:"+ "\n")
        ficheiro.write(str(analise_categoria()) + "\n")