# Resolução de Problemas com Busca — IA

Este repositório contém a implementação prática e a análise experimental de algoritmos de busca cega e heurística aplicados à navegação em labirintos matriciais $15 \times 15$ com custos de movimentação variáveis pesos de 3 a 6 e obstáculos peso -1. O projeto foi desenvolvido de forma modular, permitindo a execução de múltiplos cenários de teste de Experimentos 1 a 4 com geração automática de relatórios em formato Markdown e persistência dos mapas gerados.

---

## 🛠️ Tecnologias e Dependências

O projeto foi estruturado utilizando o gerenciador de pacotes **uv** e o ecossistema moderno do Python 3.12+.

* **Linguagem:** Python >= 3.12

* **Bibliotecas Principais:**
* `numpy` (Manipulação das matrizes e geração de números pseudoaleatórios)

* `matplotlib` (Interface gráfica para visualização do grid e caminhos)

* `pandas` (Opcional, utilizado em ramificações para agregação de dados)

* **Ferramentas de Desenvolvimento (Dev):**
* `pytest` (Suporte a testes unitários)

* `ruff` (Linter e formatador de código estrito)

---

## 📂 Estrutura do Projeto

A arquitetura do sistema foi projetada de forma modular para isolar os algoritmos de busca da lógica de experimentação e visualização:

```text
├── A_estrela/
│   ├── __init__.py
│   └── A_estrela.py          # Implementação do Algoritmo A* com peso dinâmico
├── Busca_Gulosa/
│   ├── __init__.py
│   └── busca_gulosa.py       # Implementação da Busca Gulosa (Greedy Best-First)
├── Subida_de_Enconsta/
│   ├── __init__.py
│   └── subida_de_encosta.py  # Implementações: Gulosa Det., Maior Aclive e Estocástica
├── equacoes/
│   └── heuristicas.py        # Distância Euclidiana (math.floor) e Manhattan
├── data/
│   └── save.py               # Módulo de persistência (Mapas TXT e Relatórios Markdown)
├── experimentos/
│   ├── __init__.py
│   ├── experimento_1.py      # Testes de Subida de Encosta (0% obstáculos)
│   ├── experimento_2.py      # Comparação Busca Gulosa vs A* (0% obstáculos)
│   ├── experimento_3.py      # A* com variação de pesos (20% obstáculos)
│   └── experimento_4.py      # Análise de estresse (Obstáculos de 10% a 40%)
├── resultados/
    ├── dados relatorio       # Dados usados para fazer o relatório
    ├── experimento_x         # Dados gerados automaticamente com o código
├── gerador_de_entradas.py    # Geração de grids pseudoaleatórios com validação BFS
├── viewer.py                 # Renderização visual dos grids e caminhos com Matplotlib
├── main.py                   # CLI central de execução dos experimentos
├── pyproject.toml            # Metadados do projeto e dependências
└── uv.lock                   # Lockfile para garantia de reprodutibilidade

```

---

## 🧠 Algoritmos e Heurísticas Implementados

### Heurísticas (`equacoes/heuristicas.py`)

1. **Distância Manhattan:** Adequada para movimentos estritamente ortogonais (norte, sul, leste, oeste).

2. **Distância Euclidiana:** Calcula a linha reta entre as coordenadas

### Algoritmos de Busca

* **Subida de Encosta (Hill Climbing):**
* *Gulosa Determinística:* Move-se para o primeiro vizinho estritamente melhor encontrado.

* *Maior Aclive:* Avalia todos os vizinhos ortogonais e escolhe aquele que maximiza o ganho heurístico.

* *Gulosa Estocástica:* Seleciona aleatoriamente um vizinho dentre todos os que melhoram a heurística atual.

* **Busca Gulosa (Greedy Best-First Search):** Utiliza uma fila de prioridades (`heapq`) baseada unicamente no valor da função heurística $f(n) = h(n)$.

* **Algoritmo A Estrela:** Combina o custo real acumulado com a estimativa heurística através da função $f(n) = g(n) + w \cdot h(n)$, onde $w$ representa o peso atribuído à heurística (útil para comportamento inflacionado).

---

## 📊 Descrição dos Experimentos

### Experimento 1: Variações de Subida de Encosta

* **Configuração:** 15 mapas com 0% de obstáculos.

* **Objetivo:** Avaliar o comportamento das três variantes de Subida de Encosta combinadas com as duas heurísticas, analisando a frequência de travamentos em ótimos locais mesmo em ambientes sem barreiras.

### Experimento 2: Busca Gulosa vs. Algoritmo A*

* **Configuração:** 20 mapas com 0% de obstáculos.

* **Objetivo:** Confrontar a Busca Gulosa e o A* ($w=1$) sob as duas métricas de distância. O foco é monitorar o número de nós gerados/visitados e validar a otimalidade do caminho quando $g(n)$ é considerado.

### Experimento 3: O Impacto do Peso Heurístico no A*

* **Configuração:** 20 mapas com 20% de densidade de obstáculos.

* **Objetivo:** Testar o comportamento do A* inflacionado utilizando multiplicadores de peso ($w = 1$, $w = 3$ e $w = 6$). Analisa-se a transição do algoritmo de um comportamento ótimo para uma busca direta similar à Gulosa.

### Experimento 4: Análise de Resiliência e Estresse

* **Configuração:** 80 mapas no total, divididos em 4 blocos de 20 instâncias com densidades de barreiras de 10%, 20%, 30% e 40%.

* **Objetivo:** Comparar o algoritmo de Subida de Encosta, Busca Gulosa e A* sob forte presença de obstáculos, medindo diretamente a Taxa de Sucesso e custos computacionais.

---

## 💾 Mecanismo de Salvamento e Relatórios

Para manter o repositório organizado e enxuto, o sistema realiza a persistência automática dos dados na pasta `resultados/` sem gerar complexidade de infraestrutura externa:

1. **`mapas_experimento_X.txt`**: Centraliza todas as matrizes geradas para aquele experimento em um único arquivo de texto puro, formatando colunas simétricas para legibilidade (usando caracteres alinhados para obstáculos `-1` e pesos de movimentação).

2. **`resultados_brutos_expX.md`**: Tabela Markdown detalhada contendo a performance individual (nós gerados, nós visitados, custo final do caminho e indicador de sucesso) de cada uma das execuções em cada mapa.

3. **`resultados_agregados_expX.md`**: Consolidação estatística exigida pela especificação do trabalho, apresentando de forma direta a **Média de Nós Gerados**, **Média de Nós Visitados**, **Média de Custo** (calculada estritamente sobre as execuções bem-sucedidas) e a **Taxa de Sucesso (%)**.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python 3.12 ou superior instalado. Recomenda-se o uso do **uv** para execução ágil.

### Instalação das dependências

Se estiver utilizando o `uv`, as dependências serão resolvidas automaticamente ao rodar o comando principal.

```bash
uv sync
```

Caso queira instalar manualmente via pip:

```bash
pip install numpy matplotlib pandas

```

### Execução via CLI Central

Para executar os testes e gerar os relatórios, basta rodar o script `main.py` na raiz do projeto:

```bash
python main.py

```

ou 

```bash
uv run main.py
```

O programa exibirá um menu interativo no terminal:

```text
Digite o número do experimento que deseja executar (0 para parar): 
1 - Experimento 1
2 - Experimento 2
3 - Experimento 3
4 - Experimento 4

```

Ao selecionar uma opção, o algoritmo executará as simulações em lote, criará o diretório `resultados/` com os respectivos arquivos `.txt` e `.md`.

---

### 👥 Integrantes

* Denilso Bernardo Nunes da Silva
* Antonio Willian Silva Oliveira
