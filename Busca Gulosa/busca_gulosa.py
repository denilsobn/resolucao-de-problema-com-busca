from collections import priority_queue
import numpy as np

def busca_gulosa(origem: tuple[int, int], destino: tuple[int, int], matriz: np.ndarray) -> list[tuple[int, int]]:
    q = priority_queue()
    
