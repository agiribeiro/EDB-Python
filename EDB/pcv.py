# Gerador de grafos
import random


class GeradorGrafo:
    def __init__(self, n):
        self.n = n
        self.grafo = [[] for i in range(n)]
        self.custos = {}

    def gerar_grafo(self):
        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    if (i, j) and (j, i) not in self.custos:
                        custo = random.randint(1, 100)
                        self.custos[(i, j)] = custo
                        self.custos[(j, i)] = custo
                    self.grafo[i].append(j)

    def mostrar_grafo(self):
        for i in range(self.n):
            print('Adjacentes de {}: ||'.format(i), end='')
            for adj in self.grafo[i]:
                print('{:^3s}({:>3s}) || '.format(str(adj), str(self.custos[i, adj])), end='')
            print()

    def pcv_random(self, iteracoes):

        melhor_circuito = []
        melhor_custo = None

        def gerar_circuito(melhor_circuito, melhor_custo):

            vertices = [i for i in range(1, self.n)]
            circuito = [0]
            custo_circuito = 0

            while len(vertices) > 0:
                e = random.choice(vertices)
                vertices.remove(e)
                custo_circuito += self.custos[(circuito[-1], e)]
                circuito.append(e)

            custo_circuito += self.custos[(circuito[-1], 0)]

            if melhor_custo is None:
                melhor_circuito = circuito[:]
                melhor_custo = custo_circuito
                print('Circuito inicial: {}\ncusto: {}'.format(str(melhor_circuito), melhor_custo))
            else:
                if custo_circuito < melhor_custo:
                    melhor_circuito = circuito[:]
                    melhor_custo = custo_circuito

            return melhor_circuito, melhor_custo

        for i in range(iteracoes):
            melhor_circuito, melhor_custo = gerar_circuito(melhor_circuito, melhor_custo)
        print('Melhor circuito: {} - custo: {}'.format(str(melhor_circuito), melhor_custo))

    def pcv_genetico(self, tamanho_populacao,
                     geracoes,
                     tamanho_torneio,
                     probabilidade_cruzamento,
                     probabilidade_mutacao):
        populacao = []

        def gerar_individuo():
            vertices = [i for i in range(1, self.n)]
            individuo = [0]

            while len(vertices) > 0:
                e = random.choice(vertices)
                vertices.remove(e)
                individuo.append(e)

            return individuo

        # função de fitness
        def obter_custo(individuo):
            custo = 0
            for i in range(self.n - 1):
                custo += self.custos[(individuo[i], individuo[i + 1])]
            custo += self.custos[(individuo[-1], individuo[0])]
            return custo

        # gerando a população inicial
        for i in range(tamanho_populacao):
            populacao.append(gerar_individuo())

        # a cada geração
        for i in range(geracoes):
            # seleção por torneio
            for j in range(tamanho_torneio):
                if random.random() <= probabilidade_cruzamento:
                    pai1 = random.randint(0, tamanho_populacao - 1)
                    pai2 = random.randint(0, tamanho_populacao - 1)
                    while pai1 == pai2:
                        pai1 = random.randint(0, tamanho_populacao - 1)
                        pai2 = random.randint(0, tamanho_populacao - 1)

                    filho1_validos = [i for i in range(self.n)]
                    filho2_validos = [i for i in range(self.n)]
                    filho1, filho2 = [], []

                    # cruzamento de um ponto
                    while True:
                        # selecionando um ponto
                        ponto = random.randint(0, self.n - 1)

                        if ponto != 0 and ponto != (self.n - 1):
                            for p in range(ponto):
                                if populacao[pai1][p] not in filho1:
                                    filho1.append(populacao[pai1][p])
                                    filho1_validos.remove(populacao[pai1][p])
                                else:
                                    e = random.choice(filho1_validos)
                                    filho1.append(e)
                                    filho1_validos.remove(e)
                                if populacao[pai2][p] not in filho2:
                                    filho2.append(populacao[pai2][p])
                                    filho2_validos.remove(populacao[pai2][p])
                                else:
                                    e = random.choice(filho2_validos)
                                    filho2.append(e)
                                    filho2_validos.remove(e)
                            for p in range(ponto, self.n):
                                if populacao[pai2][p] not in filho1:
                                    filho1.append(populacao[pai2][p])
                                    filho1_validos.remove(populacao[pai2][p])
                                else:
                                    e = random.choice(filho1_validos)
                                    filho1.append(e)
                                    filho1_validos.remove(e)
                                if populacao[pai1][p] not in filho2:
                                    filho2.append(populacao[pai1][p])
                                    filho2_validos.remove(populacao[pai1][p])
                                else:
                                    e = random.choice(filho2_validos)
                                    filho2.append(e)
                                    filho2_validos.remove(e)
                            # print(ponto)
                            # print('Pai 1: {}'.format(populacao[pai1]))
                            # print('Pai 2: {}'.format(populacao[pai2]))
                            # print('Gen 1: {}'.format(filho1))
                            # print('Gen 2: {}'.format(filho2))
                            break

                    if random.random() <= probabilidade_mutacao:
                        gene1 = random.randint(0, self.n - 1)
                        gene2 = random.randint(0, self.n - 1)
                        while gene1 == gene2:
                            gene1 = random.randint(0, self.n - 1)
                            gene2 = random.randint(0, self.n - 1)
                        filho1[gene1], filho1[gene2] = filho1[gene2], filho1[gene1]
                        filho2[gene1], filho2[gene2] = filho2[gene2], filho2[gene1]

                    # obtem o fitness dos pais e dos filhos
                    fitness_pai1 = obter_custo(populacao[pai1])
                    fitness_pai2 = obter_custo(populacao[pai2])
                    fitness_filho1 = obter_custo(filho1)
                    fitness_filho2 = obter_custo(filho2)
                    if fitness_filho1 < fitness_pai1 or fitness_filho1 < fitness_pai2:
                        if fitness_filho1 < fitness_pai1:
                            populacao.pop(pai1)
                        else:
                            populacao.pop(pai2)
                        populacao.append(filho1)
                    elif fitness_filho2 < fitness_pai1 or fitness_filho2 < fitness_pai2:
                        if fitness_filho2 < fitness_pai1:
                            populacao.pop(pai1)
                        else:
                            populacao.pop(pai2)
                        populacao.append(filho2)

        # obtem o melhor individuo
        melhor_individuo = populacao[0][:]
        for individuo in range(1, tamanho_populacao):
            if obter_custo(populacao[individuo]) < obter_custo(melhor_individuo):
                melhor_individuo = populacao[individuo][:]

        print('Melhor Individuo: {}\nCusto: {}'.format(str(melhor_individuo), obter_custo(melhor_individuo)))


if __name__ == '__main__':
    gerardor = GeradorGrafo(20)
    gerardor.gerar_grafo()
    # gerardor.mostrar_grafo()
    gerardor.pcv_random(1000)
    gerardor.pcv_genetico(tamanho_populacao=10,
                          geracoes=1000,
                          tamanho_torneio=1,
                          probabilidade_cruzamento=0.7,
                          probabilidade_mutacao=0.1)
