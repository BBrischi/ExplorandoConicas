# Parâmetros do cone
height = 2  # altura do cone
radius = 1  # raio da base do cone
resolution = 100  # resolução da grade de pontos

# Criação da grade de pontos para o cone
u = np.linspace(0, 2 * np.pi, resolution)
v = np.linspace(0, height, resolution)
u, v = np.meshgrid(u, v)
x = radius * (1 - v / height) * np.cos(u)
y = radius * (1 - v / height) * np.sin(u)
z = v

# Criação do gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plotagem do cone
ax.plot_surface(x, y, z, color='yellow', alpha=0.5)

# Personalização dos rótulos dos eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibição do gráfico
plt.show()