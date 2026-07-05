import A_estrela.A_estrela as As
import Busca_Gulosa.busca_gulosa as bg
import gerador_de_entradas
import Subida_de_Enconsta.subida_de_encosta as sde
import viewer
from equacoes.heuristicas import dist_manhattan
from data.save import salvar_mapas_em_txt


def run_experimento():
    densidades = [0.1, 0.2, 0.3, 0.4]

    mapas_por_densidade = {d: [] for d in densidades}

    print("Gerando mapas...")
    for d in densidades:
        for _ in range(20):
            mapas_por_densidade[d].append(gerador_de_entradas.gerar_entrada(d))

    salvar_mapas_em_txt(
        mapas_por_densidade,
    )
    print("Mapas salvos em 'mapas_experimento_4.txt'.")

    resultados_brutos = []
    agregados = {}

    print("Executando os algoritmos...")
    for d in densidades:
        agregados[d] = {
            "SdE Maior Aclive": {
                "gerados": 0,
                "visitados": 0,
                "custo": 0,
                "sucessos": 0,
            },
            "Busca Gulosa": {"gerados": 0, "visitados": 0, "custo": 0, "sucessos": 0},
            "A*": {"gerados": 0, "visitados": 0, "custo": 0, "sucessos": 0},
        }

        for i, mapa in enumerate(mapas_por_densidade[d]):
            id_mapa = f"Mapa_{int(d * 100)}%_{i + 1}"

            res_sde = sde.sde_maior_aclive(mapa, dist_manhattan)
            res_bg = bg.busca_gulosa(mapa, dist_manhattan)
            res_as = As.a_estrela(mapa, dist_manhattan, 1)

            algoritmos = [
                ("SdE Maior Aclive", res_sde),
                ("Busca Gulosa", res_bg),
                ("A*", res_as),
            ]

            for nome_algo, res in algoritmos:
                caminho, gerados, visitados, custo, sucesso = res

                status_sucesso = "Sim" if sucesso else "Não"
                resultados_brutos.append(
                    f"| {id_mapa} | {int(d * 100)}% | {nome_algo} | {gerados} | {visitados} | {custo} | {status_sucesso} |"
                )

                agregados[d][nome_algo]["gerados"] += gerados
                agregados[d][nome_algo]["visitados"] += visitados
                if sucesso:
                    agregados[d][nome_algo]["custo"] += custo
                    agregados[d][nome_algo]["sucessos"] += 1

    with open("relatorio_experimento_4.md", "w", encoding="utf-8") as f:
        f.write("# Resultados do Experimento 4\n\n")

        f.write("## 1. Dados Agregados (Médias e Taxa de Sucesso)\n\n")
        f.write(
            "| Densidade | Algoritmo | Média Gerados | Média Visitados | Média Custo (Soluções) | Taxa de Sucesso |\n"
        )
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")

        for d in densidades:
            for algo, stats in agregados[d].items():
                med_gerados = stats["gerados"] / 20
                med_visitados = stats["visitados"] / 20
                taxa_suc = (stats["sucessos"] / 20) * 100

                if stats["sucessos"] > 0:
                    med_custo = stats["custo"] / stats["sucessos"]
                else:
                    med_custo = 0

                f.write(
                    f"| {int(d * 100)}% | {algo} | {med_gerados:.1f} | {med_visitados:.1f} | {med_custo:.1f} | {taxa_suc:.1f}% |\n"
                )

        f.write("\n---\n\n")

        f.write("## 2. Dados Brutos de Todas as Execuções\n\n")
        f.write(
            "| Mapa | Densidade | Algoritmo | Gerados | Visitados | Custo | Sucesso |\n"
        )
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for linha in resultados_brutos:
            f.write(linha + "\n")

    print("Experimento 4 concluído! Verifique os arquivos gerados.")

    primeiro_mapa = mapas_por_densidade[0.1][0]
    res_a1 = sde.sde_maior_aclive(primeiro_mapa, dist_manhattan)
    res_b1 = bg.busca_gulosa(primeiro_mapa, dist_manhattan)
    res_c1 = As.a_estrela(primeiro_mapa, dist_manhattan, 1)

    viewer.visualizar_grid(
        primeiro_mapa,
        res_a1[0],
        f"SdE Maior Aclive com dist_manhattan (Sucesso: {res_a1[-1]})",
    )
    viewer.visualizar_grid(
        primeiro_mapa,
        res_b1[0],
        f"Busca Gulosa com dist_manhattan (Sucesso: {res_b1[-1]})",
    )
    viewer.visualizar_grid(
        primeiro_mapa,
        res_c1[0],
        f"A* com dist_manhattan (Sucesso: {res_c1[-1]})",
    )
