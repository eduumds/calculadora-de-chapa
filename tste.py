import tkinter as tk

def calcular_peso_chapa():
    densidade_ferro = 7.85  # Densidade do ferro em g/cm³

    # Obter as medidas da chapa da interface gráfica
    largura = float(largura_entry.get().replace(',', '.'))
    comprimento = float(comprimento_entry.get().replace(',', '.'))
    espessura = float(espessura_entry.get().replace(',', '.'))

    # Converter as dimensões para metros
    largura_m = largura / 100
    comprimento_m = comprimento / 100
    espessura_m = espessura / 100

    # Calcular o volume da chapa em metros cúbicos
    volume = largura_m * comprimento_m * espessura_m

    # Calcular o peso em gramas
    peso = volume * densidade_ferro

    # Adicionar o peso calculado à lista de resultados
    resultados_listbox.insert(tk.END, f"Chapa {len(resultados) + 1}: {peso:.2f} kg")
    resultados.append(peso)

def somar_resultados():
    # Somar todos os pesos da lista de resultados
    total = sum(resultados)

    # Exibir o resultado total
    resultado_total_label["text"] = f"Total dos pesos: {total:.2f} kg"

# Criar a janela da interface gráfica
janela = tk.Tk()
janela.title("Cálculo de Peso de Chapas")
janela.geometry("300x300")
janela.configure(background="black")
janela.option_add("*Font", "Arial 12")
janela.option_add("*Background", "black")
janela.option_add("*Foreground", "green")

# Criar os labels e campos de entrada para as medidas
largura_label = tk.Label(janela, text="Largura (mm):")
largura_label.pack()
largura_entry = tk.Entry(janela)
largura_entry.pack()

comprimento_label = tk.Label(janela, text="Comprimento (mm):")
comprimento_label.pack()
comprimento_entry = tk.Entry(janela)
comprimento_entry.pack()

espessura_label = tk.Label(janela, text="Espessura (mm):")
espessura_label.pack()
espessura_entry = tk.Entry(janela)
espessura_entry.pack()

# Criar o botão de calcular
calcular_button = tk.Button(janela, text="Calcular", command=calcular_peso_chapa)
calcular_button.pack()

# Criar o label para exibir o resultado
resultado_label = tk.Label(janela)
resultado_label.pack()

# Criar o ListBox para exibir os resultados individuais
resultados_listbox = tk.Listbox(janela)
resultados_listbox.pack()

# Criar uma lista para armazenar os resultados dos cálculos
resultados = []

# Criar o botão para somar os resultados
somar_button = tk.Button(janela, text="Somar Resultados", command=somar_resultados)
somar_button.pack()

# Criar o label para exibir o resultado total
resultado_total_label = tk.Label(janela)
resultado_total_label.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
