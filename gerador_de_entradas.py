import math
from collections import deque

import numpy as np


def gerar_entrada(porcetagem: float) -> np.ndarray:

    while True:
        matriz = np.random.randint(3, 7, size=(15, 15))
        blocos = math.floor(225 * porcetagem)

        for _ in range(blocos):
            x = np.random.randint(0, 15)
            y = np.random.randint(0, 15)

            while (x == 0 and y == 0) or (x == 14 and y == 14) or matriz[x][y] == -1:
                x = np.random.randint(0, 15)
                y = np.random.randint(0, 15)

            matriz[x][y] = -1

        if isValid(matriz, (0, 0), (14, 14)):
            return matriz


def isValid(
    matriz: np.ndarray,
    origem: tuple[int, int] = (0, 0),
    destino: tuple[int, int] = (14, 14),
) -> bool:

    vis = np.zeros((15, 15), dtype=bool)
    vis[origem[0]][origem[1]] = True
    q = deque([origem])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < 15
                and 0 <= ny < 15
                and matriz[nx][ny] != -1
                and not vis[nx][ny]
            ):
                vis[nx][ny] = True
                if (nx, ny) == destino:
                    return True
                q.append((nx, ny))

    return False
