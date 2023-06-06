import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Função que representa o cone
def cone_func(x, y):
    return np.sqrt(x**2 + y**2)

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