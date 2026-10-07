=====Lab1=====

Collecting scikit-fuzzy
  Downloading scikit_fuzzy-0.5.0-py2.py3-none-any.whl.metadata (2.6 kB)
Downloading scikit_fuzzy-0.5.0-py2.py3-none-any.whl (920 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 920.8/920.8 kB 11.0 MB/s eta 0:00:00
Installing collected packages: scikit-fuzzy
Successfully installed scikit-fuzzy-0.5.0
10°C -> ventilador a 17%
20°C -> ventilador a 44%
25°C -> ventilador a 50%
30°C -> ventilador a 56%
38°C -> ventilador a 83%

<img width="613" height="424" alt="image" src="https://github.com/user-attachments/assets/8578a6b7-0b52-46ff-a16a-956fe78aa44a" />
<img width="606" height="450" alt="image" src="https://github.com/user-attachments/assets/af188b83-2cba-4667-bbbb-bde610d5e2cf" />

=====Lab2=====

Nota do serviço (0-10) [7]: 4
Nota da comida (0-10) [3]: 6

=> Gorjeta sugerida: 12.6%

<img width="320" height="422" alt="image" src="https://github.com/user-attachments/assets/60c6b496-ddd4-482c-bac4-6d2c8da8d620" />
<img width="323" height="227" alt="image" src="https://github.com/user-attachments/assets/60804115-bda0-4e3f-abf7-ffc84c679806" />

==Lab3==

Etapa 1 & 2: Definição do Problema e Modelagem Matemática
Definição do Problema (Etapa 1)
O problema abordado é o ajuste dinâmico do Tempo de Semáforo Verde para carros em um cruzamento urbano. Tradicionalmente, os semáforos usam tempos fixos ou sensores simples do tipo "se há carro, abre". A lógica fuzzy é altamente adequada aqui porque o tráfego de pedestres e o acúmulo de carros variam de forma contínua e imprecisa. O sistema decide o tempo de abertura equilibrando a fluidez do tráfego veicular com a segurança e o tempo de espera dos pedestres, evitando decisões binárias rígidas e otimizando o fluxo geral da via.

Modelagem Matemática (Etapa 2)
Entrada 1: Tamanho da Fila (carros)
Universo:  [0,30] 
Termos linguísticos: pequena (trapézio), media (triângulo), grande (trapézio)
Entrada 2: Fluxo de Pedestres (pedestres)
Universo:  [0,50] 
Termos linguísticos: baixo (trapézio), moderado (triângulo), alto (trapézio)
Saída: Tempo de Verde (segundos)
Universo:  [10,60] 
Termos linguísticos: curto (triângulo), intermediario (triângulo), longo (triângulo)
Base de Regras (Mínimo de 6 regras, usando E e OU):
SE fila é grande E pedestres é baixo ENTÃO tempo é longo.
SE fila é pequena E pedestres é alto ENTÃO tempo é curto.
SE fila é media E pedestres é moderado ENTÃO tempo é intermediario.
SE fila é grande OU pedestres é baixo ENTÃO tempo é longo.
SE fila é pequena E pedestres é baixo ENTÃO tempo é curto.
SE fila é media OU pedestres é alto ENTÃO tempo é intermediario.


# Etapa 3: Implementação em Python do Sistema Fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 1. Definição das variáveis do universo de discurso
fila = ctrl.Antecedent(np.arange(0, 31, 1), 'fila')
pedestres = ctrl.Antecedent(np.arange(0, 51, 1), 'pedestres')
tempo_verde = ctrl.Consequent(np.arange(10, 61, 1), 'tempo_verde')

# 2. Definição das funções de pertinência
fila['pequena'] = fuzz.trapmf(fila.universe, [0, 0, 5, 12])
fila['media'] = fuzz.trimf(fila.universe, [8, 15, 22])
fila['grande'] = fuzz.trapmf(fila.universe, [18, 25, 30, 30])

pedestres['baixo'] = fuzz.trapmf(pedestres.universe, [0, 0, 10, 20])
pedestres['moderado'] = fuzz.trimf(pedestres.universe, [15, 25, 35])
pedestres['alto'] = fuzz.trapmf(pedestres.universe, [30, 40, 50, 50])

tempo_verde['curto'] = fuzz.trimf(tempo_verde.universe, [10, 10, 30])
tempo_verde['intermediario'] = fuzz.trimf(tempo_verde.universe, [20, 35, 50])
tempo_verde['longo'] = fuzz.trimf(tempo_verde.universe, [40, 60, 60])

# Visualizando as funções de pertinência
fila.view()
pedestres.view()
tempo_verde.view()
plt.show()

<img width="499" height="701" alt="image" src="https://github.com/user-attachments/assets/e4695050-4374-4994-aa6e-c30261151ee4" />
<img width="527" height="364" alt="image" src="https://github.com/user-attachments/assets/8789c2e4-3377-48d2-a418-5ae1c94b8ed5" />


# Criando e configurando o sistema com as 6 regras definidas
regra1 = ctrl.Rule(fila['grande'] & pedestres['baixo'], tempo_verde['longo'])
regra2 = ctrl.Rule(fila['pequena'] & pedestres['alto'], tempo_verde['curto'])
regra3 = ctrl.Rule(fila['media'] & pedestres['moderado'], tempo_verde['intermediario'])
regra4 = ctrl.Rule(fila['grande'] | pedestres['baixo'], tempo_verde['longo'])
regra5 = ctrl.Rule(fila['pequena'] & pedestres['baixo'], tempo_verde['curto'])
regra6 = ctrl.Rule(fila['media'] | pedestres['alto'], tempo_verde['intermediario'])

semaforo_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6])
semaforo_simulador = ctrl.ControlSystemSimulation(semaforo_ctrl)

# Etapa 4 & 5: Testes do sistema em cenários reais e gravação do relatório markdown

cenarios = [
    {"fila": 3, "pedestres": 45, "descricao": "Fila de carros pequena e muitos pedestres esperando (Esperado: tempo de verde CURTO para carros)"},
    {"fila": 28, "pedestres": 5, "descricao": "Fila imensa de carros e pouquíssimos pedestres (Esperado: tempo de verde LONGO para carros)"},
    {"fila": 15, "pedestres": 25, "descricao": "Situação de tráfego moderado para ambos (Esperado: tempo de verde INTERMEDIÁRIO)"},
    {"fila": 2, "pedestres": 2, "descricao": "Madrugada: quase sem tráfego de carros e de pedestres (Esperado: tempo de verde CURTO)"}
]

resultados_txt = []

print("--- Executando testes de simulação ---")
for i, cenario in enumerate(cenarios, 1):
    semaforo_simulador.input['fila'] = cenario['fila']
    semaforo_simulador.input['pedestres'] = cenario['pedestres']
    semaforo_simulador.compute()
    tempo_final = semaforo_simulador.output['tempo_verde']
    
    resultado_linha = f"**Cenário {i}**: {cenario['descricao']}\n" \
                      f"* Entradas: Fila = {cenario['fila']} carros, Pedestres = {cenario['pedestres']} pessoas\n" \
                      f"* Saída Fuzzy: Tempo de sinal verde calculado em **{tempo_final:.2f} segundos**\n"
    print(f"Cenário {i} -> Tempo de Verde calculado: {tempo_final:.2f}s")
    resultados_txt.append(resultado_linha)

# Gerando o arquivo resultados_aula09.md solicitado
conteudo_md = f"""# Relatório de Resultados - Aula 09: Sistema de Controle Fuzzy para Semáforos

## 1. Descrição do Problema
O sistema foi projetado para controlar dinamicamente o tempo de abertura verde para automóveis com base na fila de carros pendente e na quantidade de pedestres desejando atravessar a via.

## 2. Modelagem das Variáveis
* **Fila de carros**: Escala de 0 a 30 (Termos: pequena, media, grande)
* **Fluxo de Pedestres**: Escala de 0 a 50 (Termos: baixo, moderado, alto)
* **Tempo do Sinal Verde**: Escala de 10 a 60 segundos (Termos: curto, intermediario, longo)

## 3. Resultados das Simulações
\n""".join(resultados_txt)

with open("resultados_aula09.md", "w", encoding="utf-8") as f:
    f.write(conteudo_md)

print("\nArquivo 'resultados_aula09.md' gerado e gravado com sucesso!")

--- Executando testes de simulação ---
Cenário 1 -> Tempo de Verde calculado: 27.84s
Cenário 2 -> Tempo de Verde calculado: 53.33s
Cenário 3 -> Tempo de Verde calculado: 35.00s
Cenário 4 -> Tempo de Verde calculado: 35.00s

Arquivo 'resultados_aula09.md' gerado e gravado com sucesso!


