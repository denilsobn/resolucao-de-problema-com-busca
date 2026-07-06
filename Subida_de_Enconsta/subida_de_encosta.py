import random
from typing import Callable

from numpy import ndarray

MOVIMENTOS_NLSO = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sde_gulosa_deterministica(
    matriz: ndarray,
    func_heuristica: Callable[[tuple[int, int], tuple[int, int]], float],
    origem: tuple[int, int] = (0, 0),
    destino: tuple[int, int] = (14, 14),
) -> tuple[list[tuple[int, int]], int, int, int, bool]:
    atual = origem
    caminho = [atual]
    estados_gerados = 0
    estados_visitados = 0
    custo_total = 0

    while atual != destino:
        estados_visitados += 1
        h_atual = func_heuristica(atual, destino)
        melhor_vizinho = None

        for dx, dy in MOVIMENTOS_NLSO:
            nx, ny = atual[0] + dx, atual[1] + dy

            if 0 <= nx < 15 and 0 <= ny < 15 and matriz[nx][ny] != -1:
                estados_gerados += 1
                vizinho = (nx, ny)
                h_vizinho = func_heuristica(vizinho, destino)

                if h_vizinho < h_atual:
                    melhor_vizinho = vizinho
                    break

        if melhor_vizinho is None:
            break

        custo_total += int(matriz[melhor_vizinho[0]][melhor_vizinho[1]])
        atual = melhor_vizinho
        caminho.append(atual)

    if atual == destino:
        estados_visitados += 1

    return caminho, estados_gerados, estados_visitados, custo_total, atual == destino


def sde_maior_aclive(
    matriz: ndarray,
    func_heuristica: Callable[[tuple[int, int], tuple[int, int]], float],
    origem: tuple[int, int] = (0, 0),
    destino: tuple[int, int] = (14, 14),
) -> tuple[list[tuple[int, int]], int, int, int, bool]:
    atual = origem
    caminho = [atual]
    estados_gerados = 0
    estados_visitados = 0
    custo_total = 0

    while atual != destino:
        estados_visitados += 1
        h_atual = func_heuristica(atual, destino)

        melhor_vizinho = None
        h_melhor_vizinho = h_atual

        for dx, dy in MOVIMENTOS_NLSO:
            nx, ny = atual[0] + dx, atual[1] + dy

            if 0 <= nx < 15 and 0 <= ny < 15 and matriz[nx][ny] != -1:
                estados_gerados += 1
                vizinho = (nx, ny)
                h_vizinho = func_heuristica(vizinho, destino)

                if h_vizinho < h_melhor_vizinho:
                    h_melhor_vizinho = h_vizinho
                    melhor_vizinho = vizinho

        if melhor_vizinho is None:
            break

        custo_total += int(matriz[melhor_vizinho[0]][melhor_vizinho[1]])
        atual = melhor_vizinho
        caminho.append(atual)

    if atual == destino:
        estados_visitados += 1

    return caminho, estados_gerados, estados_visitados, custo_total, atual == destino


def sde_gulosa_estocastica(
    matriz: ndarray,
    func_heuristica: Callable[[tuple[int, int], tuple[int, int]], float],
    origem: tuple[int, int] = (0, 0),
    destino: tuple[int, int] = (14, 14),
) -> tuple[list[tuple[int, int]], int, int, int, bool]:
    atual = origem
    caminho = [atual]
    estados_gerados = 0
    estados_visitados = 0
    custo_total = 0

    while atual != destino:
        estados_visitados += 1
        h_atual = func_heuristica(atual, destino)

        vizinhos_melhores = []

        for dx, dy in MOVIMENTOS_NLSO:
            nx, ny = atual[0] + dx, atual[1] + dy

            if 0 <= nx < 15 and 0 <= ny < 15 and matriz[nx][ny] != -1:
                estados_gerados += 1
                vizinho = (nx, ny)
                h_vizinho = func_heuristica(vizinho, destino)

                if h_vizinho < h_atual:
                    vizinhos_melhores.append(vizinho)

        if not vizinhos_melhores:
            break

        melhor_vizinho = random.choice(vizinhos_melhores)

        custo_total += int(matriz[melhor_vizinho[0]][melhor_vizinho[1]])
        atual = melhor_vizinho
        caminho.append(atual)

    if atual == destino:
        estados_visitados += 1

    return caminho, estados_gerados, estados_visitados, custo_total, atual == destino
