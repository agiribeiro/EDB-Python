import random


def particiona(v, ini, fim):
    # o pivo é o elemento do início
    pivo = ini
    for i in range(ini + 1, fim + 1):
        if v[i] <= v[ini]:
            pivo += 1
            v[i], v[pivo] = v[pivo], v[i]
    v[pivo], v[ini] = v[ini], v[pivo]
    return pivo


def quick_sort(v, ini, fim):
    # se o fim for maior que o inicio,
    # então eu calculo a posição do pivô utilizando
    # a função particiona
    if fim > ini:
        pivo = particiona(v, ini, fim)
        # Tendo o pivô, chama a função duas vezes para cada partição,
        # a primeira dos elementos antes do pivô
        # e a segunda dos elementos que estão depois do pivô
        quick_sort(v, ini, pivo - 1)
        quick_sort(v, pivo + 1, fim)


if __name__ == '__main__':
    def gera_lista(n):
        lista = []
        for i in range(n):
            lista.append(random.randint(1, 1000))
        return lista


    v = gera_lista(100)
    print(v)
    quick_sort(v, 0, len(v) - 1)
    print(v)
