# LAB_1_AULA2

Total de solucoes avaliadas: 32
Tempo de execucao: 0.000147 segundos
Melhor valor encontrado: 9
Combinacao otima (0=nao leva, 1=leva): (1, 1, 0, 1, 1)

Itens escolhidos:
 - Livro (peso: 2 , valor: 3 )
 - Fone (peso: 1 , valor: 2 )
 - Carregador (peso: 1 , valor: 3 )
 - Chocolate (peso: 1 , valor: 1 )


1 - 32 soluções avaliadas: Porque com 5 itens, existem 2^5 = 32 combinações possíveis no problema da mochila.
2 - Com 15 itens: O número de soluções seria 2^15 = 32.768, tornando o algoritmo de força bruta muito lento (exponencial).
3 - Problemas da vida real: Este é o clássico Problema da Mochila, aplicável em situações como carregamento de cargas, seleção de investimentos, alocação de recursos e corte de materiais,
    onde há um limite de capacidade e o objetivo é maximizar o valor.

# LAB_2_AULA2

=================================================================
RESULTADOS DA FORCA-BRUTA NO TSP
=================================================================

>>> 4 cidades
    Rotas avaliadas : 6
    Melhor custo    : 80
    Melhor rota     : (0, 1, 3, 2, 0)
    Tempo (segundos): 0.000135

>>> 5 cidades
    Rotas avaliadas : 24
    Melhor custo    : 41
    Melhor rota     : (0, 1, 2, 3, 4, 0)
    Tempo (segundos): 0.000073

>>> 6 cidades
    Rotas avaliadas : 120
    Melhor custo    : 91
    Melhor rota     : (0, 1, 3, 4, 5, 2, 0)
    Tempo (segundos): 0.000343

=================================================================
OBSERVE: o numero de rotas cresce como (n-1)!  (fatorial)
4 cidades -> 6 rotas | 5 -> 24 | 6 -> 120 | 10 -> 362880 | 15 -> 87 bilhoes

Tabela que as duplas/trio devem preencher # Numero de cidades | Rotas avaliadas | Tempo (s) | Melhor custo  4 | | |  5 | | |  6 | | | # Perguntas de reflexao (obrigatorias) 
 16. O numero de rotas cresce de forma linear, quadratica ou muito mais rapido? Explique com as quantidades que voce coletou. 
 17. Com base no padrao observado, estime (mesmo que de forma grosseira) quanto tempo levaria para 10 cidades no mesmo computador. 
 18. Por que dizemos que o TSP e um problema “dificil”? A resposta nao e “porque e complicado de entender”, e sim por causa do crescimento do tempo.
A complexidade do TSP (Caixeiro Viajante) é fatorial, ou seja, cresce muito mais rápido que linear ou quadrática. Para 10 cidades, levaria um tempo impraticável devido ao número gigantesco de rotas (3.628.800). É um problema difícil justamente por esse crescimento exponencial do tempo de processamento com o aumento do número de cidades, e não pela dificuldade de compreensão.
=================================================================

# LAB_3_AULA2

Rodando 20 instancias...
Instancia  1 | Otimo:  199 | Gulosa:  199 | Gap:   0.0%
Instancia  2 | Otimo:  170 | Gulosa:  170 | Gap:   0.0%
Instancia  3 | Otimo:  155 | Gulosa:  155 | Gap:   0.0%
Instancia  4 | Otimo:  147 | Gulosa:  147 | Gap:   0.0%
Instancia  5 | Otimo:  261 | Gulosa:  261 | Gap:   0.0%
Instancia  6 | Otimo:  214 | Gulosa:  214 | Gap:   0.0%
Instancia  7 | Otimo:  191 | Gulosa:  187 | Gap:   2.1%
Instancia  8 | Otimo:  183 | Gulosa:  183 | Gap:   0.0%
Instancia  9 | Otimo:  215 | Gulosa:  206 | Gap:   4.2%
Instancia 10 | Otimo:  174 | Gulosa:  174 | Gap:   0.0%
Instancia 11 | Otimo:  262 | Gulosa:  262 | Gap:   0.0%
Instancia 12 | Otimo:  206 | Gulosa:  206 | Gap:   0.0%
Instancia 13 | Otimo:  231 | Gulosa:  231 | Gap:   0.0%
Instancia 14 | Otimo:  309 | Gulosa:  309 | Gap:   0.0%
Instancia 15 | Otimo:  294 | Gulosa:  294 | Gap:   0.0%
Instancia 16 | Otimo:  247 | Gulosa:  247 | Gap:   0.0%
Instancia 17 | Otimo:  136 | Gulosa:  134 | Gap:   1.5%
Instancia 18 | Otimo:  212 | Gulosa:  212 | Gap:   0.0%
Instancia 19 | Otimo:  243 | Gulosa:  243 | Gap:   0.0%
Instancia 20 | Otimo:  193 | Gulosa:  193 | Gap:   0.0%

===== RESUMO =====
Gap medio     : 0.39%
Gap minimo    : 0.00%
Gap maximo    : 4.19%
Desvio padrao : 1.03%

19. Código completo (com a função calcular_gap implementada e o loop funcionando). O código já está completo, com a função calcular_gap implementada para calcular o gap percentual e o loop do experimento rodando e adicionando os gaps à lista gaps.

20. Valor do gap médio obtido. O gap médio obtido no experimento foi de 0.39%.

21.Resposta: “A heurística gulosa é boa o suficiente para este problema? Em quais situações você usaria ela e em quais preferiria gastar mais tempo para achar o ótimo?” A heurística gulosa mostrou-se muito eficiente para este problema, com um baixo gap médio. Ela é ideal para problemas grandes ou com restrições de tempo, onde um pequeno desvio do ótimo é aceitável, pois é significativamente mais rápida. Contudo, em problemas pequenos ou quando o custo de um erro mínimo é muito alto (ex: alto impacto financeiro, projetos críticos), vale a pena investir mais tempo para encontrar a solução ótima, usando métodos exatos.

# LAB_4_AULA2











