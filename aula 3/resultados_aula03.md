LAB1_AULA3
ALGORITMO GENÉTICO PASSO A PASSO
==================================================

População inicial: [[1, 1, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 1, 1, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 0], [1, 0, 0, 1, 1]]

==================== GERAÇÃO 0 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 1, 1, 0] → x=30 → f(x)=900
  [1, 0, 1, 1, 0] → x=22 → f(x)=484
  [1, 0, 1, 1, 1] → x=23 → f(x)=529
  [1, 1, 1, 1, 0] → x=30 → f(x)=900
  [1, 0, 0, 1, 1] → x=19 → f(x)=361

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 1 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 0, 1, 1, 0] → x=22 → f(x)=484
  [1, 0, 1, 1, 0] → x=22 → f(x)=484
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 0, 1, 1, 1] → x=23 → f(x)=529

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 2 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 0, 0, 1, 1] → x=19 → f(x)=361
  [1, 1, 0, 0, 0] → x=24 → f(x)=576
  [1, 1, 1, 0, 0] → x=28 → f(x)=784
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [0, 0, 1, 1, 1] → x= 7 → f(x)= 49

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 3 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 1, 0, 0] → x=28 → f(x)=784
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 0, 0, 1, 1] → x=19 → f(x)=361
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [0, 0, 1, 1, 1] → x= 7 → f(x)= 49

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 4 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [0, 1, 1, 1, 0] → x=14 → f(x)=196
  [1, 1, 1, 0, 0] → x=28 → f(x)=784
  [1, 0, 1, 0, 0] → x=20 → f(x)=400
  [1, 1, 1, 0, 1] → x=29 → f(x)=841
  [1, 1, 0, 1, 1] → x=27 → f(x)=729

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 5 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 1, 0, 0] → x=28 → f(x)=784
  [1, 1, 1, 0, 0] → x=28 → f(x)=784
  [1, 1, 0, 1, 0] → x=26 → f(x)=676
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [0, 1, 1, 0, 0] → x=12 → f(x)=144

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 6 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 0, 1, 1, 1] → x=23 → f(x)=529
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 1, 0, 1] → x=29 → f(x)=841
  [1, 1, 1, 1, 1] → x=31 → f(x)=961

 Melhor: x = 31 → f(x) = 961

==================== GERAÇÃO 7 ====================

Avaliação dos indivíduos:
  [1, 1, 1, 1, 1] → x=31 → f(x)=961
  [0, 1, 1, 1, 1] → x=15 → f(x)=225
  [1, 1, 0, 1, 1] → x=27 → f(x)=729
  [1, 1, 1, 0, 1] → x=29 → f(x)=841
  [0, 1, 1, 0, 1] → x=13 → f(x)=169
  [1, 1, 1, 1, 0] → x=30 → f(x)=900

 Melhor: x = 31 → f(x) = 961

==================================================
RESULTADO FINAL
==================================================

Melhor indivíduo: [1, 1, 1, 1, 1]
x = 31
f(x) = 961

Ótimo global: x = 31, f(x) = 961
Erro: 0
------------------------------------------
LAB2_AULA3
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

   

------------------------------------------
LAB3_AULA_3
==================================================
OTIMIZANDO f(x) = x * sin(3x)
==================================================
Geração   0: Melhor f(x) = 6.6088 (x = 8.6667)
Geração  10: Melhor f(x) = 8.8769 (x = 8.9412)
Geração  20: Melhor f(x) = 8.8769 (x = 8.9412)
Geração  30: Melhor f(x) = 8.8769 (x = 8.9412)
Geração  40: Melhor f(x) = 8.8769 (x = 8.9412)


 MELHOR SOLUÇÃO: x = 8.9412, f(x) = 8.8769

 Parâmetros do Algoritmo Genético:

BITS (8 bits): Define a precisão do mapeamento de x. Mais bits aumentariam a precisão, mas também o espaço de busca.
POP_SIZE (20): O tamanho da população. Uma população maior pode explorar mais o espaço de busca, mas exige mais tempo de computação por geração.
GERACOES (50): O número de gerações. O gráfico de convergência mostra que o algoritmo estabilizou rapidamente. Poderíamos considerar aumentar as gerações se a função fosse mais complexa ou o problema exigisse mais convergência, ou reduzir se a convergência for sempre rápida para otimizar o tempo.
TAXA_CROSS (0.8): A taxa de crossover. Uma taxa alta incentiva a mistura de soluções, o que é bom para explorar novas combinações.
TAXA_MUT (0.05): A taxa de mutação. Uma taxa baixa é geralmente boa para manter os indivíduos existentes, enquanto uma taxa mais alta pode introduzir mais diversidade e ajudar a sair de ótimos locais, mas pode desestabilizar a convergência.
Mapeamento de Bits para X (bits_para_x): A função de mapeamento de 8 bits para o intervalo [0, 10] funcionou corretamente. É importante garantir que este mapeamento cubra o intervalo desejado de forma granular.

Função de Fitness (fitness): Como estamos maximizando f(x), a função de fitness foi definida diretamente como f(x), o que é apropriado para este problema.

Convergência: O algoritmo mostrou uma boa convergência, encontrando um valor x que maximiza f(x) dentro de poucas gerações. O gráfico de convergência confirma essa estabilidade.

Otimização Local vs. Global: Para funções mais complexas com múltiplos picos, é importante considerar se o algoritmo genético está encontrando um ótimo global ou ficando preso em um ótimo local. Para esta função específica, o ponto encontrado parece ser o máximo global no intervalo.

Aleatoriedade: Devido à natureza estocástica dos algoritmos genéticos, múltiplas execuções podem levar a resultados ligeiramente diferentes. Poderíamos executar o algoritmo várias vezes e analisar a média e o desvio padrão dos resultados para avaliar sua robustez.
