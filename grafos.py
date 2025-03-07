import networkx as nx

# Função para gerar um grafo com o número específico de vértices e arestas.
def gerar_grafo(numVertices, numArestas):

    numTotalArestas = numVertices * numArestas // 2  # Fórmula para garantir conectividade
    grafo = nx.gnm_random_graph(numVertices, numTotalArestas)
    return grafo

# Definições dos parâmetros
vertices = [500, 5000, 10000]
arestas = [3, 5, 7]

def escolher_grafo():
    opcoes = [(i, v, k, f"Grafo com {v} vértices e {k} arestas") for i, (v, k) in enumerate([(v, k) for v in vertices for k in arestas], start=1)]
    
    while True:
        print("Escolha um dos grafos para gerar:")
        for i, v, k, chave in opcoes:
            print(f"{i}: {chave}")
        
        try:
            escolha = int(input("Digite o número do grafo desejado: ")) - 1
            if 0 <= escolha < len(opcoes):
                _, v, k, chave = opcoes[escolha]
                return chave, gerar_grafo(v, k)
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número correspondente à opção desejada.")

# Executa a escolha do usuário
grafo_escolhido, grafo = escolher_grafo()
if grafo:
    print(f"Grafo {grafo_escolhido} gerado com sucesso!")
