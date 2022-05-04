import pytest
from to_test import even_odd, sum_all, time_of_day
from datetime import datetime


@pytest.mark.parametrize("test_input, expected",
                         [(4, "even"), (64, "even"),
                          (-246, "even"), (0, "even"),
                          (-1, "odd"), (-141, "odd"),
                          (7, "odd"), (33, "odd")])
def test_even_odd(test_input, expected):
    assert even_odd(test_input) == expected


@pytest.mark.parametrize("args",
                         [(0, 0, 0, 0, 0),
                          (7, 0, 0, 0, 0),
                          (5, 77, 32, 56, 8),
                          (5, -77, 56, -32, 0)])
def test_sum_all(args):

    assert sum_all(*args) == sum([*args])


@pytest.fixture
def fix_time_of_day():
    now = datetime.now()
    if 0 <= now.hour < 6:
        return "night"
    if 6 <= now.hour < 12:
        return "morning"
    if 12 <= now.hour < 18:
        return "afternoon"
    return "evening"


def test_time_of_day(fix_time_of_day):
    assert time_of_day() == fix_time_of_day
