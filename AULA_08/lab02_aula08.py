Cenário:
Um nó de Edge Computing precisa selecionar um subconjunto de 15 microsserviços disponíveis para manter em memória.
Cada serviço possui um Valor de Negócio, um Consumo de RAM (GB) e um Consumo de CPU (Cores).
O objetivo é maximizar o Valor de Negócio acumulado respeitando as restrições simultâneas de capacidade: máximo de 16 GB de RAM e máximo de 8 cores de CPU.

Requisitos do Código:
- Implementar do zero um Algoritmo Genético Binário (1 = serviço carregado, 0 = não carregado).
- Criar e comparar duas estratégias de avaliação de fitness:
  1. Estratégia A (Penalidade Rígida): Indivíduos que violarem qualquer limite (RAM ou CPU) recebem fitness = 0.
  2. Estratégia B (Penalidade Proporcional): O fitness é reduzido proporcionalmente à quantidade de RAM/CPU excedida.
- Operadores de Seleção por Torneio, Crossover de Ponto Único e Mutação Binária.

Artefatos e Testes:
- Comparar a média e o desvio-padrão do fitness ao longo das gerações entre a Estratégia A e a Estratégia B.
- Demonstrar no relatório qual das duas estratégias preservou melhor a diversidade genética da população e qual encontrou a melhor combinação final de microsserviços.

