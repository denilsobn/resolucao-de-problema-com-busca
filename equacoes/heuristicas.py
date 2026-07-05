from math import sqrt


def dist_euclidiana(origem: tuple[int, int], destino: tuple[int, int]) -> float:
    x1, y1 = origem
    x2, y2 = destino

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def dist_manhattan(origem: tuple[int, int], destino: tuple[int, int]) -> float:
    x1, y1 = origem
    x2, y2 = destino

    return abs(x1 - x2) + abs(y1 - y2)
