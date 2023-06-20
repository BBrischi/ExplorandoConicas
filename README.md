# **Projeto ExplorandoConicas**

**Integrantes**: Samuel Soares de Araújo, Laís Fernanda Medeiros Ruela, Bruno Ferreira Brischi e Beatriz Borges Ribeiro

## Resumo Teórico
O modelo de ensino da ILUM-Escola de Ciência é voltado para o preparo dos alunos como cientistas interdisciplinares que possam ver os problemas atuais de forma mais completa,tornando possível o florescer de novas formas de encarar esses problemas, porém por ter uma proposta tão ousada, o sistema da ILUM escolheu assuntos que são mais relevantes para o dia a dia do pesquisador moderno, onde grande parte do que é ensinado nas graduações não é utilizado. Assim sendo, um dos assuntos que foram dissolvidos nas matérias do curso foi a Geometria Analítica, que acaba sendo ensinada de forma gradual como ferramenta para as matérias ao longo dos 3 anos de curso. Tendo isso em vista, foi proposto como projeto de desenvolvimento, na matéria Introdução a Ciências de Dados, um sistema que proporciona o aprofundamento em um dos assuntos mais interessantes da geometria analítica: o estudo de cônicas. aos alunos da ILUM e qualquer pessoa com interesse no assunto. Para mais detalhes do projeto, acesse o PDF que está dentro do repositório como "ExplorandoConicas".

## Como acessar o material mais completo e interativo sobre cônicas do século XXI

Para ter acesso ao sistema, o usuário deve acessar a pasta Projeto Final e abrir o arquivo Samuca.ipynb em um software que rode o formato ipynb, pode ser usado o vscode, jupyterlab ou googlecolab, nos dois últimos casos, é necessário transferir toda a pasta Projeto Final nos respectivos servidores para que não haja problema na visualização das imagens, por fim, deve-se abrir o arquico Samuca.ipynb. 

## Funcionamento

Com o notebook em mãos, basta seguir a ordem já estabelicida no próprio notebook, a qual já está organizada como uma trilha de aprendizado do conteúdo de cônicas, toda a explicação está em fácil notação em LaTeX, podendo, caso o usuário tenha domínio, acrescentar observações próprias ou sinalizações que forem convinientes. Para a manipulação dos gráficos, é necessário cuidado, todos os códigos referentes aos gráficos 3D salvam os gráficos gerados em um arquivo separado do tipo HTML, por isso, o usuário deve abrir o arquivo HTML gerado pelo código para visualizar o gráfico em questão, caso o usuário julgue necessário, é possível alterar o nome dos arquivos HTML gerados. Além disso, ao abrir os arquivos HTML aparecerá no canto superior direito um botão escrito TrustHTML, que deve ser clicado para que o arquivo seja aberto.
Já para o quiz, ao rodar o código, é necessário ter cuidado para finalizar o quiz antes de rodar qualquer outro código, caso não quira terminar, deve reiniciar o Kernel. O quiz é simples com perguntas referentes aos tópicos abordados no próprio notebook, e é gerado um pequeno relatório com a quantidade de acertos por tópico para que o usuário saiba quais assuntos precisam de maior revisão. 

## Resumo do Código

O projeto do software é fornecer um guia de estudos dinâmicos no ambiente do `Jupyter Lab` para cônicas, contemplando a teoria, exercícios e o plot dos gráficos, tanto 3D quanto 2D. A teoria será escrita usando códigos LaTeX com a biblioteca `IPython`, tornando possível exibir cada equação com uma aparência agradável. Para os plots, usaremos `matplotlib` e o `plotly` aliada ao `numpy`. A primeira biblioteca já é uma conhecida entre os usuários de código e permite realizar inúmeros tipos de plots, tantos 2D quanto 3D, dependendo do método usado. Já a segunda biblioteca será importante para consolidar a matemática por trás do código, para definir parâmetros das equações e outros elementos. Além disso, para que o usuário possa testar seus conhecimentos, há um quiz com diverssas perguntas, no qual é possível ver a quantidade de acerto por tópico, permitindo que o usuário saiba quais assuntos precisa revisar,o quiz usa a biblioteca `random` para gerar a ordem das perguntas para tornar menos cansativo. 

## Pré-requisitos
Para nosso código, além de utilizar um programa que rode códigos em Python, é preciso ter as seguintes bibliotecas:
<li>Matplotlib</li>
<li>IPython</li>
<li>Numpy</li>
<li>Plotly</li>
<li>tkinter</li>
<li>random</li>

## Usando a biblioteca `IPython`

O funcionamento da biblioteca `IPython` é bem simples, já que o texto e a fórmula em LaTeX são inseridos em string. Para utilizá-lo, fazemos o import da classe `IPythondisplay`, como `from IPython.display import display, Markdown`. Assim, o notebook de rascunho já possui uma função que retorna o texto em markdown e, quando conveninente, basta adicionar os códigos em LaTeX usando `$(insira o texto aqui)$`. A função que definimos é:

```python
def txt_ltx(texto):
"""Recebe uma string como argumento e delvove um texto como Markdown"""
    
    display(Markdown(texto))
```

Além disso, como estamos trabalhando com uma string que será convertida em markdown, podemos alterar fonte, tamanho da fonte, entre outros. Um exemplo seria:

```python
txt_ltx('''Se chamarmos a geratriz de reta $a$ e o eixo de rotação de reta $b$, 
fixando a reta $a$ e girando a reta $b$ em $360^\circ$ em torno de $a$ e não alterando o ângulo entre elas, 
obtemos uma superfície cônica circular infinita formada por dois cones separados pelo vértice $V$.''')
```

## Usando a biblioteca `matplotlib`, `Plotly` e `numpy`

O papel principal dessas bibilotecas é usá-las combinadas a fim de conseguir plotar os gráficos que são tão necessários dentro do estudo de GA. Sendo o `numpy` a sustentação dos processos, servindo para as funções referentes aos gráficos, já o `matplotlib` e o `plotly` são os responsáveis pela representação dos gráficos em si, o `matplotlib` está sendo usado para representar os fráficos 2D enquanto o `plotly` para o gráficos 3D.

Usamos os seguintes imports:

```python
import plotly.graph_objects as go
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
```

Para começar a plotar os gráficos 2D, usamos as seguintes funções:

**-**`mpl.rcParams['lines.color']`: irá definir a cor padrão das linhas do gráfico (geralmente usa-se `k`)

**-**`mpl.rcParams['axes.prop_cycle']`: define o ciclo de cores padrão para os eixos dos gráficos como uma lista contendo apenas a cor preta. Isso significa que, por padrão, as diferentes linhas dos gráficos terão a mesma cor preta.

**-**`x = np.linspace(-9, 9, 400)`: cria um array unidimensional chamado 'y' com 400 valores igualmente espaçados no intervalo de -5 a 5. Esses valores serão usados como coordenadas y para os pontos do gráfico.

**-**`y = np.linspace(-5, 5, 400)`: cria um array unidimensional chamado 'y' com 400 valores igualmente espaçados no intervalo de -5 a 5. Esses valores serão usados como coordenadas y para os pontos do gráfico.

**-**`x, y = np.meshgrid(x, y)`: cria uma grade bidimensional a partir dos arrays 'x' e 'y', sendo essa função advinda do `numpy`. Essa grade será usada para desenhar o contorno do gráfico.

**-**`def axes():`: define uma função chamada 'axes' que será usada para desenhar as linhas dos eixos x e y.

**-**`plt.axvline(0, alpha=.1)`: desenha uma linha vertical no valor x=0, representando o eixo y. O argumento alpha=.1 define a transparência da linha como 0.1.

**-**`axes()`: chama a função 'axes' para desenhar as linhas dos eixos x e y.

**-**`plt.contour(x, y, (), [], colors=)`: desenha um contorno do gráfico representado por uma função com uma linha sólida na posição $y=0$. A cor da linha pode ser escolhida em `colors=`. Esse terceiro argumento é onde você insere sua função e o quarto argumento `[]` recebe o raio da sua cônica.

**-**`plt.show()`: exibe o gráfico resultante na tela.

Vejamos um exemplo de uma ampulheta com intersecção:

```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

x = np.linspace(-9, 9, 400)
y = np.linspace(-5, 5, 400)
x, y = np.meshgrid(x, y)

def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
        
a = .3 # Variável definida para comportar a variável descrita na expressão.


axes()
plt.contour(x, y, (y**2 - 4*a*x), [0], colors='blue')
plt.show()
```
Para começar a plotar os gráficos 3D, usamos as seguintes funções:

**-**` go.Cone()`: configura uma função que representa um cone, sendo possível alterar os atributos para ajustar a necessidade. Sendo possível definir a posição em relação ao eixo x, y e x junto com a inclinação em relação aos eixos x(u), y(v) e z(w), além de ajustes de referência do tamanho do cone, cor e opacidade.

**-**`go.Surface()`: configura uma função que representa um plano, sendo possível ajustar os eixos, cor e opacidade.

**-**`go.Figure()`: configura os componentes do gráfico, sendo passado as funções que irão compor a figura final.

**-**`x = np.linspace(-9, 9, 400)`: cria um array unidimensional chamado 'y' com 400 valores igualmente espaçados no intervalo de -5 a 5. Esses valores serão usados como coordenadas y para os pontos do gráfico.

**-**`y = np.linspace(-5, 5, 400)`: cria um array unidimensional chamado 'y' com 400 valores igualmente espaçados no intervalo de -5 a 5. Esses valores serão usados como coordenadas y para os pontos do gráfico.

**-**`x, y = np.meshgrid(x, y)`: cria uma grade bidimensional a partir dos arrays 'x' e 'y', sendo essa função advinda do `numpy`. Essa grade será usada para desenhar o contorno do gráfico.

**-**`.update_layout()`: configura a figura do gráfico, sendo possível definir título e tamanho. 

**-**`plt.show()`: exibe o gráfico resultante na tela.

**-**`.write_html()`: escreve a figura, que foi configurada com `go.Figure` e `.update_layout`, no formato html e salva em um arquivo.

Vejamos um exemplo com a função $y^2 = 4ax$, sendo $a>0$:

```python
import plotly.graph_objects as go
import numpy as np

# Parâmetros dos cones
raio_base = 1  # Raio da base do cone
altura = 3  # Altura do cone


# Criação do cone inferior
cone_inferior = go.Cone(
    x=[0], y=[0], z=[altura / 2],
    u=[0], v=[0], w=[altura],
    sizemode="absolute",
    sizeref=2 * raio_base,
    showscale=False,
    colorscale='Blues',
    opacity=0.5
)

# Criação do cone superior
cone_superior = go.Cone(
    x=[0], y=[0], z=[4.5],
    u=[0], v=[0], w=[-(altura)],
    sizemode="absolute",
    sizeref=2 * raio_base,
    showscale=False,
    colorscale='Blues',
    opacity=0.5
)

def plane_equation(x, y):
    return 1.5*altura + y-y

# Criação dos pontos para o grid
n_points = 50
x = np.linspace(-raio_base, raio_base, n_points)
y = np.linspace(-raio_base, raio_base, n_points)
X, Y = np.meshgrid(x, y)

# Cálculo das coordenadas do plano de corte
Z = plane_equation(X, Y)

plane = go.Surface(
    x=X, y=Y, z=Z,
    colorscale='Reds',
    opacity=0.5
)

fig = go.Figure(data=[cone_inferior, cone_superior, plane])

# Configuração do layout
fig.update_layout(
    title='Cone em Cima do Outro com Plano de Corte',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectratio=dict(x=1, y=1, z=0.8),
        camera=dict(eye=dict(x=1.2, y=1.2, z=1))
    ),
    autosize=False,
    width=800,
    height=800,
)

fig.write_html("grafico.html")
```
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Futuro que nunca vai acontecer
### Código com o tkinter sem finalização por impossibilidades técnicas:

Todo o sistema será dividido em telas, as quais funcionarão como forma de organizar os conteúdos e permitir ao usuário chegar até o assunto desejado com facilidade. Abaixo vamos ver um pouco de cada código do sistema implementado até o momento:

Tela inicial junto com as subtelas e os códigos dos gráficos. Vamos destrinchar cada parte do código para entender seu funcionamento. 

<li>Primeiro temos a tela principal feita com a biblioteca tkinter:</li>

Nessa parte do código é definida a tela principal(`root`) com uma imagem ilustrativa de geometria analítica, uma frase padrão em destaque para deixar bonito e os botões de redirecionamento. Vale lembrar que é apenas um código de testes, não mostrando a organização real das janelas.

A imagem é pega pela função `PhotoImage` e passada para uma variável chamada `photo`, o `file` é o caminho da imagem que você quer mostrar, caso queira mudar a imagem é só colocar o caminho para outra, porém o `tkinter` só aceita _.gif_, assim, é impossível colocar _.jpeg_ ou _.png_. Ela é transformada para o formato de `label` e passada para uma variável chamada `image`, a qual tem o tamanho ajustado por `.confg`, sendo possível alterar o tamanho à vontade, limitado só pelo tamanho da janela, depois `.pack` exibe o label da imagem.

A frase padrão em destaque para deixar bonito é configurada como `label`, passando o tipo de de letra e o tamanho, além da String do texto, depois, exibe com o `.pack`. Já os botões são criados com o `Button`, onde é passado o texto do botão e a função a ser chamada ao clicar através do `command`. Tem o total de três botões. o `button` que chama a função clicar, a qual abre uma janela com a lista de opções de conteúdo; o `button2` que chama a função `graph`, a qual abre uma janela com um gráfico interativo feito com `matplotlib`

<li>Função clicar</li>

A janela foi definida como bota e seu tamanho como o mesmo da página central(`bota`). 

Depois, é definido uma caixa de lista com o seu tamanho junto ao tipo e tamanho de letra que vão ser exibidos, essa caixa é onde será adicionando as opções de conteúdo. Além disso, é criado uma lista com as opções de conteúdo, essa lista é iterada com um `for`, adicionando cada item da lista(conteúdo) à caixa de lista com o comando `.insert`. 

Para selecionar os itens da lista é utilizado a função `.bind` com `<<ListboxSelect>>` que chama a função `item_selecionado` que não está funcionando ainda, mas essa função chama a função `abrir_janela` que, também, não está funcionando ainda.

<li>Função graph</li>

Essa função é responsável por plotar o gráfico 3d interativo.

_O exemplo desse código pode ser encontrado dentro do diretório Jaminho, no arquivo main.py_


