### 6.1. Implicações para o Estudante (Mapa da Romênia)

1. **Por que o BFS é geralmente melhor para o Mapa da Romênia?**

   - **Otimidade:** A Busca em Largura (BFS) garante encontrar o caminho com o menor número de paradas, pois explora o grafo nível por nível utilizando uma estrutura de dados FIFO (fila).  
   - Como o mapa da Romênia é um grafo **não ponderado**, o primeiro caminho encontrado pelo BFS (por exemplo: Arad → Sibiu → Fagaras → Bucareste) é o caminho ótimo.
   - Além disso, como a profundidade da solução mais rasa (**d**) é pequena (cerca de 3 ou 4 passos), o custo computacional **O(b^d)** é aceitável.

2. **Qual o problema do DFS (LIFO) neste caso?**

   - **Uso de Memória:** A Busca em Profundidade (DFS) utiliza menos memória que o BFS, pois sua complexidade de espaço é **O(b · m)**, armazenando apenas o caminho atual. Essa é uma de suas vantagens.
   - **Risco de Sub-otimalidade:** No entanto, o DFS não garante encontrar o caminho mais curto, pois explora profundamente um ramo antes de considerar alternativas. Assim, ele pode retornar um caminho mais longo (exemplo: Arad → Timisoara → Lugoj → ...).
   - Além disso, sem o uso do conjunto `explorados`, o DFS pode entrar em ciclos e não ser completo.

**Conclusão para o Projeto:**  
Para encontrar a rota com **menos paradas** no mapa da Romênia, a estratégia baseada em **FIFO (Busca em Largura – BFS)** é a mais adequada. Já a estratégia **LIFO (Busca em Profundidade – DFS)** pode ser útil em cenários com limitação de memória e quando a profundidade da solução não é excessiva, embora não garanta otimalidade.