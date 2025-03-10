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
    grafo.add_nodes_from(range(num_vertices))
    
    # Criando uma árvore determinística para garantir conectividade
    for i in range(1, num_vertices):
        grafo.add_edge(i, i - 1)
    
    # Adicionando arestas extras determinísticas
    for i in range(num_vertices):
        for j in range(1, num_arestas):
            destino = (i + j) % num_vertices  # Padrão fixo para previsibilidade
            if destino != i:
                grafo.add_edge(i, destino)
    
    return grafo

def gerar_grafo_kn(num_vertices: int) -> nx.Graph:
    """
    Gera um grafo completo Kn com o número de vértices especificado.

    Args:
        num_vertices (int): Número de vértices do grafo completo.

    Returns:
        nx.Graph: Grafo completo com num_vertices vértices.
    """
    return nx.complete_graph(num_vertices)

def visualizar_grafo(grafo: nx.Graph, titulo: str, inicio: int, fim: int) -> None:
    """
    Exibe uma visualização do grafo gerado com nós de início e fim destacados.

    Args:
        grafo (nx.Graph): O grafo a ser visualizado.
        titulo (str): Título da visualização.
        inicio (int): Nó inicial destacado em verde.
        fim (int): Nó final destacado em vermelho.
    """
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(grafo, seed=42)  # Layout fixo para consistência

    nx.draw(grafo, pos, node_size=20, edge_color="gray", alpha=0.6)
    nx.draw_networkx_nodes(grafo, pos, nodelist=[inicio], node_color='green', label="Início", node_size=100)
    nx.draw_networkx_nodes(grafo, pos, nodelist=[fim], node_color='red', label="Fim", node_size=100)
    plt.title(titulo)
    plt.legend()
    plt.show()

def busca_largura(grafo: nx.Graph, inicio: int, fim: int):
    """
    Implementa a busca em largura (BFS) sem utilizar funções prontas.

    Args:
        grafo (nx.Graph): O grafo onde será feita a busca.
        inicio (int): Nó inicial.
        fim (int): Nó final.

    Returns:
        list: Caminho encontrado ou vazio se não houver caminho.
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

def escolher_grafo() -> Tuple[str, nx.Graph]:
    """
    Permite ao usuário escolher um grafo a partir das opções disponíveis.

    Returns:
        tuple: Nome do grafo escolhido e o grafo gerado.
    """
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

# Escolher o grafo
grafo_escolhido, grafo = escolher_grafo()
if grafo:
    print(f"{grafo_escolhido} gerado com sucesso!")
    
    # Definir nós de início e fim
    num_vertices = len(grafo.nodes)
    while True:
        try:
            inicio = int(input(f"Digite o nó de início (0 a {num_vertices - 1}): "))
            fim = int(input(f"Digite o nó de fim (0 a {num_vertices - 1}): "))
            if 0 <= inicio < num_vertices and 0 <= fim < num_vertices:
                break
            else:
                print("Os valores devem estar dentro do intervalo válido!")
        except ValueError:
            print("Entrada inválida! Digite números inteiros.")

    # Executar a busca em largura e medir tempo
    inicio_tempo = time.time()
    caminho = busca_largura(grafo, inicio, fim)
    fim_tempo = time.time()

    # Exibir resultados
    if caminho:
        print("Caminho encontrado:", caminho)
        print(f"Tamanho do caminho: {len(caminho)}")
    else:
        print("Nenhum caminho encontrado.")

    print(f"Tempo de execução: {fim_tempo - inicio_tempo:.6f} segundos")

    # Visualizar grafo
    visualizar_grafo(grafo, grafo_escolhido, inicio, fim)
