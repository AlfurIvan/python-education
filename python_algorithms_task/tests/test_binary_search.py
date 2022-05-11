"""Tests for binary search algorithm"""

from random import randint, choice
from binary_search import binary_search
import pytest


@pytest.mark.parametrize("test_arr", (list(set(randint(0, 30) for _ in range(30))) for _ in range(2)))
def test_binary_search(test_arr):
    """Check truth of binary search algorithm` result"""
    test_arr.sort()
    search = choice(test_arr)

    assert binary_search(test_arr, search) == test_arr.index(search)
