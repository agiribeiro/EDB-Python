'''
Implementação da priority queue com lista ordenada
'''

class Person:

    '''
    nome => nome da  pessoa
    prior => prioridade da pessoa
    '''
    def __init__(self, name, prior):
        self.name, self.prior = name, prior


class PriorityQueue:

    def __init__(self):
        self.pq = []  # priority queue
        self.len = 0  # length of priority queue

    # insere decrescentemente pela prioridade
    def push(self, person):
        if self.empty():
            self.pq.append(person)
        else:
            # procura-se onde inserir para manter a fila ordenada
            flag_push = False
            for i in range(self.len):
                if self.pq[i].prior < person.prior:
                    self.pq.insert(i, person)
                    flag_push = True
                    break
            if not flag_push:
                # se entrou aqui é porque tem que inserir ao final
                self.pq.insert(self.len, person)
        self.len += 1

    def pop(self):
        if not self.empty():
            self.pq.pop(0)
            self.len -= 1

    def empty(self):
        if self.len == 0:
            return True
        return False

    def show(self):
        for p in self.pq:
            print('Nome: {}'.format(p.name))
            print('Prioridade: {}'.format(p.prior))


# criando os objetos Person
p1, p2, p3, p4 = Person('Thiago', 28), Person('Catarina', 3), Person('Pedro', 20), Person('João', 35)

# criando a fila de prioridade e inserindo os elementos
pq = PriorityQueue()
pq.push(p1)
pq.push(p2)
pq.push(p3)
pq.push(p4)

print('Exibindo após as inserções:')
pq.show()
print()

# removendo os elementos
pq.pop()
pq.pop()

print('Exibindo após as remoções:')
pq.show()
print()

# inserindo um novo elemento
pq.push(Person('Goku', 30))

print('Exibindo após a inserção')
pq.show()
