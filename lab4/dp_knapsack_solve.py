def memoize(func):
    cache = {}

    def wrapper(W, weights, values, n):
        if (n, W) in cache:
            return cache[(n, W)]

        result = func(W, weights, values, n)

        cache[(n, W)] = result
        return result

    return wrapper

@memoize
def knapsack(W, weights, values, n):
    # Base case
    if n == 0 or W == 0:
        return 0

    if weights[n-1] > W:
        return knapsack(W, weights, values, n-1)
    else:
        included = values[n-1] + knapsack(W - weights[n-1], weights, values, n-1)
        excluded = knapsack(W, weights, values, n-1)

        return max(included, excluded)

# Example usage:
values = [60, 100, 120, 150]
weights = [10, 20, 30, 25]
W = 50
n = len(values)
result = knapsack(W, weights, values, n)
print("Maximum value that can be obtained:", result)


def sort_by_str(massive, strategy):
    pass

def observable():
    def subs():
        pass


def observer1():
    pass


def obs2():
    pass
