"""Test for iterative quicksort impl."""

from random import randint
from quick_sort import quick_sort
import pytest


@pytest.mark.parametrize("test_arr", ([randint(-100, 100) for _ in range(50)] for _ in range(20)))
def test_quick_sort(test_arr):
    """Compares the result of my quick sort function and the built-in function sort"""
    assert quick_sort(test_arr) == test_arr.sort()
