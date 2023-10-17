produto = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
valor = float(input("Digite o valor: "))

comprar = int(input(f"Quanto deseja comprar de {produto}? Digite ao lado: "))

if comprar > quantidade:
    print(f"Não é possível comprar mais do que {quantidade}")

custo_total = valor * comprar

pagamento = float(input("Quanto vai pagar? Digite ao lado: "))

if pagamento < custo_total:
    print(f"R${custo_total} não é suficiente.")
elif pagamento == custo_total:
    print("Compra realizada com sucesso.")
else:
    troco = pagamento - custo_total
    print(f"Compra realizada com sucesso. Seu troco é R${troco}")
