# Onemax Problem with Simulated Annealing


import random

import math


class OneMax:
    def __init__(self, size):
        self.size = size
        self.solution = [random.randint(0, 1) for i in range(self.size)]
        self.cost = self.obj_fun(self.solution)

    def neighbor(self):
        new_neighbor = self.solution[:]
        pos = random.randint(0, self.size - 1)
        new_neighbor[pos] = 1 if new_neighbor[pos] == 0 else 0
        return new_neighbor

    # função objetivo
    def obj_fun(self, solution):
        return sum(solution)

    """
    Simulated Annealing
    t => temperatura inicial
    t_min => temperatura minima
    alpha => decaimento da temperatura
    max_iter => quantidade de iterações com a mesma temperatura
    """
    def run_anneal(self, t=1.0, t_min=0.00001, alpha=0.9, max_iter=100):
        while t > t_min:
            # iterações com uma mesma temperatura
            for i in range(max_iter):
                new_solution = self.neighbor()  # gera uma nova temperatura
                new_cost = self.obj_fun(new_solution)  # calcula o custo dessa nova solução
                delta = self.cost - new_cost  # calcula a diferença dos custos
                ap = math.exp(-delta / t)  # probabilidade de aceitação de uma solução de piora
                if ap > random.random():  # verifica se aceita ou não
                    self.solution = new_solution[:]  # copia a nova solução
                    self.cost = new_cost  # atribui o novo custo
            t *= alpha


one_max = OneMax(10)
print('Solução inicial: {}'.format(one_max.solution))
one_max.run_anneal()
print('Solução final: {}'.format(one_max.solution))
one_max = OneMax(50)
print('Solução inicial: {}'.format(one_max.solution))
one_max.run_anneal()
print('Solução final: {}'.format(one_max.solution))
one_max = OneMax(100)
print('Solução inicial: {}'.format(one_max.solution))
one_max.run_anneal()
print('Solução final: {}'.format(one_max.solution))
