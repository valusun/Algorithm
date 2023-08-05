import pytest
from .. import prime, primes


@pytest.mark.parametrize(
    "args, result",
    [
        (0, False),
        (1, False),
        (2, True),
        (11, True),
        (10**9, False),
        (10**9 + 7, True),
        (998244353, True),
    ],
)
def test_prime(args, result):
    assert prime.is_prime(args) == result


@pytest.fixture(scope="module")
def _primes():
    # 毎回生成するのは重いため
    return primes.get_primes(10**6)


@pytest.mark.parametrize(
    "args, result",
    [(0, False), (1, False), (2, True), (11, True), (99991, True), (99993, False)],
)
def test_primes(args, result, _primes):
    # 配列を生成する関係上、大きな値を入れられないデメリットがある
    assert _primes[args] == result
