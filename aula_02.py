# Tkinter biblioteca gráfica
import tkinter as tk

# themed Tkinter (ttk) é um conjunto de widgets (elementos de interface)
from tkinter import ttk

# Declaração de fontes para uso posterior
fonte1 = ("Arial", 10)
fonte2 = ("Arial", 16, "bold")

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc


def classificar_imc(imc):
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 25:
        classificacao = "Peso normal"
    elif 25 <= imc < 30:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 35:
        classificacao = "Obesidade grau I"
    elif 35 <= imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
    
    return classificacao


def cadastrar_pessoa():
    nome = nome_entry.get()
    idade = int(idade_entry.get())
    peso = float(peso_entry.get())
    altura = float(altura_entry.get())

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    resultado_label["text"] = f"Nome: {nome}\nIdade: {idade}\nPeso (kg): {peso} kg\nAltura (m): {altura:.2f}m\nIMC: {imc:.2f}"
    classificacao_label["text"] = f"A classificação é: {classificacao}"


# Cria a janela principal
root = tk.Tk()
root.title("Inova Uniesp")
root.geometry("330x550") # Define o tamanho da janela

# Cria os widgets
titulo_label = ttk.Label(root, text="Calcular IMC", font=fonte2)

nome_label = ttk.Label(root, text="Nome:", font=fonte1)
nome_entry = ttk.Entry(root, font=fonte1, width=30)

idade_label = ttk.Label(root, text="Idade:", font=fonte1)
idade_entry = ttk.Entry(root, font=fonte1, width=30)

peso_label = ttk.Label(root, text="Peso (kg):", font=fonte1)
peso_entry = ttk.Entry(root, font=fonte1, width=30)

altura_label = ttk.Label(root, text="Altura (m):", font=fonte1)
altura_entry = ttk.Entry(root, font=fonte1, width=30)

resultado_label = ttk.Label(root, text="", font=fonte1)
classificacao_label = ttk.Label(root, text="", font=fonte1)

botao = ttk.Button(root, text="Calcular IMC", command=cadastrar_pessoa)

# Ajusta a posição geometricamente na tela
titulo_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

nome_label.grid(row=1, column=0, padx=10, pady=20)
nome_entry.grid(row=1, column=1, padx=10, pady=20)

idade_label.grid(row=2, column=0, padx=10, pady=20)
idade_entry.grid(row=2, column=1, padx=10, pady=20)

peso_label.grid(row=3, column=0, padx=10, pady=20)
peso_entry.grid(row=3, column=1, padx=10, pady=20)

altura_label.grid(row=4, column=0, padx=10, pady=20)
altura_entry.grid(row=4, column=1, padx=10, pady=20)

botao.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

resultado_label.grid(row=6, column=0, columnspan=2, pady=5)
classificacao_label.grid(row=7, column=0, columnspan=2, pady=5)

# Inicia a interface gráfica
root.mainloop()
