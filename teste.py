import networkx as nx
import random
import time

# Função para gerar um grafo e representá-lo como um dicionário de adjacência
def gerar_grafo(numVertices, numArestas):
    numTotalArestas = numVertices * numArestas // 2  # Garante conectividade
    grafo_nx = nx.gnm_random_graph(numVertices, numTotalArestas)
    
    grafo = {i: [] for i in range(numVertices)}  # Dicionário de adjacência
    for u, v in grafo_nx.edges():
        grafo[u].append(v)
        grafo[v].append(u)  # Grafo não direcionado

    return grafo

# Algoritmo de busca em largura (BFS)
def busca_em_largura(grafo, inicio, objetivo):
    fila = [(inicio, [inicio])]  # (vértice atual, caminho percorrido)
    visitados = set()
    
    while fila:
        atual, caminho = fila.pop(0)
        if atual == objetivo:
            return caminho  # Caminho encontrado
        
        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    return None  # Caminho não encontrado

# Algoritmo de busca em profundidade (DFS)
def busca_em_profundidade(grafo, inicio, objetivo):
    pilha = [(inicio, [inicio])]
    visitados = set()
    
    while pilha:
        atual, caminho = pilha.pop()
        if atual == objetivo:
            return caminho
        
        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo[atual]:
                if vizinho not in visitados:
                    pilha.append((vizinho, caminho + [vizinho]))

    return None

# Algoritmo de busca em profundidade limitada (DLS)
def busca_em_profundidade_limitada(grafo, inicio, objetivo, limite):
    def dfs_limitado(no, caminho, profundidade):
        if no == objetivo:
            return caminho
        if profundidade >= limite:
            return None

        for vizinho in grafo[no]:
            if vizinho not in caminho:  # Evita ciclos
                resultado = dfs_limitado(vizinho, caminho + [vizinho], profundidade + 1)
                if resultado:
                    return resultado
        return None

    return dfs_limitado(inicio, [inicio], 0)

# Parâmetros
vertices = [500, 5000, 10000]
arestas = [3, 5, 7]
limite_profundidade = 10  # Limite arbitrário para o DLS

# Escolher um grafo aleatório para teste
numVertices = random.choice(vertices)
numArestas = random.choice(arestas)
grafo = gerar_grafo(numVertices, numArestas)

# Selecionar dois pontos aleatórios no grafo
ponto_inicio, ponto_fim = random.sample(list(grafo.keys()), 2)

# Executar as buscas e medir o tempo
print(f"Buscando caminho entre {ponto_inicio} e {ponto_fim} em um grafo de {numVertices} vértices e {numArestas} arestas por vértice.\n")

# Busca em Largura
inicio = time.time()
caminho_bfs = busca_em_largura(grafo, ponto_inicio, ponto_fim)
tempo_bfs = time.time() - inicio
print(f"BFS - Tempo: {tempo_bfs:.6f}s | Caminho encontrado: {len(caminho_bfs) if caminho_bfs else 'Nenhum'}")

# Busca em Profundidade
inicio = time.time()
caminho_dfs = busca_em_profundidade(grafo, ponto_inicio, ponto_fim)
tempo_dfs = time.time() - inicio
print(f"DFS - Tempo: {tempo_dfs:.6f}s | Caminho encontrado: {len(caminho_dfs) if caminho_dfs else 'Nenhum'}")

# Busca em Profundidade Limitada
inicio = time.time()
caminho_dls = busca_em_profundidade_limitada(grafo, ponto_inicio, ponto_fim, limite_profundidade)
tempo_dls = time.time() - inicio
print(f"DLS - Tempo: {tempo_dls:.6f}s | Caminho encontrado: {len(caminho_dls) if caminho_dls else 'Nenhum'}")
