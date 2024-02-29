def knapsack(W, weights, values, n):
    # Базовый случай
    if n == 0 or W == 0:
        return 0

    if (weights[n-1] > W):
        return knapsack(W, weights, values, n-1)

    else:
        return max(values[n-1] + knapsack(W - weights[n-1], weights, values, n-1), knapsack(W, weights, values, n-1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    n = len(values)
    print(knapsack(W, weights, values, n))