import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def visualizar_grid(matriz: np.ndarray, caminho: list[tuple[int, int]], algoritmo = ''):
    fig, ax = plt.subplots(figsize=(8, 8))
    
    cmap = ListedColormap(['#404040', '#F0F0F0'])
    
    ax.imshow(matriz, cmap=cmap, vmin=-1, vmax=0)

    if caminho:
        y_coords = [passo[0] for passo in caminho]
        x_coords = [passo[1] for passo in caminho]
        
        ax.plot(x_coords, y_coords, color='#007BFF', linewidth=3, label='Caminho', zorder=1)
        
        ax.scatter(x_coords[0], y_coords[0], color='#28A745', s=200, label='Origem', zorder=2)
        
        ax.scatter(x_coords[-1], y_coords[-1], color='#DC3545', s=300, marker='*', label='Destino', zorder=2)

    ax.set_xticks(np.arange(-0.5, 15, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 15, 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
    ax.tick_params(which="minor", size=0)
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.title(algoritmo)
    plt.legend()
    plt.show()