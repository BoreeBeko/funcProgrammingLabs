def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Example usage:
n = 100
print("Prime numbers up to", n, "are:")
prime_gen = prime_generator()
for _ in range(n):
    print(next(prime_gen), end=" ")
