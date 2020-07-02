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
                print('Circuito inicial: {} - custo: {}'.format(str(melhor_circuito), melhor_custo))
            else:
                if custo_circuito < melhor_custo:
                    melhor_circuito = circuito[:]
                    melhor_custo = custo_circuito

            return melhor_circuito, melhor_custo

        for i in range(iteracoes):
            melhor_circuito, melhor_custo = gerar_circuito(melhor_circuito, melhor_custo)
        print('Melhor circuito: {} - custo: {}'.format(str(melhor_circuito), melhor_custo))


if __name__ == '__main__':
    gerardor = GeradorGrafo(20)
    gerardor.gerar_grafo()
    # gerardor.mostrar_grafo()
    gerardor.pcv_random(1000000)
