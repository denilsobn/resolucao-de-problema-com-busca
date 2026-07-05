from equacoes.heuristicas import dist_euclidiana, dist_manhattan
import gerador_de_entradas
import Subida_de_Enconsta.subida_de_encosta as sde

def run_experimento_1():

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
        tabela_resultados_a.append(sde.sde_gulosa_deterministica(entrada, dist_euclidiana, (0, 0), (14, 14)))
        tabela_resultados_b.append(sde.sde_gulosa_deterministica(entrada, dist_manhattan, (0, 0), (14, 14)))
        tabela_resultados_c.append(sde.sde_maior_aclive(entrada, dist_euclidiana, (0, 0), (14, 14)))
        tabela_resultados_d.append(sde.sde_maior_aclive(entrada, dist_manhattan, (0, 0), (14, 14)))
        tabela_resultados_e.append(sde.sde_gulosa_estocastica(entrada, dist_euclidiana, (0, 0), (14, 14)))
        tabela_resultados_f.append(sde.sde_gulosa_estocastica(entrada, dist_manhattan, (0, 0), (14, 14)))

    
