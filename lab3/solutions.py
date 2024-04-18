def fib(n):
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


print([fib(n) for n in range(1, 15)])


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


def facttail(n, acc):
    if n == 0:
        return 1
    else:
        return facttail(n-1, acc*n)
