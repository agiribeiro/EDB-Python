from collections import defaultdict


class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age


class Friendship:
    def __init__(self, person1, person2):
        self.person1, self.person2 = person1, person2


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, p1, p2):
        self.graph[p1.name].append(p2)
        self.graph[p2.name].append(p1)

    def show_friends(self, name):
        for friend in self.graph[name]:
            print('{}'.format(friend.name))


p1 = Person('Maria', 20)
p2 = Person('Pedro', 30)
p3 = Person('Diego', 18)
p4 = Person('Carol', 25)
p5 = Person('Yankee', 14)

g = Graph()
g.add_edge(p1, p2)
g.add_edge(p1, p3)
g.add_edge(p2, p4)
g.add_edge(p4, p3)
g.add_edge(p3, p4)
g.add_edge(p5, p1)

print('Amigos de {}'.format(p1.name))
g.show_friends(p1)
print('================\n\n')
print('Amigos de {}'.format(p2.name))
g.show_friends(p2)
print('================\n\n')
print('Amigos de {}'.format(p3.name))
g.show_friends(p3)
print('================\n\n')
print('Amigos de {}'.format(p4.name))
g.show_friends(p4)
print('================\n\n')
print('Amigos de {}'.format(p5.name))
g.show_friends(p5)
print('================\n\n')
