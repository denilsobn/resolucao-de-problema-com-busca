import A_estrela.A_estrela as As
import gerador_de_entradas
import viewer
from data.save import salvar_dados_agregados, salvar_dados_brutos, salvar_mapas_em_txt
from equacoes.heuristicas import dist_euclidiana, dist_manhattan


def run_experimento():
    num_execucoes = 20
    densidade = 0.2
    entradas = []

    for _ in range(num_execucoes):
        entradas.append(gerador_de_entradas.gerar_entrada(densidade))

    mapas_por_densidade = {densidade: entradas}
    salvar_mapas_em_txt(mapas_por_densidade, "mapas_experimento_3.txt")

    tabela_resultados_a = []
    tabela_resultados_b = []
    tabela_resultados_c = []
    tabela_resultados_d = []
    tabela_resultados_e = []
    tabela_resultados_f = []

    print("Executando algoritmos...")
    for entrada in entradas:
        tabela_resultados_a.append(As.a_estrela(entrada, dist_euclidiana, 1))
        tabela_resultados_b.append(As.a_estrela(entrada, dist_euclidiana, 3))
        tabela_resultados_c.append(As.a_estrela(entrada, dist_euclidiana, 6))
        tabela_resultados_d.append(As.a_estrela(entrada, dist_manhattan, 1))
        tabela_resultados_e.append(As.a_estrela(entrada, dist_manhattan, 3))
        tabela_resultados_f.append(As.a_estrela(entrada, dist_manhattan, 6))

    print("Processando dados para tabelas...")

    nomes_algoritmos = [
        ("A* (h1 = 1x D_E)", tabela_resultados_a),
        ("A* (h2 = 3x D_E)", tabela_resultados_b),
        ("A* (h3 = 6x D_E)", tabela_resultados_c),
        ("A* (h4 = 1x D_M)", tabela_resultados_d),
        ("A* (h5 = 3x D_M)", tabela_resultados_e),
        ("A* (h6 = 6x D_M)", tabela_resultados_f),
    ]

    resultados_brutos = []
    agregados = {densidade: {}}

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

            # Linha para a tabela bruta
            resultados_brutos.append(
                f"| {id_mapa} | {int(densidade * 100)}% | {nome_algo} | {gerados} | {visitados} | {custo} | {status_sucesso} |"
            )

            # Acumulando para a tabela agregada
            agregados[densidade][nome_algo]["gerados"] += gerados
            agregados[densidade][nome_algo]["visitados"] += visitados
            if sucesso:
                agregados[densidade][nome_algo]["custo"] += custo
                agregados[densidade][nome_algo]["sucessos"] += 1

    salvar_dados_brutos("resultados_brutos_exp3.md", resultados_brutos)
    salvar_dados_agregados("resultados_agregados_exp3.md", agregados, num_execucoes)
    print("Relatórios do Experimento 3 exportados com sucesso em Markdown!")
    print("Resultados brutos e agregados salvos na pasta 'resultados/'.")

    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_a[0][0],
        f"A* (h1 = 1x D_E) - Sucesso: {tabela_resultados_a[0][-1]}",
    )
