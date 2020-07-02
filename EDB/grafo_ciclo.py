class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista = [[] for i in range(vertices)]

    def add_aresta(self, origin, destiny):
        self.lista[origin].append(destiny)

    def dfs(self, v):
        pilha, pilha_rec = [], []
        visited = [False for i in range(self.vertices)]
        pilha_rec = [False for i in range(self.vertices)]
        while True:
            neighbour_found = False
            if not visited[v]:
                pilha.append(v)
                visited[v] = pilha_rec[v] = True
            aux_adj = None
            for adj in self.lista[v]:
                aux_adj = adj
                # se o vizinho está na pilha é porque existe ciclo
                if pilha_rec[adj]:
                    return True
                elif not visited[adj]:
                    # se não está na pilha e não foi visitado, indica que achou
                    neighbour_found = True
                    break
            if not neighbour_found:
                pilha_rec[pilha[-1]] = False  # marca que saiu da pilha
                pilha.pop()  # remove da pilha
                if len(pilha) == 0:
                    break
                v = pilha[-1]
            else:
                v = aux_adj
        return False

    def has_cycle(self):
        for i in range(self.vertices):
            if self.dfs(i):
                return True
        return False


g = Grafo(4)
g.add_aresta(0, 1)
g.add_aresta(1, 2)
g.add_aresta(2, 1)
print(g.has_cycle())
