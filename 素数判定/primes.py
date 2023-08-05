from math import sqrt


def get_primes(n):
    """エラトステネスの篩を用いて素数を列挙する"""

    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, int(sqrt(n)) + 1, 2):
        if primes[p] == 0:
            continue
        for q in range(p * p, n + 1, p * 2):
            primes[q] = 0
    return primes
