class Deque:

    def __init__(self):
        self.deque = []
        self.len = 0

    def empty(self):
        if self.len == 0:
            return True
        return False

    def push_front(self, e):
        self.deque.insert(0, e)
        self.len += 1

    def push_back(self, e):
        self.deque.insert(self.len, e)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.len -= 1
            return self.deque.pop(0)

    def pop_back(self):
        if not self.empty():
            self.len -= 1
            return self.deque.pop(self.len)

    def front(self):
        if not self.empty():
            return self.deque[0]

    def back(self):
        if not self.empty():
            return self.deque[-1]

    def show(self):
        for i in self.deque:
            print(i, end=' ')
        print()


if __name__ == '__main__':
    d = Deque()
    d.push_front(10)  # 10
    d.show()
    d.push_front(5)  # 5 10
    d.show()
    d.push_back(20)  # 5 10 20
    d.show()
    d.push_front(7)  # 7 5 10 20
    d.show()
    d.push_back(40)  # 7 5 10 20 40
    print('front: {}'.format(d.front()))
    print('back: {}'.format(d.back()))
    d.show()
    d.pop_back()  # 7 5 10 20
    d.show()
    d.pop_back()  # 7 5 10
    d.show()
    d.pop_front()  # 5 10
    d.show()
    print('front: {}'.format(d.front()))
    print('back: {}'.format(d.back()))
