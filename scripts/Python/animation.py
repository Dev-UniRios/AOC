import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Configurações para os dispositivos, CPU e Barramento
devices = ['CPU', 'Bus', 'Memory', 'Printer']
positions = [(0, 0), (1, 1), (2, 0), (3, 1)]  # Posições de onde os dispositivos vão estar

# Configurando a figura para o gráfico
fig, ax = plt.subplots()
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 2)
ax.set_xticks([])
ax.set_yticks([])

# Criar os círculos que representam os dispositivos
circles = []
for pos in positions:
    circle = plt.Circle(pos, 0.1, color='blue', fill=True)
    circles.append(circle)
    ax.add_artist(circle)

# Adicionar os rótulos para os dispositivos
for i, pos in enumerate(positions):
    ax.text(pos[0], pos[1]+0.15, devices[i], ha='center', fontsize=12)

# Variáveis para animar o dado entre dispositivos
data_text = ax.text(0, 0, '', fontsize=12, color='red')

# Criar uma linha que simula o barramento (será atualizada durante a animação)
line, = ax.plot([], [], 'r-', lw=2)

# Função auxiliar para interpolação entre dois pontos
def interpolate(start, end, t):
    return (1 - t) * np.array(start) + t * np.array(end)

# Função para mover o dado e atualizar a linha do barramento
def animate(frame):
    # Fases da animação
    if frame < 10:  # CPU para Barramento
        pos = interpolate(positions[0], positions[1], frame / 10)
        data_text.set_position(pos)
        data_text.set_text("Data: 42")
        line.set_data([positions[0][0], pos[0]], [positions[0][1], pos[1]])  # Atualiza a linha
        
    elif frame < 20:  # Barramento para Memória
        pos = interpolate(positions[1], positions[2], (frame - 10) / 10)
        data_text.set_position(pos)
        data_text.set_text("Data: 42")
        line.set_data([positions[1][0], pos[0]], [positions[1][1], pos[1]])  # Atualiza a linha
        
    elif frame < 30:  # Memória para Impressora
        pos = interpolate(positions[2], positions[3], (frame - 20) / 10)
        data_text.set_position(pos)
        data_text.set_text("Data: 42")
        line.set_data([positions[2][0], pos[0]], [positions[2][1], pos[1]])  # Atualiza a linha
        
    else:  # Fim da animação
        data_text.set_text('Transf. completa')
        line.set_data([], [])  # Remove a linha no final

# Criar animação
ani = FuncAnimation(fig, animate, frames=40, interval=200)

# Salvar animação como GIF
gif_path = 'bus_simulation_with_line.gif'
ani.save(gif_path, writer='imagemagick')

gif_path
