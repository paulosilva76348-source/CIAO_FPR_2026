==================================================
ONEMAX - AG com 30 indivíduos, 50 gerações
==================================================
Geração   0: Melhor = 12/20, Média = 9.37
Geração  10: Melhor = 19/20, Média = 18.53
Geração  20: Melhor = 20/20, Média = 19.60
Geração  30: Melhor = 20/20, Média = 19.43
Geração  40: Melhor = 20/20, Média = 19.57

 MELHOR FITNESS: 20/20
   Ótimo = 20 (todos os bits são 1)


DESAFIO: Mude os parâmetros e veja o que acontece!
==================================================
1. Aumente a TAXA_MUT para 0.1. O que acontece?
    Aumentar TAXA_MUT para 0.1:Aumenta bastante a quantidade de mutações. Isso aumenta a diversidade da população, mas também pode atrapalhar a convergência,
    pois muitos bits que já são 1 podem virar 0. O algoritmo pode demorar mais para chegar ao ótimo.

2. Diminua POPULACAO para 10. O que acontece?
     Diminuir POPULACAO para 10:A população fica menor e há menos diversidade genética. O AG pode convergir mais rapidamente em alguns casos,
     mas aumenta a chance de ficar preso em soluções não tão boas. O resultado também pode variar mais entre execuções.

3. Aumente GERACOES para 100. O que acontece?
     Aumentar GERACOES para 100:O algoritmo terá mais oportunidades para melhorar as soluções. Em geral, o melhor fitness tende a chegar mais próximo de 20/20, aumentando a chance de encontrar a solução ótima.

4. Mude ELITE para 0. O que acontece?Mudar ELITE para 0:
    Nenhum dos melhores indivíduos é preservado diretamente para a próxima geração. Assim, uma solução boa pode ser perdida por crossover ou mutação.
    Isso pode deixar o algoritmo menos estável e dificultar a manutenção do melhor resultado encontrado.

   
