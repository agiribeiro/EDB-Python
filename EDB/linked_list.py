class Node:

    def __init__(self, label):
        self.label = label
        self.next = None


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def empty(self):
        if self.len_list == 0:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):
        curr_node = self.first
        while curr_node:
            print(curr_node.label, end=' ')
            curr_node = curr_node.next
        print()

    def push(self, label, index):
        if index >= 0:
            node = Node(label)

        if self.empty():
            self.first = node
            self.last = node
        else:
            if index == 0:
                # inserção no inicio
                node.next = self.first
                self.first = node
            elif index >= self.len_list:
                # inserção no final
                self.last.next = node
                self.last = node
            else:
                # inserção no meio
                prev_node = self.first
                curr_node = self.first.next
                curr_index = 1
                while curr_node:
                    if curr_index == index:
                        # seta o curr_node como o próximo nó
                        node.next = curr_node
                        # seta o node como o próximo do prev_node
                        prev_node.next = node
                        break
                    prev_node = curr_node
                    curr_node = curr_node.next
                    curr_index += 1
        self.len_list += 1

    def pop(self, index):
        # if self.first.next is None:
        #     print(type(self.first.next))
        if not self.empty() and 0 <= index < self.len_list:
            flag_remove = False
            if self.first.next is None:
                print('único')
                # possui apenas 1 elemento
                node = self.first
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                print('inicio')
                # remove do início da lista
                node = self.first
                self.first = self.first.next
                flag_remove = True
            else:
                print('outro')
                prev_node = self.first
                curr_node = self.first.next
                curr_index = 1
                while curr_node:
                    if index == curr_index:
                        node = curr_node
                        prev_node.next = curr_node.next
                        curr_node.next = None
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.next
                    curr_index += 1

            if flag_remove:
                self.len_list -= 1
                return node.label


if __name__ == '__main__':
    lista = LinkedList()
    lista.push('Thiago', 0)
    lista.show()
    lista.push('Maria', 1)
    lista.show()
    lista.push('Marcos', 0)
    lista.show()
    lista.push('Catarina', 2)
    lista.show()
    lista.push('Lilica', 4)
    lista.show()
    lista.push('Sara', 2)
    lista.show()
    print('Tamanho da lista: {}'.format(lista.length()))
    lista.pop(0)
    lista.pop(0)
    lista.pop(0)
    lista.pop(0)
    lista.pop(0)
    lista.pop(0)
    lista.show()
    lista.pop(2)
    lista.show()
    lista.pop(3)
    lista.show()
    # lista.show()
    # # lista.show()
    print('Tamanho da lista: {}'.format(lista.length()))
