from openpyxl import load_workbook

#abrir ficheiro
arquivo=load_workbook("USAvsUK.xlsx")

#guardar a folha ativa numa variavel
folha = arquivo.active

#guardar o nome da folha ativa
nome_folha = folha.title

#1ª coisa a fazer e saber o valor da ultima linha do ficheiro

def ultima_linha(folha):
    ultima = 0
    #percorrer todas as linhas da folha
    for numero_linha, linha in enumerate(
        folha.iter_rows(values_only=True),start=1
    ):
        for valor in linha:
            if valor is not None:
                ultima=numero_linha
                break
    return ultima
contagem =ultima_linha(folha)
print("Ultima linha de dados:",contagem)

#2ª criar as folhas dos paises
#percorrer a coluna C do excel e apartir da segunda linha
def criar_folha(pais,arquivo):
    if pais not in arquivo.sheetnames:
        arquivo.create_sheet(pais)

for linha in folha.iter_rows(min_row=2,max_row=contagem,min_col=3,max_col=3, values_only=True):
    pais = linha[0]
    #ignorar as celulas vazias
    if not pais:
        continue
    criar_folha(pais,arquivo)
arquivo.save("USAvsUK2.xlsx")
print("Nova folha criada")
print("Folha ativa",folha.title)

#Preencher cabeçalhos

def preencher_cabecalhos(arquivo,folha):
    cabecalhos=next(folha.iter_rows(min_row=1,max_row=1,values_only=True))
    lista_folhas=arquivo.sheetnames
    for nome_folha in lista_folhas[1:]:
        folha_destino = arquivo[nome_folha]
        colunas_origem =[0,1,3,4]
        #copiar os cabecalhos
        for coluna_destino,indice_origem in enumerate(
            colunas_origem,start=1
        ):
            folha_destino.cell(row=1,column=coluna_destino).value = cabecalhos[indice_origem]
        
preencher_cabecalhos(arquivo,folha)
arquivo.save("USAvsUK2.xlsx")
