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

Tabela que as duplas/trio devem preencher # Numero de cidades | Rotas avaliadas | Tempo (s) | Melhor custo # 4 | | | # 5 | | | # 6 | | | # Perguntas de reflexao (obrigatorias) 
# 16. O numero de rotas cresce de forma linear, quadratica ou muito mais rapido? Explique com as quantidades que voce coletou. 
# 17. Com base no padrao observado, estime (mesmo que de forma grosseira) quanto tempo levaria para 10 cidades no mesmo computador. 
#18. Por que dizemos que o TSP e um problema “dificil”? A resposta nao e “porque e complicado de entender”, e sim por causa do crescimento do tempo.
A complexidade do TSP (Caixeiro Viajante) é fatorial, ou seja, cresce muito mais rápido que linear ou quadrática. Para 10 cidades, levaria um tempo impraticável devido ao número gigantesco de rotas (3.628.800). É um problema difícil justamente por esse crescimento exponencial do tempo de processamento com o aumento do número de cidades, e não pela dificuldade de compreensão.
=================================================================

# LAB_3_AULA2







