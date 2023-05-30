import tkinter as tk

# Criando a janela
janela = tk.Tk()
janela.title("James")

# Definindo o tamanho da janela
largura_tela = 8
altura_tela = 8
largura_pixels = 100
altura_pixels = 100

largura_total = largura_tela * largura_pixels
altura_total = altura_tela * altura_pixels

# Centralizando a janela na tela
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

posicao_x = int(largura_screen/2 - largura_total/2)
posicao_y = int(altura_screen/2 - altura_total/2)

janela.geometry(f"{largura_total}x{altura_total}+{posicao_x}+{posicao_y}")

# Carregando a imagem
imagem = tk.PhotoImage(file="caminho_para_a_imagem.gif")  # Substitua pelo caminho correto da imagem (formato GIF)

# Criando um widget Label para exibir a imagem
label_imagem = tk.Label(janela, image=imagem)
label_imagem.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Criando campos de entrada
campos = []
for i in range(largura_tela):
    linha_campos = []
    for j in range(altura_tela):
        entrada = tk.Entry(janela)
        entrada.grid(row=j, column=i, padx=5, pady=5)
        linha_campos.append(entrada)
    campos.append(linha_campos)

# Executando o loop principal da janela
janela.mainloop()
