from math import sqrt


def is_prime(n):
    """`n`が素数かどうかを判定する"""

    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
