import A_estrela.A_estrela as As
import Busca_Gulosa.busca_gulosa as bg
import gerador_de_entradas
from data.save import salvar_dados_agregados, salvar_dados_brutos, salvar_mapas_em_txt
from equacoes.heuristicas import dist_euclidiana, dist_manhattan
import viewer


def run_experimento():
    num_execucoes = 20
    densidade = 0.0
    entradas = []

    for _ in range(num_execucoes):
        entradas.append(gerador_de_entradas.gerar_entrada(densidade))

    mapas_por_densidade = {densidade: entradas}
    salvar_mapas_em_txt(mapas_por_densidade, "mapas_experimento_2.txt", 2)

    tabela_resultados_a = []
    tabela_resultados_b = []
    tabela_resultados_c = []
    tabela_resultados_d = []

    print("Executando algoritmos...")
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

    nomes_algoritmos = [
        ("Busca Gulosa (Euclidiana)", tabela_resultados_a),
        ("Busca Gulosa (Manhattan)", tabela_resultados_b),
        ("A Estrela (Euclidiana)", tabela_resultados_c),
        ("A Estrela (Manhattan)", tabela_resultados_d),
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

    for i in range(num_execucoes):
        id_mapa = f"Mapa_0%_{i + 1}"

        for nome_algo, tabela in nomes_algoritmos:
            res = tabela[i]
            caminho, gerados, visitados, custo, sucesso = res
            status_sucesso = "Sim" if sucesso else "Não"

            resultados_brutos.append(
                f"| {id_mapa} | 0% | {nome_algo} | {gerados} | {visitados} | {custo} | {status_sucesso} |"
            )

            agregados[densidade][nome_algo]["gerados"] += gerados
            agregados[densidade][nome_algo]["visitados"] += visitados
            if sucesso:
                agregados[densidade][nome_algo]["custo"] += custo
                agregados[densidade][nome_algo]["sucessos"] += 1

    salvar_dados_brutos("resultados_brutos_exp2.md", resultados_brutos, 2)
    salvar_dados_agregados("resultados_agregados_exp2.md", agregados, num_execucoes, 2)
    print("Relatórios do Experimento 2 exportados com sucesso em Markdown!")
    print("Resultados brutos e agregados salvos na pasta 'resultados/'.")

    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_a[0][0],
        2,
        f"busca gulosa com dist_euclidiana (Sucesso: {tabela_resultados_a[0][-1]})",
    )

    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_b[0][0],
        2,
        f"busca gulosa com dist_manhattan (Sucesso: {tabela_resultados_b[0][-1]})",
    )

    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_c[0][0],
        2,
        f"A Estrela com dist_euclidiana (Sucesso: {tabela_resultados_c[0][-1]})",
    )

    viewer.visualizar_grid(
        entradas[0],
        tabela_resultados_d[0][0],
        2,
        f"A Estrela com dist_manhattan (Sucesso: {tabela_resultados_d[0][-1]})",
    )
