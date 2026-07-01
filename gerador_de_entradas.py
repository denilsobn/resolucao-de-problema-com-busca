import numpy as np
from collections import queue

def gerar_entrada(porcetagem: int) -> np.ndarray:

    matriz = np.random.randint(3, 7, size=(15, 15))
    blocos = int(225 * porcetagem)

    for _ in range(blocos):
        x = np.random.randint(0, 15)
        y = np.random.randint(0, 15)

        while matriz[x][y] == -1:
            x = np.random.randint(0, 15)
            y = np.random.randint(0, 15)

        matriz[x][y] = -1

    if (isValid(matriz)):
        return matriz
    else:
        return gerar_entrada(porcetagem)


def isValid(matriz: np.ndarray, origem: tuple[int, int], destino: tuple[int, int]) -> bool:

    vis = np.zeros((15, 15), dtype=bool)
    vis[origem[0]][origem[1]] = True
    q = queue([origem])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while not q.empty():
        x, y = q.front()
        q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 15 and 0 <= ny < 15 and matriz[nx][ny] != -1 and not vis[nx][ny]:
                vis[nx][ny] = True
                if (nx, ny) == destino:
                    return True
                q.push((nx, ny))


    return False



    





