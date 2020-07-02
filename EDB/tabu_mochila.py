# Busca tabu para resolver o problema da mochila


import random


"""
configuração da mochila
para cada sublista, o primeiro elemento é o peso
e o segundo elemento é o benefício
"""


def obter_avaliacao(melhor_solucao, mochila, capacidade_maxima):
    somatorio_peso, somatorio_beneficio = 0, 0

    for i in range(len(melhor_solucao)):
        somatorio_peso += melhor_solucao[i] * mochila[i][0]
        somatorio_beneficio += melhor_solucao[i] * mochila[i][1]
    avaviacao = somatorio_beneficio * (1 - max(0, somatorio_peso - capacidade_maxima))

    return avaviacao


def obter_peso(solucao, mochila):
    peso = 0
    for i in range(len(solucao)):
        peso += solucao[i] * mochila[i][0]
    return peso


def gerar_vizinhos(melhor_solucao, max_vizinhos):
    vizinhos = []
    pos = 0
    for i in range(max_vizinhos):
        vizinho = []
        for j in range(len(melhor_solucao)):
            if j == pos:
                if melhor_solucao[j] == 0:
                    vizinho.append(1)
                else:
                    vizinho.append(0)
            else:
                vizinho.append(melhor_solucao[j])
        vizinhos.append(vizinho)
        pos += 1
    return vizinhos


def obter_avaliacao_vizinhos(vizinhos, mochila, capacidade_maxima, max_vizinhos):
    vizinhos_avaliacao = []
    for i in range(max_vizinho):
        vizinhos_avaliacao.append(obter_avaliacao(vizinhos[i], mochila, capacidade_maxima))
    return vizinhos_avaliacao


def obter_bit_modificado(melhor_solucao, melhor_vizinho):
    for i in range(len(melhor_solucao)):
        if melhor_solucao[i] != melhor_vizinho[i]:
            return i


def obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos):
    maxima_avaliacao = max(vizinhos_avaliacao)
    pos = 0
    bit_proibido = -1

    if len(lista_tabu) != 0:
        bit_proibido = lista_tabu[0]

    for i in range(len(vizinhos_avaliacao)):
        if vizinhos_avaliacao[i] == maxima_avaliacao:
            pos = i
            break

    if bit_proibido != -1:
        bit_pos = obter_bit_modificado(melhor_solucao, vizinhos[pos])

        if bit_pos == bit_proibido:
            melhor_pos = 0
            for i in range(len(vizinhos_avaliacao)):
                if i != bit_pos:
                    if vizinhos_avaliacao[i] > vizinhos_avaliacao[melhor_pos]:
                        melhor_pos = i
            return melhor_pos

    return pos


mochila = [[4, 2], [5, 2], [7, 3], [9, 4], [6, 4]]

iteracao, melhor_iteracao = 0, 0
melhor_solucao = []  # Guarda a melhor solução
lista_tabu = []  # lista tabu
capacidade_maxima = 23  # capacidade máxima da mochila
bt_max = 1  # quantidade máxima de iterações sem melhora no valor da melhor solução
max_vizinho = 5  # quantidade máxima de vizinhos

for i in range(len(mochila)):
    bit = random.randint(0, 1)
    melhor_solucao.append(bit)

print('Solução inicial: {0}, Avaliação: {1}'.format(melhor_solucao,
                                                    obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)))
peso_corrente = obter_peso(melhor_solucao, mochila)
melhor_avaliacao = obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)
vizinhos = gerar_vizinhos(melhor_solucao, max_vizinho)
print('vizinhos', vizinhos)
vizinhos_avaliacao = obter_avaliacao_vizinhos(vizinhos, mochila, capacidade_maxima, max_vizinho)
pos_melhor_vizinho = obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos)

if vizinhos_avaliacao[pos_melhor_vizinho] > melhor_avaliacao:
    bit_modificado = obter_bit_modificado(melhor_solucao, vizinhos[pos_melhor_vizinho])
    lista_tabu.append(bit_modificado)
    melhor_solucao = vizinhos[pos_melhor_vizinho][:]
    melhor_iteracao += 1

iteracao += 1

while (iteracao - melhor_iteracao) < bt_max:
    """
    A condição de parada é se a diferença entre a iteraçaão e a melhor iteração
    for maior que bt_max. A iteração global (sempre é incrementada).
    melhor_iteração é a iteração onde se achou a melhor solução (nem sempre é incrementada).
    bt_max é o máximo de iterações sem melhora no valor da melhor solução.
    """
    print('vizinhos', vizinhos)
    vizinhos = gerar_vizinhos(melhor_solucao, max_vizinho)[:]
    vizinhos_avaliacao = obter_avaliacao_vizinhos(vizinhos, mochila, capacidade_maxima, max_vizinho)[:]
    pos_melhor_vizinho = obter_vizinho_melhor_avaliacao(vizinhos_avaliacao, lista_tabu, melhor_solucao, vizinhos)

    if vizinhos_avaliacao[pos_melhor_vizinho] > melhor_avaliacao:
        bit_modificado = obter_bit_modificado(melhor_solucao, vizinhos[pos_melhor_vizinho])
        lista_tabu[0] = bit_modificado
        melhor_solucao = vizinhos[pos_melhor_vizinho][:]
        melhor_avaliacao = vizinhos_avaliacao[pos_melhor_vizinho]
        melhor_iteracao += 1

    iteracao += 1

print('Solução inicial: {0}, Avaliação: {1}'.format(melhor_solucao,
                                                    obter_avaliacao(melhor_solucao, mochila, capacidade_maxima)))
print('Melhor iteração: {0}'.format(melhor_iteracao))
print('Iteração: {0}'. format(iteracao))
