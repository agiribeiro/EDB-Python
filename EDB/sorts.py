import numpy as np
import datetime
import random
from Algoritmos_e_Estrutura_de_Dados import bubble_sort, insertion_sort, selection_sort, quick_sort


if __name__ == '__main__':
    def gera_lista(n):
        lista = []
        for i in range(n):
            lista.append(random.randint(1, 1000000))
        return lista

    faster = []
    n = 10000
    inicio = datetime.datetime.now()
    for i in range(1000):
        inic = datetime.datetime.now()
        lista = gera_lista(n)
        print('gerando lista: ', datetime.datetime.now() - inic)
        print()
        dic = {}

        v = lista[:]
        ini = datetime.datetime.now()
        insertion_sort.insertion_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'insertion'

        v = lista[:]
        ini = datetime.datetime.now()
        selection_sort.selection_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'selection'

        v = lista[:]
        ini = datetime.datetime.now()
        quick_sort.quick_sort(v, 0, len(v) - 1)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'quick'

        v = lista[:]
        ini = datetime.datetime.now()
        bubble_sort.bubble_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'bubble'

        v = np.array(lista[:])
        ini = datetime.datetime.now()
        bubble_sort.bubble_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_bubble'

        v = np.array(lista[:])
        ini = datetime.datetime.now()
        insertion_sort.insertion_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_insertion'

        v = np.array(lista[:])
        ini = datetime.datetime.now()
        selection_sort.selection_sort(v)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_selection'

        v = np.array(lista[:])
        ini = datetime.datetime.now()
        quick_sort.quick_sort(v, 0, len(v) - 1)
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_quick'

        v = np.array(lista[:])
        ini = datetime.datetime.now()
        v.sort()
        fim = datetime.datetime.now()
        dic[fim - ini] = 'np_tim'

        v = lista[:]
        ini = datetime.datetime.now()
        v.sort()
        fim = datetime.datetime.now()
        dic[fim - ini] = 'tim'

        faster.append(dic.get(min(dic.keys())))

        for chave, valor in sorted(dic.items()):
            print('{:>13}: {}'.format(valor, chave))

        print('\n=======================', i, '=>', datetime.datetime.now() - inicio, '=========================\n')
    print(faster)