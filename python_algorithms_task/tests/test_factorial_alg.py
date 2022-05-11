"""Test for recursive factorial impl."""

from math import factorial
from random import randint
import pytest
from factorial_alg import recursive_factorial


@pytest.mark.parametrize("num", (randint(0, 128) for _ in range(10)))
def test_recursive_factorial(num):
    """Matches my factorial impl. and the builtin math factorial"""
    assert recursive_factorial(num) == factorial(num)
