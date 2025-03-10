import networkx as nx
import matplotlib.pyplot as plt
import time
from typing import Tuple

def gerar_grafo_conexo(num_vertices: int, num_arestas: int) -> nx.Graph:
    """
    Gera um grafo conexo determinístico.

    Args:
        num_vertices (int): Número de vértices do grafo.
        num_arestas (int): Número de arestas adicionais para cada vértice.

    Returns:
        nx.Graph: Um grafo conexo determinístico com os parâmetros fornecidos.
    """
    grafo = nx.Graph()
    grafo.add_nodes_from(range(1, num_vertices + 1))
    
    # Criando uma árvore determinística para garantir conectividade
    for i in range(2, num_vertices + 1):
        grafo.add_edge(i, i - 1)
    
    # Adicionando arestas extras determinísticas
    for i in range(1, num_vertices + 1):
        for j in range(1, num_arestas):
            destino = (i + j) % num_vertices  # Padrão fixo para previsibilidade
            if destino != i:
                grafo.add_edge(i, destino)
    
    return grafo

def gerar_grafo_kn(num_vertices: int) -> nx.Graph:
    """Gera um grafo completo Kn com o número de vértices especificado."""
    grafo = nx.complete_graph(num_vertices)
    grafo = nx.relabel_nodes(grafo, {i: i+1 for i in grafo.nodes})
    return grafo
    """Gera um grafo completo Kn com o número de vértices especificado."""
    grafo = nx.complete_graph(num_vertices)
    grafo = nx.relabel_nodes(grafo, {i: i+1 for i in grafo.nodes})
    return grafo

def visualizar_grafo(grafo: nx.Graph, titulo: str, inicio: int, fim: int) -> None:
    """
    Exibe uma visualização do grafo gerado com nós de início e fim destacados.
    """
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(grafo, seed=42)
    
    nx.draw(grafo, pos, node_size=20, edge_color="gray", alpha=0.6)
    nx.draw_networkx_nodes(grafo, pos, nodelist=[inicio], node_color='green', label="Início", node_size=100)
    nx.draw_networkx_nodes(grafo, pos, nodelist=[fim], node_color='red', label="Fim", node_size=100)
    plt.title(titulo)
    plt.legend()
    plt.show()

def busca_largura(grafo: nx.Graph, inicio: int, fim: int):
    """
    Implementa a busca em largura (BFS) sem utilizar funções prontas.
    """
    fila = [(inicio, [inicio])]
    visitados = set()
    
    while fila:
        (atual, caminho) = fila.pop(0)
        if atual == fim:
            return caminho
        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo.neighbors(atual):
                fila.append((vizinho, caminho + [vizinho]))
    return []

def busca_profundidade(grafo: nx.Graph, inicio: int, fim: int):
    """
    Implementa a busca em profundidade (DFS) usando pilha.
    """
    pilha = [(inicio, [inicio])]
    visitados = set()
    
    while pilha:
        (atual, caminho) = pilha.pop()
        if atual == fim:
            return caminho
        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo.neighbors(atual):
                pilha.append((vizinho, caminho + [vizinho]))
    return []

def escolher_grafo() -> Tuple[str, nx.Graph]:
    """Permite ao usuário escolher um grafo a partir das opções disponíveis."""
    opcoes = [(i, v, k, f"Grafo com {v} vértices e {k} arestas") 
               for i, (v, k) in enumerate([(v, k) for v in [500, 5000, 10000] for k in [3, 5, 7]], start=1)]
    opcoes.append((10, 10000, "Kn", "Grafo Completo com 10000 vértices"))
    
    while True:
        print("Escolha um dos grafos para gerar:")
        for i, _, _, descricao in opcoes:
            print(f"{i}: {descricao}")
        
        try:
            escolha = int(input("Digite o número do grafo desejado: "))
            if 1 <= escolha <= 9:
                _, v, k, descricao = opcoes[escolha - 1]
                return descricao, gerar_grafo_conexo(v, k)
            elif escolha == 10:
                _, v, _, descricao = opcoes[-1]
                return descricao, gerar_grafo_kn(v)
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número correspondente à opção desejada.")

grafo_escolhido, grafo = escolher_grafo()
if grafo:
    print(f"{grafo_escolhido} gerado com sucesso!")
    
    num_vertices = max(grafo.nodes)
    while True:
        try:
            inicio = int(input(f"Digite o nó de início (1 a {num_vertices}): "))
            fim = int(input(f"Digite o nó de fim (1 a {num_vertices}): "))
            if 1 <= inicio <= num_vertices and 1 <= fim <= num_vertices:
                break
            else:
                print("Os valores devem estar dentro do intervalo válido!")
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")
    
    while True:
        escolha_busca = input("Escolha o algoritmo de busca (L para Busca em Largura, P para Busca em Profundidade): ").strip().upper()
        if escolha_busca == 'L':
            algoritmo = busca_largura
            break
        elif escolha_busca == 'P':
            algoritmo = busca_profundidade
            break
        else:
            print("Opção inválida! Digite 'L' para Busca em Largura ou 'P' para Busca em Profundidade.")
    
    inicio_tempo = time.time()
    caminho = algoritmo(grafo, inicio, fim)
    fim_tempo = time.time()
    
    if caminho:
        print("Caminho encontrado:", caminho)
        print(f"Tamanho do caminho: {len(caminho)}")
    else:
        print("Nenhum caminho encontrado.")
    
    print(f"Tempo de execução: {fim_tempo - inicio_tempo:.6f} segundos")
    visualizar_grafo(grafo, grafo_escolhido, inicio, fim)
