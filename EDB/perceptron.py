"""

Implementação da rede neural Perceptron

u = g(u) -> y
w = w + N * (d(k) - y) * x(k)

"""
from random import random

import copy


class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):
        """

        :type amostras: list
        :param amostras: todas as amostras
        :param saidas: saídas respectivas de cada amostra
        :param taxa_aprendizado: taxa de aprendizado (entre 0 e 1)
        :param epocas: número de épocas
        :param limiar: limiar
        """
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.limiar = limiar
        self.num_amostras = len(amostras)
        self.num_amostra = len(amostras[0])
        self.pesos = []

    def treinar(self):
        """
        Função para treinar a rede
        :return:
        """
        for amostra in self.amostras:                       # Adiciona -1 para cada uma das amostras
            # assert isinstance(amostra, list)
            amostra.insert(0, -1)
        for i in range(self.num_amostra):                   # Inicia o vetor de pesos com valores aleatórios
            self.pesos.append(random())
        self.pesos.insert(0, self.limiar)                   # Insere o limiar no vetor de pesos

        num_epocas = 0                                      # Inicia o contador de epocas
        # erro = True                                         # Existe erro
        # while num_epocas <= self.epocas and erro:
        while True:
            erro = False
            for i in range(self.num_amostras):              # Para todas as amostras de treinamento
                u = 0
                for j in range(self.num_amostra + 1):       # Realiza p somatório, o limite (self.amostra + 1)
                    u += self.pesos[j] * self.amostras[i][j]   # é porque foi inserido o -1 para cada amostra

                y = self.sinal(u)                           # Obtém a saída da rede utilizando a função de ativação

                if y != self.saidas[i]:                     # Verifica se a saída da rede é diferente da saída desejada

                    erro_aux = self.saidas[i] - y   # Calcula o erro: subtração entre a saída desejada e a saída da rede

                    for j in range(self.num_amostra + 1):   # Faz o ajuste dos pesos para cada elemento da amostra
                        self.pesos[j] += self.taxa_aprendizado * erro_aux * self.amostras[i][j]
                    erro = True

                # else:                                       # Não existe mais erro
                #     erro = False

            # num_epocas += 1                                 # Incrementa o número de épocas
            if num_epocas > self.epocas or not erro:
                break
        print(self.pesos)

    def testar(self, amostra, classe1, classe2):
        """
        Função utilizada para testar a rede
        Recebe uma amostra a ser classificada e os nomes das classes.
        Utiliza a função sinal, se é -1 então é classe1, senão é classe2

        :type amostra: list
        :param amostra: Amostra a ser testada
        :param classe1:
        :param classe2:
        :return:
        """
        amostra.insert(0, -1)                               # Insere -1 na amostra

        u = 0                                               # Utiliza o vetor de pesos
        for i in range(self.num_amostra + 1):               # que foi ajustado na fase de treinamento
            u += self.pesos[i] * amostra[i]
        y = self.sinal(u)                                   # Calcula a saída da rede
        # print(y, u)
        classe = classe1 if y == -1 else classe2            # Verifica a qual classe pertence
        print('A amostra pertence a classe {}'.format(classe))

    @staticmethod
    def sinal(u):
        return 1 if u >= 0 else -1


if __name__ == '__main__':
    print('A ou B?')

    amostras = [[0.1, 0.4, 0.7],
                [0.3, 0.7, 0.2],
                [0.6, 0.9, 0.8],
                [0.5, 0.7, 0.1]]
    # saídas desejadas de cada amostra
    saidas = [1, -1, -1, 1]

    testes = copy.deepcopy(amostras)

    rede = Perceptron(amostras=amostras, saidas=saidas, taxa_aprendizado=0.1, epocas=1000)
    rede.treinar()
    for teste in testes:
        rede.testar(teste, 'A', 'B')
