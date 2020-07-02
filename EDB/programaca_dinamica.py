from _datetime import datetime


N = 50
mem = [-1 for i in range(N)]
mem[0] = mem[1] = 1


def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_pd(n):
    if mem[n - 1] != - 1:
        return mem[n - 1]
    mem[n - 1] = fib_pd(n - 1) + fib_pd(n - 2)
    return mem[n - 1]


inicio = datetime.now()
print(fib_pd(N))
fim = datetime.now()
print(fim - inicio)

inicio = datetime.now()
print(fib(N))
fim = datetime.now()
print(fim - inicio)
