from collections import defaultdict
import heapq


class MinHeap:
    def __init__(self):
        self._queue = []
        self._index = 0

    def insert(self, item: object, priority: object) -> object:
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def remove(self):
        return heapq.heappop(self._queue)[-1]

    def get_length(self):
        return len(self._queue)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertexes = {}

    def add_edge(self, src, dest, cost):
        self.graph[src].append((dest, cost))
        self.vertexes[src] = src
        self.vertexes[dest] = dest

    def dijkstra(self, src, dest):
        number_vertexes = len(self.vertexes)  # obtem o número de vértices
        p = [None for i in range(number_vertexes)]  # estimativas de menor custo
        p[src] = 0  # estima para a origem 0
        min_heap = MinHeap()  # constrói a min heap
        min_heap.insert(src, 0)  # insere a origem na min heap

        while min_heap.get_length() > 0:  # enquanto o tamanho da fila for maior que 0
            u = min_heap.remove()  # remove da fila de prioridades
            for edge in self.graph[u]:  # percorre os adjacentes de 'u'
                v, cost = edge  # obtem o vértice e o custo
                if p[v] is None or p[v] > p[u] + cost:  # relaxamento
                    p[v] = p[u] + cost  # atualiza a estimativa de custo
                    min_heap.insert(v, p[v])  # insere na fila de prioridades

        return p[dest]  # retorna o custo do menor caminho


g = Graph()
g.add_edge(0, 1, 1)
g.add_edge(0, 3, 3)
g.add_edge(0, 4, 10)
g.add_edge(1, 2, 5)
g.add_edge(2, 4, 1)
g.add_edge(3, 2, 2)
g.add_edge(3, 4, 6)

print(g.dijkstra(0, 4))

