Cenário:
Redirecionamento dinâmico de tráfego web entre 6 zonas de disponibilidade (AZs).
O sistema deve encontrar o vetor de pesos contínuos W = [w1, w2, w3, w4, w5, w6] (com sum(wi) = 1.0) para minimizar a temperatura média ponderada dos racks, 
sabendo que cada AZ possui um coeficiente de aquecimento específico C = [42.0, 35.0, 58.0, 30.0, 50.0, 65.0] °C.

Requisitos do Código:
- Implementar do zero a classe/estrutura do PSO Contínuo (com atualização de velocidade, posição e histórico de P_best e G_best).
- Aplicar um operador de normalização no vetor de posições das partículas a cada iteração, garantindo obrigatoriamente sum(wi) = 1.0.
- Implementar função de penalidade externa caso a temperatura de alguma AZ ultrapasse o limite crítico de 75 °C.

Artefatos e Testes
- Executar e comparar a evolução do fitness para 3 tamanhos de população de partículas: 10, 30 e 50 partículas.
- Registrar a tabela com a melhor distribuição W encontrada para cada população e a validação da soma (sum(wi) = 1.0).
