import A_estrela.A_estrela as As
import Busca_Gulosa.busca_gulosa as bg
import gerador_de_entradas
from equacoes.heuristicas import dist_euclidiana, dist_manhattan


def run_experimento():

    entradas = []

    for _ in range(20):
        entradas.append(gerador_de_entradas.gerar_entrada(0))

    # mostrar entradas

    tabela_resultados_a = []
    tabela_resultados_b = []
    tabela_resultados_c = []
    tabela_resultados_d = []

    for entrada in entradas:
        tabela_resultados_a.append(
            bg.busca_gulosa(entrada, dist_euclidiana, (0, 0), (14, 14))
        )
        tabela_resultados_b.append(
            bg.busca_gulosa(entrada, dist_manhattan, (0, 0), (14, 14))
        )
        tabela_resultados_c.append(
            As.a_estrela(entrada, dist_euclidiana, 1, (0, 0), (14, 14))
        )
        tabela_resultados_d.append(
            As.a_estrela(entrada, dist_manhattan, 1, (0, 0), (14, 14))
        )
