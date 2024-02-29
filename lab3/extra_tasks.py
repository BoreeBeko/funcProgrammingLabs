def fact_rec(n):
    if n == 0:
        return 1
    else:
        return n * fact_rec(n-1)


def fact_tailrec(n, result=1):
    if n == 0:
        return result
    else:
        return fact_tailrec(n-1, result*n)

