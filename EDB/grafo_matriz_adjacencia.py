class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]
        self.visitados = [False] * self.vertices

    def add_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def show(self):
        for i in self.grafo:
            for j in i:
                print(j, end=', ')
            print()

    def tem_ligacao(self, u, v):
        if self.grafo[u - 1][v - 1] == 1:
            return True
        return False

    def dfs(self, u):
        self.visitados[u - 1] = True
        print('{} visitado.'.format(u))
        for i in range(1, self.vertices + 1):
            if self.grafo[u - 1][i - 1] == 1 and not self.visitados[i - 1]:
                self.dfs(i)

    def bfs(self, v):
        # lista de visitados
        visitados = [False] * self.vertices
        # marca 'v' como visitado
        visitados[v - 1] = True
        fila = [v - 1]
        # enquanto a fila não for vazia
        while len(fila) > 0:
            # obtem o elemento da fila
            v = fila[0]
            # para cada vertice 'u' adjacente a 'v'
            for u in range(self.vertices):
                # verifica se existe conexão
                if self.grafo[v][u] == 1:
                    # verifica se 'u' não foi visitado
                    if visitados[u] == False:
                        # marca 'u' como visitado
                        visitados[u] = True
                        # insere 'u' na fila
                        fila.append(u)
                        print('{} visitado'.format(u + 1))
            # remove 'v' da fila
            fila.pop(0)


g = Grafo(5)
g.add_aresta(1, 3)
g.add_aresta(3, 4)
g.add_aresta(2, 3)
g.add_aresta(3, 5)
g.add_aresta(4, 5)
g.show()

print(g.tem_ligacao(1, 5))
print(g.tem_ligacao(1, 3))
print('================================\n\n')

e = Grafo(5)
e.add_aresta(1, 4)
e.add_aresta(4, 2)
e.add_aresta(4, 5)
e.add_aresta(2, 5)
e.add_aresta(5, 3)
e.dfs(1)
print('================================\n\n')

c = Grafo(10)
c.add_aresta(1, 2)
c.add_aresta(1, 3)
c.add_aresta(1, 4)
c.add_aresta(2, 5)
c.add_aresta(3, 6)
c.add_aresta(3, 7)
c.add_aresta(4, 8)
c.add_aresta(5, 9)
c.add_aresta(6, 10)
c.bfs(1)
