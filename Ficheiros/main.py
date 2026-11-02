with open("equipas.txt", "a") as file:
    equipas2 = file.write("Braga MunicipalBraga 30000 31000 120000000 400000 Franclim")
print(equipas2)    
with open("equipas.txt", "r") as file:
    equipas1 = file.read()
print(equipas1)

