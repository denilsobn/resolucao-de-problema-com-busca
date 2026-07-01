from math import sqrt, floor


def dist_euclidiana(origem: tuple[int, int], destino: tuple[int, int]) -> int:
    x1, x2 = origem
    y1, y2 = destino

    return floor(sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2))


def dist_manhattan(origem: tuple[int, int], destino: tuple[int, int]) -> int:
    x1, x2 = origem
    y1, y2 = destino

    return abs(x1 - x2) + abs(y1 - y2)
