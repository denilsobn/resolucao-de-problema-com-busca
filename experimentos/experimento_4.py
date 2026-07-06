import A_estrela.A_estrela as As
import Busca_Gulosa.busca_gulosa as bg
import gerador_de_entradas
import Subida_de_Enconsta.subida_de_encosta as sde
import viewer
from data.save import salvar_dados_agregados, salvar_dados_brutos, salvar_mapas_em_txt
from equacoes.heuristicas import dist_manhattan


def run_experimento():
    num_execucoes = 20

    entradas_10 = []
    entradas_20 = []
    entradas_30 = []
    entradas_40 = []

    for _ in range(num_execucoes):
        entradas_10.append(gerador_de_entradas.gerar_entrada(0.1))
        entradas_20.append(gerador_de_entradas.gerar_entrada(0.2))
        entradas_30.append(gerador_de_entradas.gerar_entrada(0.3))
        entradas_40.append(gerador_de_entradas.gerar_entrada(0.4))

    mapas_por_densidade = {
        0.1: entradas_10,
        0.2: entradas_20,
        0.3: entradas_30,
        0.4: entradas_40,
    }
    salvar_mapas_em_txt(mapas_por_densidade, "mapas_experimento_4.txt")

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

    print("Executando algoritmos...")
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

    densidades_resultados = [
        (0.1, tabela_resultados_a1, tabela_resultados_b1, tabela_resultados_c1),
        (0.2, tabela_resultados_a2, tabela_resultados_b2, tabela_resultados_c2),
        (0.3, tabela_resultados_a3, tabela_resultados_b3, tabela_resultados_c3),
        (0.4, tabela_resultados_a4, tabela_resultados_b4, tabela_resultados_c4),
    ]

    resultados_brutos = []
    agregados = {0.1: {}, 0.2: {}, 0.3: {}, 0.4: {}}

    for densidade, tab_a, tab_b, tab_c in densidades_resultados:
        nomes_algoritmos = [
            ("SdE Maior Aclive", tab_a),
            ("Busca Gulosa", tab_b),
            ("A*", tab_c),
        ]

        for nome_algo, tabela in nomes_algoritmos:
            agregados[densidade][nome_algo] = {
                "gerados": 0,
                "visitados": 0,
                "custo": 0,
                "sucessos": 0,
            }

            for i, res in enumerate(tabela):
                id_mapa = f"Mapa_{int(densidade * 100)}%_{i + 1}"
                caminho, gerados, visitados, custo, sucesso = res
                status_sucesso = "Sim" if sucesso else "Não"

                resultados_brutos.append(
                    f"| {id_mapa} | {int(densidade * 100)}% | {nome_algo} | {gerados} | {visitados} | {custo} | {status_sucesso} |"
                )
                agregados[densidade][nome_algo]["gerados"] += gerados
                agregados[densidade][nome_algo]["visitados"] += visitados
                if sucesso:
                    agregados[densidade][nome_algo]["custo"] += custo
                    agregados[densidade][nome_algo]["sucessos"] += 1

    salvar_dados_brutos("resultados_brutos_exp4.md", resultados_brutos)
    salvar_dados_agregados("resultados_agregados_exp4.md", agregados, num_execucoes)
    print("Relatórios do Experimento 4 exportados com sucesso em Markdown!")
    print("Resultados brutos e agregados salvos na pasta 'resultados/'.")

    viewer.visualizar_grid(
        entradas_10[0],
        tabela_resultados_a1[0][0],
        f"sde maior_aclive com dist_manhattan (Sucesso: {tabela_resultados_a1[0][-1]})",
    )
    viewer.visualizar_grid(
        entradas_10[0],
        tabela_resultados_b1[0][0],
        f"busca gulosa com dist_manhattan (Sucesso: {tabela_resultados_b1[0][-1]})",
    )
    viewer.visualizar_grid(
        entradas_10[0],
        tabela_resultados_c1[0][0],
        f"A* com dist_manhattan (Sucesso: {tabela_resultados_c1[0][-1]})",
    )
