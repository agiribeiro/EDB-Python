# Primeiro a ser inserido é o último a ser removido


class Stack:  # Stack

    def __init__(self):
        self.stack = []
        self.len_stack = 0

    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            e = self.stack.pop(self.len_stack)
            self.len_stack -= 1
            return e

    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None

    def empty(self):
        if self.len_stack == 0:
            return True
        return False

    def lenght(self):
        return self.len_stack


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())
    print(s.empty())
    s.pop()
    print(s.top())
    s.pop()
    print(s.lenght())
