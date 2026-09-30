Cenário:
Conectar 10 switches de rede em uma topologia em árvore geradora que minimize a latência total acumulada entre os pares mais críticos, respeitando a matriz de latências físicas de cabeamento D (10x10).

Requisitos do Código:
- Implementar do zero o algoritmo de Colônia de Formigas (ACO) adaptado para seleção de arestas em grafos.
- Incluir verificação de ciclos/conectividade ao longo da construção da rota das formigas para garantir que a solução final forme um grafo/árvore válido.
- Atualização da matriz de feromônio tau_ij com taxa de evaporação rho = 0.2 aplicada apenas às melhores topologias da iteração.

Artefatos e Testes:
- Imprimir a Matriz de Adjacência final (10x10) do grafo de rede otimizado pelo ACO.
- Apresentar o ganho percentual de redução de latência obtido pelo ACO em relação a uma topologia gerada de forma aleatória.
