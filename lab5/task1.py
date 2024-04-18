def infinite_arithmetic_sequence(start, step):
    current = start
    while True:
        yield current
        current += step


sequence = infinite_arithmetic_sequence(1, 1)

for _ in range(10):
    print(next(sequence))
