import gerador_de_entradas
import Subida_de_Enconsta.subida_de_encosta as sde
import viewer
from data.save import salvar_dados_agregados, salvar_dados_brutos, salvar_mapas_em_txt
from equacoes.heuristicas import dist_euclidiana, dist_manhattan


def run_experimento():
    num_execucoes = 15
    entradas = []

    print("Gerando mapas...")
    for _ in range(num_execucoes):
        entradas.append(gerador_de_entradas.gerar_entrada(0.0))

    mapas_por_densidade = {0.0: entradas}
    salvar_mapas_em_txt(mapas_por_densidade, "mapas_experimento_1.txt", 1)

    tabela_resultados_a = []
    tabela_resultados_b = []
    tabela_resultados_c = []
    tabela_resultados_d = []
    tabela_resultados_e = []
    tabela_resultados_f = []

    print("Executando algoritmos...")
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

    algoritmos = [
        ("SdE Gulosa Det. (Euclidiana)", tabela_resultados_a),
        ("SdE Gulosa Det. (Manhattan)", tabela_resultados_b),
        ("SdE Maior Aclive (Euclidiana)", tabela_resultados_c),
        ("SdE Maior Aclive (Manhattan)", tabela_resultados_d),
        ("SdE Gulosa Estoc. (Euclidiana)", tabela_resultados_e),
        ("SdE Gulosa Estoc. (Manhattan)", tabela_resultados_f),
    ]

    resultados_brutos = []
    agregados = {0.0: {}}

    for nome_algo, tabela in algoritmos:
        agregados[0.0][nome_algo] = {
            "gerados": 0,
            "visitados": 0,
            "custo": 0,
            "sucessos": 0,
        }

    for i in range(num_execucoes):
        id_mapa = f"Mapa_0%_{i + 1}"

        for nome_algo, tabela in algoritmos:
            res = tabela[i]
            caminho, gerados, visitados, custo, sucesso = res
            status_sucesso = "Sim" if sucesso else "Não"

            resultados_brutos.append(
                f"| {id_mapa} | 0% | {nome_algo} | {gerados} | {visitados} | {custo} | {status_sucesso} |"
            )

            agregados[0.0][nome_algo]["gerados"] += gerados
            agregados[0.0][nome_algo]["visitados"] += visitados
            if sucesso:
                agregados[0.0][nome_algo]["custo"] += custo
                agregados[0.0][nome_algo]["sucessos"] += 1

    salvar_dados_brutos("resultados_brutos_exp1.md", resultados_brutos, 1)
    salvar_dados_agregados("resultados_agregados_exp1.md", agregados, num_execucoes, 1)
    print("Relatórios exportados com sucesso em Markdown!")
    print("Resultados brutos e agregados salvos na pasta 'resultados/'.")

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
