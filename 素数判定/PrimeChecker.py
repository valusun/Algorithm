from math import sqrt


def isPrime(n: int) -> bool:
    """引数の素数判定を行う

    Args:
        n (int): 数値

    Returns:
        bool: 素数ならばtrue
    """

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def SieveEratosthenes(n: int) -> list[int]:
    """インデックス番号が素数の箇所を1としたリストを生成する

    Args:
        n (int): 上限

    Returns:
        primes (list[int]): 引数までの素数
    """

    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, int(n**0.5) + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes
