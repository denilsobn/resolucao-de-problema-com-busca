import os

if not os.path.exists("resultados"):
    os.makedirs("resultados")


def salvar_mapas_em_txt(
    mapas_por_densidade: dict[float, list], nome_arquivo: str = "mapas_experimento.txt"
):
    """
    Salva todos os mapas gerados num único arquivo de texto, alinhando as colunas.
    """
    nome_arquivo = os.path.join("resultados", nome_arquivo)

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for densidade, mapas in mapas_por_densidade.items():
            f.write(f"=== Mapas com Densidade {int(densidade * 100)}% ===\n\n")
            for i, mapa in enumerate(mapas):
                f.write(f"--- Mapa {i + 1} ---\n")
                for linha in mapa:
                    linha_str = " ".join(
                        f"{val if val != -1 else 'X':1}" for val in linha
                    )
                    f.write(linha_str + "\n")
                f.write("\n")


def salvar_dados_brutos(nome_arquivo: str, resultados_brutos: list):
    """
    Salva os dados brutos de todas as execuções em um arquivo de texto markdown.
    """
    nome_arquivo = os.path.join("resultados", nome_arquivo)

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("## Dados Brutos de Todas as Execuções\n\n")
        f.write(
            "| Mapa | Densidade | Algoritmo | Gerados | Visitados | Custo | Sucesso |\n"
        )
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for linha in resultados_brutos:
            f.write(linha + "\n")


def salvar_dados_agregados(nome_arquivo: str, agregados: dict, num_execucoes: int):
    """
    Salva as médias e taxas de sucesso em um arquivo Markdown.
    """
    nome_arquivo = os.path.join("resultados", nome_arquivo)

    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("## Dados Agregados (Médias e Taxa de Sucesso)\n\n")
        f.write(
            "| Densidade | Algoritmo | Média Gerados | Média Visitados | Média Custo (Soluções) | Taxa de Sucesso |\n"
        )
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")

        for densidade, resultados_algo in agregados.items():
            for algo, stats in resultados_algo.items():
                med_gerados = stats["gerados"] / num_execucoes
                med_visitados = stats["visitados"] / num_execucoes
                taxa_suc = (stats["sucessos"] / num_execucoes) * 100

                # A média de custo só conta execuções que encontraram o objetivo
                if stats["sucessos"] > 0:
                    med_custo = stats["custo"] / stats["sucessos"]
                else:
                    med_custo = 0

                f.write(
                    f"| {int(densidade * 100)}% | {algo} | {med_gerados:.1f} | {med_visitados:.1f} | {med_custo:.1f} | {taxa_suc:.1f}% |\n"
                )
