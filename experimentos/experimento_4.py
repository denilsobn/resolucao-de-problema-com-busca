from equacoes.heuristicas import dist_euclidiana, dist_manhattan
import gerador_de_entradas, A_estrela.A_estrela as As, Busca_Gulosa.busca_gulosa as bg, Subida_de_Enconsta.subida_de_encosta as sde
import viewer

def run_experimento_2():

    entradas_10 = []
    entradas_20 = []
    entradas_30 = []
    entradas_40 = []

    for _ in range(20):
        entradas_10.append(gerador_de_entradas.gerar_entrada(0.1))
        entradas_20.append(gerador_de_entradas.gerar_entrada(0.2))
        entradas_30.append(gerador_de_entradas.gerar_entrada(0.3))
        entradas_40.append(gerador_de_entradas.gerar_entrada(0.4))
    
    # mostrar entradas

    tabela_resultados_a1 = []
    tabela_resultados_a2 = []
    tabela_resultados_a3 = []
    tabela_resultados_a4 = []

    tabela_resultados_b1 = []
    tabela_resultados_b2 = []
    tabela_resultados_b3 = []
    tabela_resultados_b4 = []

    tabela_resultados_c1 = []
    tabela_resultados_c2 = []
    tabela_resultados_c3 = []
    tabela_resultados_c4 = []

    for entrada in entradas_10:
        tabela_resultados_a1.append(sde.sde_maior_aclive(entrada, dist_manhattan))
        tabela_resultados_b1.append(bg.busca_gulosa(entrada, dist_manhattan))
        tabela_resultados_c1.append(As.a_estrela(entrada, dist_manhattan, 1))

    for entrada in entradas_20:
        tabela_resultados_a2.append(sde.sde_maior_aclive(entrada, dist_manhattan))
        tabela_resultados_b2.append(bg.busca_gulosa(entrada, dist_manhattan))
        tabela_resultados_c2.append(As.a_estrela(entrada, dist_manhattan, 1))

    for entrada in entradas_30:
        tabela_resultados_a3.append(sde.sde_maior_aclive(entrada, dist_manhattan))
        tabela_resultados_b3.append(bg.busca_gulosa(entrada, dist_manhattan))
        tabela_resultados_c3.append(As.a_estrela(entrada, dist_manhattan, 1))

    for entrada in entradas_40:
        tabela_resultados_a4.append(sde.sde_maior_aclive(entrada, dist_manhattan))
        tabela_resultados_b4.append(bg.busca_gulosa(entrada, dist_manhattan))
        tabela_resultados_c4.append(As.a_estrela(entrada, dist_manhattan, 1))
        

    viewer.visualizar_grid(entradas_20[0], tabela_resultados_a1[0][0], 'A estrela')