import gerador_de_entradas
import Subida_de_Enconsta.subida_de_encosta as sde
import viewer
from equacoes.heuristicas import dist_euclidiana, dist_manhattan


def run_experimento():

    entradas = []

    for _ in range(15):
        entradas.append(gerador_de_entradas.gerar_entrada(0))

    # mostrar entradas

    tabela_resultados_a = []
    tabela_resultados_b = []
    tabela_resultados_c = []
    tabela_resultados_d = []
    tabela_resultados_e = []
    tabela_resultados_f = []

    for entrada in entradas:
        tabela_resultados_a.append(
            sde.sde_gulosa_deterministica(entrada, dist_euclidiana, (0, 0), (14, 14))
        )
        tabela_resultados_b.append(
            sde.sde_gulosa_deterministica(entrada, dist_manhattan, (0, 0), (14, 14))
        )
        tabela_resultados_c.append(
            sde.sde_maior_aclive(entrada, dist_euclidiana, (0, 0), (14, 14))
        )
        tabela_resultados_d.append(
            sde.sde_maior_aclive(entrada, dist_manhattan, (0, 0), (14, 14))
        )
        tabela_resultados_e.append(
            sde.sde_gulosa_estocastica(entrada, dist_euclidiana, (0, 0), (14, 14))
        )
        tabela_resultados_f.append(
            sde.sde_gulosa_estocastica(entrada, dist_manhattan, (0, 0), (14, 14))
        )

    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_a[0][0],
        "sde_gulosa_deterministica com dist_euclidiana",
    )
    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_b[0][0],
        "sde_gulosa_deterministica com dist_manhattan",
    )
    viewer.visualizar_grid(
        entradas[0], tabela_resultados_c[0][0], "sde_maior_aclive com dist_euclidiana"
    )
    viewer.visualizar_grid(
        entradas[0], tabela_resultados_d[0][0], "sde_maior_aclive com dist_manhattan"
    )
    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_e[0][0],
        "sde_gulosa_estocastica com dist_euclidiana",
    )
    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_f[0][0],
        "sde_gulosa_estocastica com dist_manhattan",
    )
