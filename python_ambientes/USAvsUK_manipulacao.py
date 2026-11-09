from openpyxl import load_workbook

arquivo=load_workbook("USAvsUK.xlsx")

print(arquivo.sheetnames)

#ver folha ativa
folha_ativa = arquivo.active
print(folha_ativa)
#selecionar celula
print(folha_ativa["A1"].value)

folha_ativa["A1"].value ="Python"
arquivo.save("USAvsUK1.xlsx")

folha_ativa=arquivo["Folha1"]

print(folha_ativa.max_row)
print(len(folha_ativa["A"]))

valor1=folha_ativa.cell(row=45,column=3)
print(valor1)
print(valor1.value)