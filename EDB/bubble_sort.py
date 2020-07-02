import numpy as np
import datetime
import random
from Algoritmos_e_Estrutura_de_Dados import insertion_sort, selection_sort, quick_sort

# Implementação do Bubble Sort


def bubble_sort(v):
    len_v = len(v)
    i = len_v - 1

    for i in range(len_v - 1, 0, -1):
        swapped = False
        for j in range(i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                swapped = True
        if not swapped:
            break


if __name__ == '__main__':
    def gera_lista(n):
        lista = []
        for i in range(n):
            lista.append(random.randint(1, 1000000))
        return lista

    faster = []
    n = 10000
    for i in range(1000):
        list = gera_lista(n)
        dic = {}

        v = list[:]
        ini = datetime.datetime.now()
        insertion_sort.insertion_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'insertion'

        v = list[:]
        ini = datetime.datetime.now()
        selection_sort.selection_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'selection'

        v = list[:]
        ini = datetime.datetime.now()
        quick_sort.quick_sort(v, 0, len(v) - 1)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'quick'

        v = list[:]
        ini = datetime.datetime.now()
        bubble_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'bubble'

        v = np.array(list[:])
        ini = datetime.datetime.now()
        bubble_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_bubble'

        v = np.array(list[:])
        ini = datetime.datetime.now()
        insertion_sort.insertion_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_insertion'

        v = np.array(list[:])
        ini = datetime.datetime.now()
        selection_sort.selection_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_selection'

        v = np.array(list[:])
        ini = datetime.datetime.now()
        quick_sort.quick_sort(v, 0, len(v) - 1)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_quick'

        faster.append(dic.get(min(dic.keys())))

        for chave, valor in sorted(dic.items()):
            print('{:>13}: {}'.format(valor, chave))

        print('\n================================================\n')
    print(faster)