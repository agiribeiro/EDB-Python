# encoding: utf-8
# author: Thiago da Cunha Borges


def busca_binaria(lista, chave, ini=0, fim=None):
    if not fim:
        fim = len(lista) - 1

    if ini > fim:
        return False

    meio = (ini + fim) // 2

    if chave == lista[meio]:
        return True
    elif chave < lista[meio]:
        return busca_binaria(lista, chave, ini, meio - 1)
    else:
        return busca_binaria(lista, chave, meio + 1, fim)


lista = [11, 5, 10, 20, 15, 4]
lista.sort()
chave = 20
if busca_binaria(lista, chave):
    print('Encontrou')
else:
    print('Não encontrou')
