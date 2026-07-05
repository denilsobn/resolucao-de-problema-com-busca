import heapq
from typing import Callable

from numpy import ndarray

MOVIMENTOS_NLSO = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def a_estrela(
    matriz: ndarray,
    func_heuristica: Callable[[tuple[int, int], tuple[int, int]], int],
    peso=1,
    origem: tuple[int, int] = (0, 0),
    destino: tuple[int, int] = (14, 14),
) -> tuple[list[tuple[int, int]], int, int, int]:

    fila_prioridade = [(func_heuristica(origem, destino) * peso, 0, origem)]
    estados_gerados = estados_visitados = 0

    g_custo = {origem: 0}
    parent = {}

    while fila_prioridade:
        estados_visitados += 1

        f_atual, g_atual, atual = heapq.heappop(fila_prioridade)

        if atual == destino:
            caminho = path(origem, destino, parent)

            return caminho, estados_gerados, estados_visitados, g_atual, True

        for dx, dy in MOVIMENTOS_NLSO:
            estados_gerados += 1
            nx, ny = atual[0] + dx, atual[1] + dy

            if 0 <= nx < 15 and 0 <= ny < 15 and matriz[nx][ny] != -1:
                novo_g = g_atual + int(matriz[nx][ny])

                if (nx, ny) not in g_custo or novo_g < g_custo[(nx, ny)]:
                    parent[(nx, ny)] = atual

                    g_custo[(nx, ny)] = novo_g

                    fn = novo_g + func_heuristica((nx, ny), destino) * peso

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
