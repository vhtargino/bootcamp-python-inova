# cadastrar = input("Deseja cadastrar (S/N): ").upper()
# i = 0

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

pessoas = []

cadastrar = int(input("Quantas vezes quer cadastrar? Digite ao lado: "))

# while cadastrar > i:
for i in range(cadastrar):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    peso = float(input(f"Digite o peso da pessoa {i + 1} em kg: "))
    altura = float(input(f"Digite a altura da pessoa {i + 1} em metros: "))

    cadastro = (nome, idade, peso, altura)
    pessoas.append(cadastro)

    imc = calcular_imc(peso, altura)
    print(imc)

    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    elif 30 <= imc < 35:
        print("Obesidade grau I")
    elif 35 <= imc < 40:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")
    
    print(f"A pessoa {nome} com idade {idade}, peso {peso} kg, altura {altura}m, tem o IMC {imc:.2f}.")

    # cadastrar = input("Deseja cadastrar (S/N): ").upper()
    # i += 1
