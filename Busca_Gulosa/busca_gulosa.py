import heapq
from typing import Callable

from numpy import ndarray

MOVIMENTOS_NLSO = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def busca_gulosa(
    matriz: ndarray,
    func_heuristica: Callable[[tuple[int, int], tuple[int, int]], int],
    origem: tuple[int, int] = (0, 0),
    destino: tuple[int, int] = (14, 14),
) -> tuple[list[tuple[int, int]], int, int, int]:

    fila_prioridade = [(func_heuristica(origem, destino), 0, origem)]
    estados_gerados = estados_visitados = 0

    explorado = set([origem])
    parent = {}

    while fila_prioridade:
        estados_visitados += 1

        h_atual, g_atual, atual = heapq.heappop(fila_prioridade)

        if atual == destino:
            caminho = path(origem, destino, parent)
            return caminho, estados_gerados, estados_visitados, g_atual, True

        for dx, dy in MOVIMENTOS_NLSO:
            nx, ny = atual[0] + dx, atual[1] + dy

            if 0 <= nx < 15 and 0 <= ny < 15 and matriz[nx][ny] != -1:
                if (nx, ny) not in explorado:
                    estados_gerados += 1
                    explorado.add((nx, ny))
                    parent[(nx, ny)] = atual

                    novo_g = g_atual + int(matriz[nx][ny])

                    fn = func_heuristica((nx, ny), destino)

                    heapq.heappush(fila_prioridade, (fn, novo_g, (nx, ny)))

    return [], estados_gerados, estados_visitados, 0, False


def path(
    origem: tuple[int, int], destino: tuple[int, int], parent: dict
) -> list[tuple[int, int]]:
    caminho = []
    curr = destino
    while curr in parent:
        caminho.append(curr)
        curr = parent[curr]
    caminho.append(origem)
    caminho.reverse()
    return caminho
