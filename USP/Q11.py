compras_vista = 0
compras_prazo = 0

for _ in range(15):
    codigo = input("Digite o código (V para à vista, P para a prazo): ")
    valor = float(input("Digite o valor da transação: "))
    
    if codigo == 'V':
        compras_vista += valor
    elif codigo == 'P':
        compras_prazo += valor

total_compras = compras_vista + compras_prazo
primeira_prestacao = compras_prazo / 3

print(f"Valor total das compras à vista: R${compras_vista:.2f}")
print(f"Valor total das compras a prazo: R${compras_prazo:.2f}")
print(f"Valor total das compras efetuadas: R${total_compras:.2f}")
print(f"Valor da primeira prestação das compras a prazo: R${primeira_prestacao:.2f}")
