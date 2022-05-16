import pytest
from ds_queue import Queue


@pytest.fixture()
def queue_ex():
    """Queue_ex fixture"""
    stack_ex = Queue()
    return stack_ex


@pytest.mark.parametrize("value",
                         [70, 6, 8, "bruh"])
def test_enqueue_item(queue_ex, value):
    """Check addition an element to the beginning of the queue"""
    queue_ex.enqueue_item(value)
    queue_ex.enqueue_item("WOW! another some(")
    before = queue_ex._list_length()
    queue_ex.enqueue_item("some")
    assert queue_ex.peek_item() == value \
           and queue_ex._list_length() - before == 1


def test_peek(queue_ex):
    """Check searching (lookup_by_index)"""
    queue_ex.enqueue_item("some")
    queue_ex.enqueue_item("some2")
    assert queue_ex.peek_item() == "some"


def test_dequeue_item(queue_ex):
    """Check did the queue get less after deletion"""
    queue_ex.enqueue_item("some")
    queue_ex.enqueue_item("another some")
    queue_ex.enqueue_item("another some2")
    queue_ex.enqueue_item("ome more some")
    before = queue_ex._list_length()
    queue_ex.dequeue_item()
    assert before - queue_ex._list_length() == 1
