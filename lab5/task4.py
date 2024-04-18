def decorator():
    cache = {}

    def fibonacci(n):
        if n < 2:
            cache[n] = 1
        if n not in cache:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]


    n = 0
    while True:
        yield fibonacci(n)
        n += 1


