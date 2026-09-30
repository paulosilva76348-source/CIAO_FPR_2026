Cenário:
Conectar 10 switches de rede em uma topologia em árvore geradora que minimize a latência total acumulada entre os pares mais críticos, respeitando a matriz de latências físicas de cabeamento D (10x10).

Requisitos do Código:
- Implementar do zero o algoritmo de Colônia de Formigas (ACO) adaptado para seleção de arestas em grafos.
- Incluir verificação de ciclos/conectividade ao longo da construção da rota das formigas para garantir que a solução final forme um grafo/árvore válido.
- Atualização da matriz de feromônio tau_ij com taxa de evaporação rho = 0.2 aplicada apenas às melhores topologias da iteração.

Artefatos e Testes:
- Imprimir a Matriz de Adjacência final (10x10) do grafo de rede otimizado pelo ACO.
- Apresentar o ganho percentual de redução de latência obtido pelo ACO em relação a uma topologia gerada de forma aleatória.

                                                                                                                                                                                                  import random
import math


NUM_SWITCHES = 10
RHO = 0.2
NUM_FORMIGAS = 30
ITERACOES = 100
ALPHA = 1.0
BETA = 2.0


# Substituir pela matriz D fornecida na atividade.
D = [
    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
    [10, 0, 15, 25, 35, 45, 55, 65, 75, 85],
    [20, 15, 0, 10, 20, 30, 40, 50, 60, 70],
    [30, 25, 10, 0, 15, 25, 35, 45, 55, 65],
    [40, 35, 20, 15, 0, 10, 20, 30, 40, 50],
    [50, 45, 30, 25, 10, 0, 15, 25, 35, 45],
    [60, 55, 40, 35, 20, 15, 0, 10, 20, 30],
    [70, 65, 50, 45, 30, 25, 10, 0, 15, 25],
    [80, 75, 60, 55, 40, 35, 20, 15, 0, 10],
    [90, 85, 70, 65, 50, 45, 30, 25, 10, 0]
]


def validar_matriz(D):
    if len(D) != NUM_SWITCHES:
        raise ValueError(
            "D deve possuir 10 linhas."
        )

    for linha in D:
        if len(linha) != NUM_SWITCHES:
            raise ValueError(
                "D deve possuir 10 colunas."
            )

    for i in range(NUM_SWITCHES):
        if D[i][i] != 0:
            raise ValueError(
                "A diagonal de D deve ser zero."
            )


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[
                self.parent[x]
            ]
            x = self.parent[x]

        return x

    def union(self, a, b):
        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            return False

        if self.rank[raiz_a] < self.rank[raiz_b]:
            self.parent[raiz_a] = raiz_b

        elif self.rank[raiz_a] > self.rank[raiz_b]:
            self.parent[raiz_b] = raiz_a

        else:
            self.parent[raiz_b] = raiz_a
            self.rank[raiz_a] += 1

        return True


def todas_as_arestas():
    arestas = []

    for i in range(NUM_SWITCHES):
        for j in range(i + 1, NUM_SWITCHES):

            if D[i][j] > 0:
                arestas.append((i, j))

    return arestas


def construir_arvore(tau):
    """
    Constrói uma árvore geradora utilizando probabilidades baseadas
    em feromônio e heurística de baixa latência.
    """

    arestas = todas_as_arestas()
    uf = UnionFind(NUM_SWITCHES)

    selecionadas = []

    while len(selecionadas) < NUM_SWITCHES - 1:

        candidatas = []

        for i, j in arestas:
            if uf.find(i) == uf.find(j):
                continue

            feromonio = tau[i][j]
            heuristica = 1.0 / max(D[i][j], 1e-9)

            peso = (
                feromonio ** ALPHA
                * heuristica ** BETA
            )

            candidatas.append(
                ((i, j), peso)
            )

        if not candidatas:
            raise RuntimeError(
                "Não foi possível construir árvore."
            )

        soma = sum(
            peso
            for _, peso in candidatas
        )

        if soma == 0:
            aresta, _ = random.choice(candidatas)

        else:
            sorteio = random.random() * soma
            acumulado = 0.0
            aresta = None

            for candidato, peso in candidatas:
                acumulado += peso

                if acumulado >= sorteio:
                    aresta = candidato
                    break

        i, j = aresta

        if uf.union(i, j):
            selecionadas.append(
                (i, j)
            )

    return selecionadas


def custo_arvore(arestas):
    return sum(
        D[i][j]
        for i, j in arestas
    )


def matriz_adjacencia(arestas):
    matriz = [
        [0 for _ in range(NUM_SWITCHES)]
        for _ in range(NUM_SWITCHES)
    ]

    for i, j in arestas:
        matriz[i][j] = 1
        matriz[j][i] = 1

    return matriz


def arvore_aleatoria():
    """
    Gera uma árvore aleatória válida usando ordem aleatória de
    arestas e Union-Find.
    """

    arestas = todas_as_arestas()
    random.shuffle(arestas)

    uf = UnionFind(NUM_SWITCHES)
    resultado = []

    for i, j in arestas:
        if uf.union(i, j):
            resultado.append((i, j))

            if len(resultado) == NUM_SWITCHES - 1:
                break

    return resultado


class ACO:
    def __init__(
        self,
        num_formigas=NUM_FORMIGAS,
        iteracoes=ITERACOES,
        rho=RHO,
        seed=42
    ):
        random.seed(seed)

        self.num_formigas = num_formigas
        self.iteracoes = iteracoes
        self.rho = rho

        self.tau = [
            [1.0 for _ in range(NUM_SWITCHES)]
            for _ in range(NUM_SWITCHES)
        ]

        self.melhor_global = None
        self.melhor_custo = float("inf")

        self.historico = []

    def evaporar(self):
        for i in range(NUM_SWITCHES):
            for j in range(NUM_SWITCHES):
                self.tau[i][j] *= (1.0 - self.rho)

    def depositar(self, melhores):
        """
        Depósito somente nas melhores topologias da iteração.
        """

        if not melhores:
            return

        melhor_custo = custo_arvore(melhores[0])

        for aresta in melhores[0]:
            i, j = aresta

            deposito = 1.0 / max(
                melhor_custo,
                1e-9
            )

            self.tau[i][j] += deposito
            self.tau[j][i] += deposito

    def executar(self):
        for _ in range(self.iteracoes):

            solucoes = []

            for _ in range(self.num_formigas):
                arvore = construir_arvore(self.tau)
                custo = custo_arvore(arvore)

                solucoes.append(
                    (custo, arvore)
                )

            solucoes.sort(
                key=lambda x: x[0]
            )

            melhores = [
                solucoes[0][1]
            ]

            melhor_custo, melhor_arvore = solucoes[0]

            if melhor_custo < self.melhor_custo:
                self.melhor_custo = melhor_custo
                self.melhor_global = melhor_arvore

            # Evaporação.
            self.evaporar()

            # Depósito somente da melhor topologia da iteração.
            self.depositar(melhores)

            self.historico.append(
                self.melhor_custo
            )

        return self.melhor_global, self.melhor_custo


def imprimir_matriz(matriz):
    print("\nMatriz de Adjacência:")

    for linha in matriz:
        print(
            " ".join(str(x) for x in linha)
        )


def executar_experimento():
    validar_matriz(D)

    aco = ACO(
        num_formigas=NUM_FORMIGAS,
        iteracoes=ITERACOES,
        rho=RHO,
        seed=42
    )

    melhor_arvore, custo_aco = aco.executar()

    random.seed(42)

    arvore_randomica = arvore_aleatoria()
    custo_randomico = custo_arvore(
        arvore_randomica
    )

    ganho = (
        (custo_randomico - custo_aco)
        / custo_randomico
        * 100.0
    )

    matriz = matriz_adjacencia(
        melhor_arvore
    )

    imprimir_matriz(matriz)

    print("\n=== RESULTADOS LAB 03 ===")
    print(
        f"Custo ACO: {custo_aco:.4f}"
    )
    print(
        f"Custo aleatório: {custo_randomico:.4f}"
    )
    print(
        f"Ganho percentual: {ganho:.2f}%"
    )

    return {
        "arvore": melhor_arvore,
        "matriz_adjacencia": matriz,
        "custo_aco": custo_aco,
        "custo_randomico": custo_randomico,
        "ganho_percentual": ganho,
        "historico": aco.historico
    }


if __name__ == "__main__":
    executar_experimento()
