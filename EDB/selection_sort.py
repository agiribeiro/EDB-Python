import random


def selection_sort(v):
    len_v = len(v)

    for i in range(len_v - 1):
        menor = i
        for j in range(i + 1, len_v):
            if v[j] < v[menor]:
                menor = j
        v[menor], v[i] = v[i], v[menor]


if __name__ == '__main__':
    def gera_lista(n):
        lista = []
        for i in range(n):
            lista.append(random.randint(1, 1000))
        return lista

    v = gera_lista(10)
    print(v)
    selection_sort(v)
    print(v)
