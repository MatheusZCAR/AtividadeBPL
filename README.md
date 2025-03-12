# Algoritmos de Busca Não-Informada em Grafos

## 📖 Descrição
Este projeto contém a implementação em Python dos algoritmos clássicos de busca não-informada aplicados em grafos:

- **Busca em Largura (BFS)**
- **Busca em Profundidade (DFS)**
- **Busca em Profundidade Limitada (DLS)**

O projeto permite gerar grafos determinísticos com diferentes quantidades de vértices e arestas adicionais, facilitando testes consistentes dos algoritmos.

---

## 👨‍💻 Autores

- Felipe Yabiko Nogueira - RA: 22002265  
- Henrique Ladeira Alves - RA: 23016926  
- João Victor Rokemback Tapparo - RA: 22003236  
- Matheus Zanon Caritá - RA: 22014203  
- Mayron Germann Sousa de Pádua - RA: 21003182  

---

## 🚀 Bibliotecas utilizadas
- **Python 3**
- **NetworkX**
- **Matplotlib**
- **SciPy** *(necessário para visualização gráfica eficiente)*

---

## 📝 Observações importantes

- Grafos Grandes: Grafos com muitos vértices, especialmente grafos completos (**Kn com 10.000 vértices**), podem demandar um tempo significativo para geração e visualização. Por exemplo, em um processador Apple Silicon M2, a geração e visualização de um grafo completo com 10.000 vértices levaram aproximadamente **7 minutos e 20 segundos**.
- Visualização Animada: A visualização gráfica do caminho encontrado é feita por meio de uma animação, que pode demorar dependendo do tamanho do grafo. Recomenda-se não interromper a execução e aguardar a conclusão do processo para garantir a integridade dos resultados.
