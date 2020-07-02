def gerar_subconjuntos(s, vet, k, n):
    if k == n:
        for i in range(n):
            if vet[i] == True:
                print('{}'.format(s[i]), end=', ')
        print()
    else:
        vet[k] = True
        gerar_subconjuntos(s, vet, k + 1, n)
        vet[k] = False
        gerar_subconjuntos(s, vet, k + 1, n)


s = [i for i in range(10)]
tam_s = len(s)
vet = [False for i in range(tam_s)]
gerar_subconjuntos(s, vet, 0, tam_s)
