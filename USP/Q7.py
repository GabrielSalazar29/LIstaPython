contagem = 0
for _ in range(10):
    idade = int(input("Digite a idade: "))
    if idade >= 18:
        contagem += 1

print(f"{contagem} pessoas têm 18 anos ou mais.")