class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, label: object) -> object:
        # cria um novo nó
        node = Node(label)
        # verifica se a árvore está vazia
        if self.empty():
            self.root = node
        else:
            # árvore não vazia, insere recursivamente
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:
                    dad_node = curr_node
                    # verifica se vai para esquerda ou direita
                    if node.label < curr_node.label:
                        # vai para esquerda
                        curr_node = curr_node.left
                    else:
                        # vai para direita
                        curr_node = curr_node.right
                else:
                    # se curr_node é None, então encontrou onde inserir
                    if node.label < dad_node.label:
                        dad_node.left = node
                    else:
                        dad_node.right = node
                    break  # sai do loop

    def empty(self):
        if self.root is None:
            return True
        return False

    # mostra em pré-ordem (raiz-esq-dir)
    def show(self, curr_node):
        if curr_node is not None:
            print('%d' % curr_node.label, end=' ')
            self.show(curr_node.left)
            self.show(curr_node.right)

    def remove(self, label):
        # 3 casos
        #
        # Caso 1
        # o nó a ser removido não tem filhos
        # esse caso é simples, basta ar a ligação
        # do pai para None
        #
        # Caso 2
        # o nó a ser removido tem somente 1 filho
        # basta colocar o seu filho no lugar dele
        #
        # Caso 3
        # o nó a ser removido possui dois filhos
        # basta pegar o menor elemento da subárvore à direita
        dad_node = None  # parent
        curr_node = self.root
        while curr_node is not None:
            # verifica se encontrou o nó a ser removido
            if label == curr_node.label:
                # caso 1: o nó a ser removido não possui filhos (nó folha)
                if curr_node.left is None and curr_node.right is None:
                    # verifica se é a raiz
                    if dad_node is None:
                        self.root = None
                    else:
                        # verifica se é filho à esquerda ou à direita
                        if dad_node.left == curr_node:
                            dad_node.left = None
                        elif dad_node.right == curr_node:
                            dad_node.right = None

                # caso 2: o nó a ser removido possui somente um filho
                elif (curr_node.left is None and curr_node.right is not None) or \
                        (curr_node.left is not None and curr_node.right is None):
                    # verifica se o nó a ser removido é a raiz
                    if dad_node is None:
                        # verifica se o filho de curr_node é filho à esquerda
                        if curr_node.left is not None:
                            self.root = curr_node.left
                        else:  # senão o filho de curr_node é filho à direita
                            self.root = curr_node.right
                    else:
                        # verifica se o filho de curr_node é filho à esquerda
                        if curr_node.left is not None:
                            # verifica se curr_node é filho à esquerda
                            if dad_node.left and dad_node.left.label == curr_node.label:
                                dad_node.left = curr_node.left
                            else:  # senão curr_node é filho à direita
                                dad_node.right = curr_node.left
                        else:  # senão o filho de curr_node é filho à direita
                            # verifica se curr_node é filho à esquerda
                            if dad_node.left and dad_node.left.label == curr_node.label:
                                dad_node.left = curr_node.right
                            else:  # senão curr_node é filho à direita
                                dad_node.right = curr_node.right

                # caso 3: o nó a ser removido possui dois filhos
                # pega-se o menor elemento da subárvore à direita
                elif curr_node.left is not None and curr_node.right is not None:
                    dad_smaller_node = curr_node
                    smaller_node = curr_node.right
                    next_smaller = curr_node.right.left

                    while next_smaller is not None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller = smaller_node.left

                    # verifica se o nó a ser removido é a raiz
                    if dad_node is None:
                        # Caso especial: o nó que vai ser a nova raiz é filho da raiz
                        if self.root.right.label == smaller_node.label:
                            smaller_node.left = self.root.left
                        else:
                            # verifica se o smaller_node é filho à esquerda ou à direita
                            # para ar para None o smaller_node
                            if dad_smaller_node.left and dad_smaller_node.left.label == smaller_node.label:
                                dad_smaller_node.left = None
                            else:
                                dad_smaller_node.right = None

                            # a os filhos à direita e esquerda de smaller_node
                            smaller_node.left = curr_node.left
                            smaller_node.right = curr_node.right

                        # faz com que o smaller_node seja a raiz
                        self.root = smaller_node

                    else:
                        # verifica se curr_node é filho à esquerda ou à direita
                        # para ar o smaller_node como filho do pai do curr_node (dad_node)
                        if dad_node.left and dad_node.left.label == curr_node.label:
                            dad_node.left = smaller_node
                        else:
                            dad_node.right = smaller_node
                        # verifica se o smaller_node é filho à esquerda ou à direita
                        # para ar para None o smaller_node
                        if dad_smaller_node.left and dad_smaller_node.left.label == smaller_node.label:
                            dad_smaller_node.left = None
                        else:
                            dad_smaller_node.right = None

                        # a os filhos à direita e esquerda de smaller_node
                        smaller_node.left = curr_node.left
                        smaller_node.right = curr_node.right

                break  # sai do loop

            dad_node = curr_node
            # verifica se vai para esquerda ou direita
            if label < curr_node.label:
                # vai para esquerda
                curr_node = curr_node.left
            else:
                # vai para direita
                curr_node = curr_node.right

    # mostra em pré-ordem (raiz-esq-dir)
    def pre_ordem(self, curr_node):
        if curr_node is not None:
            print('{}'.format(curr_node.label), end=', ')
            self.pre_ordem(curr_node.left)
            self.pre_ordem(curr_node.right)

    def ordem(self, curr_node):
        if curr_node is not None:
            self.ordem(curr_node.left)
            print('{}'.format(curr_node.label), end=', ')
            self.ordem(curr_node.right)

    def pos_ordem(self, curr_node):
        if curr_node is not None:
            self.pos_ordem(curr_node.right)
            self.pos_ordem(curr_node.left)
            print('{}'.format(curr_node.label), end=', ')


t = BinarySearchTree()
t.insert(8)
t.insert(3)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(10)
t.insert(14)
t.insert(13)

t.show(t.root)
print()

t.remove(8)
t.show(t.root)
print()

# # t.remove(13)
# t.show(t.root)
# print()
#
# # t.insert(1)
# # t.insert(13)
# t.show(t.root)
# print()
#
# t.remove(10)
# t.show(t.root)
# print()
#
# # t.remove(10)
# t.show(t.root)
# print()
# print(t.root.label)

#
# t = BinarySearchTree()
# t.insert(8)
# t.insert(3)
# t.insert(1)
# t.insert(6)
# t.insert(4)
# t.insert(7)
# t.insert(10)
# t.insert(14)
# t.insert(13)
# t.insert(9)
#
# t.remove(8)
#
# t.show(t.Root())
