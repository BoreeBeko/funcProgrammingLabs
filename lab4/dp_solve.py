def knapsack_dp(W, weights, values, n):
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    if weights[n-1] <= W:
        t[n][W] = max(values[n-1] + knapsack_dp(W - weights[n-1], weights, values, n-1),
                      knapsack_dp(W, weights, values, n-1))
        return t[n][W]
    elif weights[n-1] > W:
        t[n][W] = knapsack_dp(W, weights, values, n-1)
        return t[n][W]


if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    n = len(values)

    # We initialize the matrix with -1 at first.
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    print(knapsack_dp(W, weights, values, n))
    print(t)