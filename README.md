# **Projeto ExplorandoConicas**

**Integrantes**: Samuel Soares de Araújo, Laís Fernanda Medeiros Ruela, Bruno Ferreira Brischi e Beatriz Borges Ribeiro

## Resumo Teórico
O modelo de ensino da ILUM-Escola de Ciência é voltado para o preparo dos alunos como cientistas interdisciplinares que possam ver os problemas atuais de forma mais completa,tornando possível o florescer de novas formas de encarar esses problemas, porém por ter uma proposta tão ousada, o sistema da ILUM escolheu assuntos que são mais relevantes para o dia a dia do pesquisador moderno, onde grande parte do que é ensinado nas graduações não é utilizado. Assim sendo, um dos assuntos que foram dissolvidos nas matérias do curso foi a Geometria Analítica, que acaba sendo ensinada de forma gradual como ferramenta para as matérias ao longo dos 3 anos de curso. Tendo isso em vista, foi proposto como projeto de desenvolvimento, na matéria Introdução a Ciências de Dados, um sistema que proporciona o aprofundamento em um dos assuntos mais interessantes da geometria analítica: o estudo de cônicas. aos alunos da ILUM e qualquer pessoa com interesse no assunto. Para mais detalhes do projeto, acesse o PDF que está dentro do repositório como "ExplorandoConicas" 

## Resumo do Código

Usando a biblioteca `tkinter`, iremos programar as telas interativas e interface gráfica para exibir a teoria, exercícios e o plot dos gráficos, tanto 3D quanto 2D. A teoria será escrita usando códigos LaTeX com a biblioteca `IPython`, tornando possível exibir cada equação com uma aparência agradável. Para os plots, usaremos `matplotlib` aliada a `numpy`. A primeira biblioteca já é uma conhecida entre os usuários de código e permite realizar inúmeros tipos de plots, tantos 2D quanto 3D, dependendo do método usado. Já a segunda biblioteca será importante para consolidar a matemática por trás do código, para definir parâmetros das equações e outros elementos.

## Pré-requisitos
Para nosso código, além de utilizar um programa que rode códigos em Python, é preciso ter as seguintes bibliotecas:
<li>Matplotlib</li>
<li>IPython</li>
<li>Numpy</li>
<li>tkinter</li>

## Usando a biblioteca `IPython`

O funcionamento da biblioteca `IPython` é bem simples, já que o texto e a fórmula em LaTeX são inseridos em string. Para utilizá-lo, fazemos o import da classe `IPythondisplay`, como `from IPython.display import display, Math`. Assim, armazenamos em uma variável a fórmula do LaTeX em string em raw string e usamos o comando `display(Math())`, em que o argumento da função `Math` é a variável com LaTeX. Vejamos um exemplo:

```python
exemplo2 = r'''
    \begin{gather}
    \frac{\partial f}{\partial \vec{w}} \left(2, \frac{1}{2} \right) = 
    \langle \nabla f(4,3), \vec{w}  \rangle = (4,3) \cdot \left(\frac{4}{5}, \frac{3}{5} \right) = 
    \frac{16}{5} + \frac{9}{5} = \frac{25}{5} = 5
    \end{gather}
    '''
    
display(Math(exemplo2))
```

Rodando esse código, obtemos:

$$\frac{\partial f}{\partial \vec{w}} \left(2, \frac{1}{2} \right) = \langle \nabla f(4,3), \vec{w}  \rangle = (4,3) \cdot \left(\frac{4}{5}, \frac{3}{5} \right) = \frac{16}{5} + \frac{9}{5} = \frac{25}{5} = 5$$

<i>Observação: Esse código usando essa biblioteca é focada para ambientes interativos como Jupyter Notebook e IPython. No momento, estamos encontrando problemas para rodar esse código na interface da biblioteca do tkinker. Explicamos já o funcionamento dessa biblioteca pela sua simplicidade e porque será uma das opções que iremos aderir caso a ideia de fazer uma interface interativa funcione.</i>

## Usando a biblioteca `tkinker`

Todo o sistema é dividido em telas, as quais funcionam como forma de organizar os conteúdos e permitir ao usuário chegar até o assunto desejado com facilidade. Abaixo vamos ver um pouco de cada código do sistema implementado até o momento:

### Código Principal:

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

## Usando a biblioteca `matplotlib` e `numpy`

O papel principal dessas duas bibilotecas é usá-las combinadas a fim de conseguir plotar os gráficos que são tão necessários dentro do estudo de GA. Com a `matplotlib`, usamos a classe `import matplotlib.pyplot as plt`, os outros imports são:

```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt 
```
Para começar a plotar os gráficos, usamos as seguintes funções:

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

Vejamos um exemplo com a função $y^2 = 4ax$, sendo $a>0$:

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
