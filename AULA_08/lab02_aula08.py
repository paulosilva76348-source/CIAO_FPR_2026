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

"""
LAB 02 - Algoritmo Genético Binário para seleção de microsserviços.

Estratégias:
A) Penalidade rígida:
   qualquer violação => fitness = 0

B) Penalidade proporcional:
   reduz o valor proporcionalmente aos excessos de RAM e CPU.
"""

import random
import statistics


SERVICOS = [
    {"nome": "MS01", "valor": 40, "ram": 2.0, "cpu": 1.0},
    {"nome": "MS02", "valor": 35, "ram": 1.5, "cpu": 0.8},
    {"nome": "MS03", "valor": 55, "ram": 3.0, "cpu": 1.5},
    {"nome": "MS04", "valor": 30, "ram": 1.0, "cpu": 0.5},
    {"nome": "MS05", "valor": 70, "ram": 4.0, "cpu": 2.0},
    {"nome": "MS06", "valor": 45, "ram": 2.5, "cpu": 1.0},
    {"nome": "MS07", "valor": 60, "ram": 3.0, "cpu": 1.2},
    {"nome": "MS08", "valor": 25, "ram": 1.0, "cpu": 0.4},
    {"nome": "MS09", "valor": 50, "ram": 2.0, "cpu": 1.5},
    {"nome": "MS10", "valor": 65, "ram": 3.5, "cpu": 1.8},
    {"nome": "MS11", "valor": 38, "ram": 1.5, "cpu": 0.7},
    {"nome": "MS12", "valor": 48, "ram": 2.0, "cpu": 1.0},
    {"nome": "MS13", "valor": 58, "ram": 3.0, "cpu": 1.3},
    {"nome": "MS14", "valor": 32, "ram": 1.0, "cpu": 0.6},
    {"nome": "MS15", "valor": 52, "ram": 2.5, "cpu": 1.1},
]

LIMITE_RAM = 16.0
LIMITE_CPU = 8.0


def calcular_recursos(individuo):
    valor = 0.0
    ram = 0.0
    cpu = 0.0

    for bit, servico in zip(individuo, SERVICOS):
        if bit:
            valor += servico["valor"]
            ram += servico["ram"]
            cpu += servico["cpu"]

    return valor, ram, cpu


def fitness_rigido(individuo):
    valor, ram, cpu = calcular_recursos(individuo)

    if ram > LIMITE_RAM or cpu > LIMITE_CPU:
        return 0.0

    return valor


def fitness_proporcional(individuo):
    valor, ram, cpu = calcular_recursos(individuo)

    excesso_ram = max(0.0, ram - LIMITE_RAM)
    excesso_cpu = max(0.0, cpu - LIMITE_CPU)

    percentual_ram = excesso_ram / LIMITE_RAM
    percentual_cpu = excesso_cpu / LIMITE_CPU

    penalidade = percentual_ram + percentual_cpu

    return max(0.0, valor * (1.0 - penalidade))


def diversidade_genetica(populacao):
    """
    Mede diversidade através da proporção média de posições que
    diferem entre pares de indivíduos.
    """
    if len(populacao) < 2:
        return 0.0

    distancias = []

    for i in range(len(populacao)):
        for j in range(i + 1, len(populacao)):
            diferencas = sum(
                a != b
                for a, b in zip(populacao[i], populacao[j])
            )

            distancias.append(
                diferencas / len(populacao[i])
            )

    return statistics.mean(distancias)


class AlgoritmoGenetico:
    def __init__(
        self,
        tamanho_populacao=50,
        geracoes=100,
        taxa_mutacao=0.02,
        taxa_crossover=0.8,
        estrategia="A",
        seed=42
    ):
        random.seed(seed)

        self.tamanho_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.taxa_mutacao = taxa_mutacao
        self.taxa_crossover = taxa_crossover
        self.estrategia = estrategia

        self.populacao = [
            self.criar_individuo()
            for _ in range(tamanho_populacao)
        ]

        self.media_historico = []
        self.desvio_historico = []
        self.diversidade_historico = []

    def criar_individuo(self):
        return [
            random.randint(0, 1)
            for _ in SERVICOS
        ]

    def fitness(self, individuo):
        if self.estrategia == "A":
            return fitness_rigido(individuo)

        return fitness_proporcional(individuo)

    def torneio(self, k=3):
        candidatos = random.sample(self.populacao, k)

        return max(
            candidatos,
            key=self.fitness
        ).copy()

    def crossover(self, pai1, pai2):
        if random.random() > self.taxa_crossover:
            return pai1.copy(), pai2.copy()

        ponto = random.randint(1, len(pai1) - 1)

        filho1 = pai1[:ponto] + pai2[ponto:]
        filho2 = pai2[:ponto] + pai1[ponto:]

        return filho1, filho2

    def mutacao(self, individuo):
        individuo = individuo.copy()

        for i in range(len(individuo)):
            if random.random() < self.taxa_mutacao:
                individuo[i] = 1 - individuo[i]

        return individuo

    def executar(self):
        for _ in range(self.geracoes):

            fitnesses = [
                self.fitness(ind)
                for ind in self.populacao
            ]

            self.media_historico.append(
                statistics.mean(fitnesses)
            )

            self.desvio_historico.append(
                statistics.pstdev(fitnesses)
            )

            self.diversidade_historico.append(
                diversidade_genetica(self.populacao)
            )

            nova_populacao = []

            # Elitismo.
            elite = max(
                self.populacao,
                key=self.fitness
            ).copy()

            nova_populacao.append(elite)

            while len(nova_populacao) < self.tamanho_populacao:

                pai1 = self.torneio()
                pai2 = self.torneio()

                filho1, filho2 = self.crossover(
                    pai1,
                    pai2
                )

                filho1 = self.mutacao(filho1)
                filho2 = self.mutacao(filho2)

                nova_populacao.append(filho1)

                if len(nova_populacao) < self.tamanho_populacao:
                    nova_populacao.append(filho2)

            self.populacao = nova_populacao

        melhor = max(
            self.populacao,
            key=self.fitness
        )

        return melhor


def executar_experimento(estrategia, seed):
    ag = AlgoritmoGenetico(
        tamanho_populacao=50,
        geracoes=100,
        taxa_mutacao=0.02,
        taxa_crossover=0.8,
        estrategia=estrategia,
        seed=seed
    )

    melhor = ag.executar()

    valor, ram, cpu = calcular_recursos(melhor)

    return {
        "estrategia": estrategia,
        "melhor": melhor,
        "valor": valor,
        "ram": ram,
        "cpu": cpu,
        "fitness": ag.fitness(melhor),
        "media_final": ag.media_historico[-1],
        "desvio_final": ag.desvio_historico[-1],
        "diversidade_final": ag.diversidade_historico[-1],
        "media_historico": ag.media_historico,
        "desvio_historico": ag.desvio_historico,
        "diversidade_historico": ag.diversidade_historico,
    }


def imprimir_resultado(resultado):
    selecionados = [
        SERVICOS[i]["nome"]
        for i, bit in enumerate(resultado["melhor"])
        if bit == 1
    ]

    print("\n=== LAB 02 ===")
    print(f"Estratégia: {resultado['estrategia']}")
    print(f"Selecionados: {selecionados}")
    print(f"Valor: {resultado['valor']:.2f}")
    print(f"RAM: {resultado['ram']:.2f} GB")
    print(f"CPU: {resultado['cpu']:.2f} cores")
    print(f"Fitness: {resultado['fitness']:.2f}")
    print(
        f"Diversidade final: "
        f"{resultado['diversidade_final']:.6f}"
    )


if __name__ == "__main__":
    resultado_a = executar_experimento("A", 42)
    resultado_b = executar_experimento("B", 42)

    imprimir_resultado(resultado_a)
    imprimir_resultado(resultado_b)

    print("\n=== COMPARAÇÃO ===")
    print(
        f"Média final A: "
        f"{resultado_a['media_final']:.4f}"
    )
    print(
        f"Desvio final A: "
        f"{resultado_a['desvio_final']:.4f}"
    )
    print(
        f"Média final B: "
        f"{resultado_b['media_final']:.4f}"
    )
    print(
        f"Desvio final B: "
        f"{resultado_b['desvio_final']:.4f}"
    )
