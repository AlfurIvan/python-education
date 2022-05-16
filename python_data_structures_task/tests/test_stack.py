import pytest
from ds_stack import Stack


@pytest.fixture()
def stack_ex():
    """Stack fixture"""
    stack_ex = Stack()
    return stack_ex


@pytest.mark.parametrize("value",
                         [70, 6, 8, "bruh"])
def test_push(stack_ex, value):
    """Check addition an element to the beginning of the stack"""
    stack_ex.push_item("some")
    stack_ex.push_item("WOW! another some(")
    before = stack_ex._list_length()
    stack_ex.push_item(value)
    assert stack_ex.peek_item() == value \
           and stack_ex._list_length() - before == 1


def test_peek(stack_ex):
    """Check searching (lookup_by_index)"""
    stack_ex.push_item("some")
    stack_ex.push_item("some2")
    assert stack_ex.peek_item() == "some2"


def test_delete(stack_ex):
    """Check did the stack get less after deletion"""
    stack_ex.push_item("some")
    stack_ex.push_item("another some")
    stack_ex.push_item("another some2")
    stack_ex.push_item("ome more some")
    before = stack_ex._list_length()
    stack_ex.pop_item()
    assert before - stack_ex._list_length() == 1
