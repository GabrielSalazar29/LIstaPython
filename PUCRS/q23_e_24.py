maior_idade = 0
contador_mulheres = 0

while True:
    idade = int(input("Digite a idade do habitante (ou -1 para encerrar): ")
    
    if idade == -1:
        break

    sexo = input("Digite o sexo (M para masculino, F para feminino): ")
    cor_olhos = input("Digite a cor dos olhos (azuis, verdes, castanhos): ")
    cor_cabelos = input("Digite a cor dos cabelos (louros, castanhos, pretos): ")

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "F" and 18 <= idade <= 35 and cor_olhos == "verdes" and cor_cabelos == "louros":
        contador_mulheres += 1

print("A maior idade dos habitantes é:", maior_idade)
print("A quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos louros é:", contador_mulheres)
