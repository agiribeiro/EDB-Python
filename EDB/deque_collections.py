from collections import deque


def show(d):
    for i in d:
        print(i, end=' ')
    print()


d = deque()
d.append(1)  # adiciona do lado direito
d.appendleft(2)  # adiciona do lado esquerdo
d.append(3)
d.appendleft(4)

show(d)

print(d.pop())

show(d)

print(d.popleft())

show(d)

d.remove(1)

show(d)
