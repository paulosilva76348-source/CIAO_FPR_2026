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


"""
LAB 01 - PSO Contínuo para Balanceamento Dinâmico de Carga em Datacenters

Objetivo:
Encontrar pesos W=[w1,...,w6], sum(W)=1, que minimizem a temperatura
média ponderada, considerando penalidade quando alguma temperatura
individual ultrapassar 75 °C.
"""

import random
import math
import statistics


COEF_AQUECIMENTO = [42.0, 35.0, 58.0, 30.0, 50.0, 65.0]
LIMITE_CRITICO = 75.0


def normalizar_posicao(posicao):
    """Normaliza os pesos para garantir exatamente sum(wi) = 1."""
    posicao = [max(0.0, x) for x in posicao]
    soma = sum(posicao)

    if soma == 0:
        return [1.0 / len(posicao)] * len(posicao)

    pesos = [x / soma for x in posicao]

    # Correção numérica para garantir soma exatamente 1.
    pesos[-1] += 1.0 - sum(pesos)

    return pesos


def avaliar(posicao):
    """
    Fitness a ser minimizado.

    A temperatura de cada AZ é calculada proporcionalmente ao peso
    direcionado à AZ. A penalidade externa é aplicada quando uma
    temperatura individual ultrapassa 75 °C.
    """
    pesos = normalizar_posicao(posicao)

    temperaturas = [
        coef * peso
        for coef, peso in zip(COEF_AQUECIMENTO, pesos)
    ]

    temperatura_media = sum(temperaturas) / len(temperaturas)

    excesso = sum(
        max(0.0, temperatura - LIMITE_CRITICO)
        for temperatura in temperaturas
    )

    penalidade = 1000.0 * excesso

    fitness = temperatura_media + penalidade

    return fitness, temperaturas, pesos


class Particula:
    def __init__(self, dimensao):
        self.posicao = [random.uniform(0.0, 1.0) for _ in range(dimensao)]
        self.posicao = normalizar_posicao(self.posicao)

        self.velocidade = [
            random.uniform(-0.1, 0.1)
            for _ in range(dimensao)
        ]

        self.p_best = self.posicao.copy()
        self.p_best_fitness = avaliar(self.posicao)[0]


class PSOContinuo:
    def __init__(
        self,
        numero_particulas,
        dimensao=6,
        iteracoes=100,
        w=0.7,
        c1=1.5,
        c2=1.5,
        seed=42
    ):
        random.seed(seed)

        self.numero_particulas = numero_particulas
        self.dimensao = dimensao
        self.iteracoes = iteracoes
        self.w = w
        self.c1 = c1
        self.c2 = c2

        self.particulas = [
            Particula(dimensao)
            for _ in range(numero_particulas)
        ]

        melhor = min(
            self.particulas,
            key=lambda p: p.p_best_fitness
        )

        self.g_best = melhor.p_best.copy()
        self.g_best_fitness = melhor.p_best_fitness

        self.historico_g_best = []
        self.historico_p_best = []

    def executar(self):
        for _ in range(self.iteracoes):

            for particula in self.particulas:

                for i in range(self.dimensao):
                    r1 = random.random()
                    r2 = random.random()

                    componente_cognitivo = (
                        self.c1
                        * r1
                        * (particula.p_best[i] - particula.posicao[i])
                    )

                    componente_social = (
                        self.c2
                        * r2
                        * (self.g_best[i] - particula.posicao[i])
                    )

                    particula.velocidade[i] = (
                        self.w * particula.velocidade[i]
                        + componente_cognitivo
                        + componente_social
                    )

                    particula.posicao[i] += particula.velocidade[i]

                # Operador obrigatório de normalização.
                particula.posicao = normalizar_posicao(
                    particula.posicao
                )

                fitness, _, _ = avaliar(particula.posicao)

                if fitness < particula.p_best_fitness:
                    particula.p_best = particula.posicao.copy()
                    particula.p_best_fitness = fitness

                    if fitness < self.g_best_fitness:
                        self.g_best = particula.posicao.copy()
                        self.g_best_fitness = fitness

            self.historico_g_best.append(self.g_best_fitness)
            self.historico_p_best.append(
                min(p.p_best_fitness for p in self.particulas)
            )

        return self.g_best, self.g_best_fitness


def executar_experimento():
    resultados = []

    for tamanho in [10, 30, 50]:
        pso = PSOContinuo(
            numero_particulas=tamanho,
            iteracoes=100,
            seed=42 + tamanho
        )

        melhor_w, fitness = pso.executar()
        fitness, temperaturas, melhor_w = avaliar(melhor_w)

        resultados.append({
            "populacao": tamanho,
            "pesos": melhor_w,
            "soma": sum(melhor_w),
            "fitness": fitness,
            "temperaturas": temperaturas,
            "historico": pso.historico_g_best
        })

    return resultados


def imprimir_resultados(resultados):
    print("\n=== LAB 01 - RESULTADOS ===")

    for resultado in resultados:
        print(f"\nPopulação: {resultado['populacao']}")
        print(
            "W = ["
            + ", ".join(f"{x:.6f}" for x in resultado["pesos"])
            + "]"
        )
        print(f"Soma(W) = {resultado['soma']:.12f}")
        print(f"Fitness = {resultado['fitness']:.6f}")

        print("Temperaturas:")
        print(
            "["
            + ", ".join(
                f"{x:.6f}" for x in resultado["temperaturas"]
            )
            + "]"
        )


if __name__ == "__main__":
    resultados = executar_experimento()
    imprimir_resultados(resultados)
