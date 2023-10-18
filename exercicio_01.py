def realizar_venda(qtd_vendida, valor_pago, produto):
    if qtd_vendida > qtd_estoque:
        print("Quantidade insuficiente em estoque")
    else:
        valor_total = qtd_vendida * valor
        if valor_pago >= valor_total:
            troco = valor_pago - valor_total
            print(f"Venda realizada com sucesso!\nTroco: R${troco:.2f}")
        else:
            print("Valor pago é insuficiente")


estoque = []

num = int(input("Digite o número de produtos que quer cadastrar: "))

for i in range(num):
    nome = input("Digite o nome do produto: ")
    qtd_estoque = int(input("Digite a quantidade em estoque: "))
    valor = float(input("Digite o valor do produto: "))
    produto = {nome, qtd_estoque, valor}

    qtd_vendida = int(input("Digite a quantidade a ser vendida: "))

    if qtd_vendida > qtd_estoque:
        print("Não pode realizar a venda")
    else:
        valor_pago = float(input("Digite o valor pago: "))
        realizar_venda(qtd_vendida, valor_pago, produto)
