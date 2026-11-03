import datetime as dt
#Exercicio 1
#a)
def escrever_ficheiro():
    with open("relatorio.txt", "w", encoding="utf-8") as ficheiro:
        ficheiro.write("O projeto Alpha foi iniciado em janeiro. \n")
        ficheiro.write("O projeto Beta será concluído em março.  \n")
        ficheiro.write("O projeto Gamma está em fase de testes. \n")

#b)
def ler_ficheiro():
    with open("relatorio.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()
    conteudo_lista = conteudo.splitlines()
    print(conteudo_lista)
    print(conteudo_lista[0])
    print(conteudo_lista[1])
    print(conteudo_lista[2])

#c)
def contar_palavras():
    with open("relatorio.txt", "r", encoding= "utf-8") as ficheiro:
        conteudo = ficheiro.read()
        contagem = conteudo.count("projeto")
    print(f"A palavra 'projeto' aparece {contagem} vezes no ficheiro.")

#d)
def adicionar_linha():
    with open("relatorio.txt", "a", encoding="utf-8") as ficheiro:
        ficheiro.write("O projeto Delta será iniciado em abril. \n")

#e)
def adicionar_tempo():
    data_atual = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("relatorio.txt", "r", encoding="utf-8") as ficheiro:
        conteudo = ficheiro.read()

    with open("relatorio.txt", "w", encoding="utf-8") as ficheiro:
        ficheiro.write(f"Última atualização: {data_atual}\n")
        ficheiro.write(conteudo)


''' Utilizando a função tell() para obter a posição atual do cursor no ficheiro, e a função seek() para mover o cursor para uma posição específica, podemos adicionar a data e hora
with open("relatorio.txt", "r+", encoding="utf-8") as ficheiro:
  posicao_inicial = ficheiro.tell()  # Retorna 0 (início do ficheiro)

  conteudo_antigo = ficheiro.read()  # O cursor vai para o fim do ficheiro

  ficheiro.seek(posicao_inicial)  # Move o cursor de volta para o início (0)

  # Escreve o topo e depois o resto (ainda precisa do conteúdo antigo na memória)
  ficheiro.write(f"Última atualização: {data_atual}\n")
  ficheiro.write(conteudo_antigo)
'''