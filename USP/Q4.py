grupos = []
for _ in range(5):
    grupo = [int(input("Digite A: ")), 
             int(input("Digite B: ")), 
             int(input("Digite C: ")), 
             int(input("Digite D: "))]
    grupos.append(grupo)

print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

print("Grupos em ordem crescente:")
grupos.sort()
for grupo in grupos:
    print(grupo)

print("Grupos em ordem decrescente:")
grupos.sort(reverse=True)
for grupo in grupos:
    print(grupo)
