# Initiate Cache
n = 10
cache = [None] * (n+1)


def fibonacci_dp(n):

    # Edge Case
    if n == 0 or n == 1:
        return n

    # Check Cache
    if cache[n] is not None:
        return cache[n]

    # Setting Cache
    cache[n] = fibonacci_dp(n-1) + fibonacci_dp(n-2)

    # print(cache[n])
    return cache[n]


print(fibonacci_dp(10))