import random


def insertion_sort(v):
    len_v = len(v)

    for i in range(1, len_v):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave


if __name__ == '__main__':
    def gera_lista(n):
        lista = []
        for i in range(n):
            lista.append(random.randint(1, 1000))
        return lista

    v = gera_lista(10)
    print(v)
    insertion_sort(v)
    print(v)
