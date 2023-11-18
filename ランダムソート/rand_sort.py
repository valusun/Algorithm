from random import randint
from typing import TypeVar


T = TypeVar("T")


def RandomSort(arr: list[T]) -> list[T]:
    """Fisher-Yatesアルゴリズムを用いてランダムソートを行う"""

    for i in reversed(range(1, len(arr))):
        j = randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr
