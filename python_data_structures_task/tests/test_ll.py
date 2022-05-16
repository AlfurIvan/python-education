import pytest
from ds_linked_list import SingleLinkedList


@pytest.fixture()
def ll_ex():
    """LinkedList fixture"""
    ll_ex = SingleLinkedList()
    return ll_ex


def test_get_item(ll_ex):
    """Checks whether an element can be retrieved by index"""
    ll_ex.append_item("some")
    assert ll_ex[0] == ll_ex[-1] == "some"


def test_set_item(ll_ex):
    """Checks can element be added by index"""
    ll_ex.append_item("some")
    ll_ex[0] = "another some"
    assert ll_ex[0] == "another some"


@pytest.mark.parametrize("value",
                         [1, 2, 3, "bruh", "bruhbruh"])
def test_prepend(ll_ex, value):
    """Check addition an element to the beginning of the list"""
    ll_ex.prepend_item("some")
    ll_ex.prepend_item("WOW! another some")
    before = ll_ex.list_length()
    ll_ex.prepend_item(value)
    assert ll_ex[0] == value \
           and ll_ex.list_length() - before == 1


@pytest.mark.parametrize("value",
                         [1, 2, 3, "bruh", "bruhbruh"])
def test_append(ll_ex, value):
    """Check addition an element to the end of the list"""
    ll_ex.append_item("some")
    ll_ex.append_item("some2")
    before = ll_ex.list_length()
    ll_ex.append_item(value)
    assert ll_ex[-1] == value \
           and ll_ex.list_length() - before == 1


def test_lookup_by_val_by_index(ll_ex):
    """Check searching _lookup_by_index _lookup_by_val"""
    ll_ex.append_item("some")
    ll_ex.append_item("some2")
    assert ll_ex.lookup("some") == 1 \
           and ll_ex.lookup("some2") == 2
    assert ll_ex.lookup_by_index(1).data == "some2"


@pytest.mark.parametrize("index, value",
                         [(1, 0)])
def test_insert(ll_ex, index, value):
    """Checks insert"""
    ll_ex.append_item("some")
    ll_ex.append_item("another some")
    ll_ex.append_item("another some2")
    ll_ex.append_item("ome more some")
    before = ll_ex.list_length()
    ll_ex.insert_item(index-1, value)
    assert ll_ex.lookup_by_index(index).data == value \
           and ll_ex.list_length() - before == 1


def test_delete(ll_ex):
    """Check did the list get less after deletion"""
    ll_ex.append_item("some")
    ll_ex.append_item("another some")
    ll_ex.append_item("another some2")
    ll_ex.append_item("ome more some")
    before = ll_ex.list_length()
    ll_ex.delete_item(1)
    assert before - ll_ex.list_length() == 1


def test_is_empty_true(ll_ex):
    """Checks if the function returns true if the list is empty"""
    assert ll_ex.is_empty() is True


def test_is_empty_false(ll_ex):
    """Checks if the function returns false if the list is not empty"""
    ll_ex.append_item("some")
    assert ll_ex.is_empty() is False

