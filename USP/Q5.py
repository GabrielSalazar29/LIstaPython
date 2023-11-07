for _ in range(15):
    nome = input("Digite o nome do cliente: ")
    compras = float(input("Digite o valor das compras no ano passado: "))
    if compras < 1000:
        bonus = 0.10 * compras
    else:
        bonus = 0.15 * compras
    print(f"{nome} tem direito a um bônus de R${bonus:.2f}")