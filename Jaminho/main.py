import tkinter
from tkinter import Tk, Button, Label, PhotoImage, TOP, BOTTOM, Entry
from tkinter.messagebox import showinfo


#função responsável por abrir as subjanelas do conteúdo selecionado na página bota //Não funciona ainda
def abrir_janela(item):
    nova_janela = tkinter.Toplevel(root)
    nova_janela.title(item)
    nova_janela.geometry("400x300")
    label = tkinter.Label(nova_janela, text=f"Conteúdo da janela '{item}'")
    label.pack(pady=50)


#função que pega o item selecionado na página bota e passa como argumento para função abrir_janela //Não funciona ainda
def item_selecionado(event):
    selecionado = listbox.curselection()
    if selecionado:
        item = listbox.get(selecionado)
        abrir_janela(item)


#fução que cria a subjanela com as opções de conteúdo
def clicar():
    bota = Tk() #definindo janela como bota
    bota.geometry("600x400") #tamanho da janela
    listbox = tkinter.Listbox(bota, width=50, font=("Times New Roman", 24)) #definindo uma caixa para lista
    listbox.pack(pady=10) #mostrando a caixa sem as lista
    #definindo os tópicos em uma lita
    itens = [
        "1º Introdução às curvas",
        "2º Cônicas, seções planas do cone",
        "3º Estudo da Parábola",
        "4º Estudo da Elipse",
        "5º Estudo da Hipérbole",
        "6º Classificação das Cônicas",
        "7º Coordenadas Polares e Cônicas"
    ]
    #colocando na caixa de lista cada item da lista Lista
    for item in itens:
        listbox.insert(tkinter.END, item)
    listbox.bind("<<ListboxSelect>>", item_selecionado) #deveria servir para selecionar a opção e redirecionar para outra página
    bota.mainloop()

#função para exibição de latex como imagem
def latex():
    import tkinter as tk
    from latex2image import Latex2Image

    lt = tk.Tk()

    # Função para converter uma expressão LaTeX em uma imagem
    def convert_latex_to_image(latex):
        l2i = Latex2Image(latex)
        image = l2i.as_image()
        return image

    # Função para exibir uma fórmula LaTeX em um widget Tkinter
    def exibir_formula_latex(formula):
        image = convert_latex_to_image(formula)
        photo = tk.PhotoImage(master=lt, image=image)
        label = tk.Label(lt, image=photo)
        label.image = photo
        label.pack()

    # Exemplo de uso
    formula_latex = r"f(x) = \frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x - \mu)^2}{2\sigma^2}}"
    exibir_formula_latex(formula_latex)

    lt.mainloop()

def graf():
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np

    # Função que representa o cone
    def cone_func(x, y):
        return np.sqrt(x ** 2 + y ** 2)

    # Definição do intervalo e resolução da grade
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)

    # Cálculo da função do cone para obter os valores de Z
    Z = cone_func(X, Y)

    # Criação da figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plotagem do cone
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    # Definição do plano de corte
    plane_height = 1.5
    plane_inclination = 0.5  # Fator de inclinação do plano em relação a y

    # Cálculo das coordenadas do plano
    plane_z = plane_height + plane_inclination * Y

    # Plotagem do plano
    ax.plot_surface(X, Y, plane_z, color='r', alpha=0.5)

    # Configurações dos eixos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Exibição do gráfico
    plt.show()


#Definindo a tela principal
root = Tk()
root.geometry("500x400") #tamanho da janela
root.title('ExplorandoConicas') #título da janela
photo = PhotoImage(file='gif.gif').subsample(5) #pegando o arquivo .gif para ilustração da tela principal
image = Label(master=root, image=photo) #passando a imagem(variável photo) como atributo image para um label
image.config(width=100, height=100) #tamanho da imagem
image.pack(pady=20) #mostrando a imagem na janela
text = Label(master=root, font=("Times New Roman", 16), text='GeometriaAnalítica by ILUM') #definisdo um label com a frase em destaque
text.pack(pady=20) #mostrando a frase em destaque
button = Button(root, text='Começar', command=clicar) #criando um botão que chama a função 'clicar' definida acima
button.pack(pady=20, side=BOTTOM) #mostrando o botão
button2 = Button(root, text='Teste', command=graf) #criando outro botão, esse chama a função graf
button2.pack(pady=20, side=BOTTOM) #mostrando botão
button3 = Button(root, text='Latex', command=latex) #criando outro botão, esse chama a função latex
button3.pack(pady=20, side=BOTTOM) #mostrando botão
root.mainloop() #padrão para manter a janela ativa
