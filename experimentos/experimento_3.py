from equacoes.heuristicas import dist_euclidiana, dist_manhattan
import gerador_de_entradas, A_estrela.A_estrela as As
import viewer

def run_experimento_2():

    entradas = []

    for _ in range(20):
        entradas.append(gerador_de_entradas.gerar_entrada(0.2))
    
    # mostrar entradas

    tabela_resultados_a = []
    tabela_resultados_b = []
    tabela_resultados_c = []
    tabela_resultados_d = []
    tabela_resultados_e = []
    tabela_resultados_f = []

    for entrada in entradas:
        tabela_resultados_a.append(As.a_estrela(entrada, dist_euclidiana, 1))
        tabela_resultados_b.append(As.a_estrela(entrada, dist_euclidiana, 3))
        tabela_resultados_c.append(As.a_estrela(entrada, dist_euclidiana, 6))
        tabela_resultados_d.append(As.a_estrela(entrada, dist_manhattan, 1))
        tabela_resultados_e.append(As.a_estrela(entrada, dist_manhattan, 3))
        tabela_resultados_f.append(As.a_estrela(entrada, dist_manhattan, 6))

    viewer.visualizar_grid(entradas[0], tabela_resultados_a[0][0], 'A estrela')