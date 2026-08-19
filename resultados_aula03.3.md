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

