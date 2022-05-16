"""Tests fot Hash Table class"""

import pytest
from ds_hash_table import HashTable


@pytest.fixture(name="hash_ex")
def fix_hash_ex():
    """Create HashTable object"""
    return HashTable()


@pytest.mark.parametrize("string, expected",
                         [("look", 17),
                          ("book", 7),
                          ("game", 20)])
def test_hash(hash_ex, string, expected):
    """Check hash function"""
    assert hash_ex.hash(string) == expected


@pytest.mark.parametrize("string, expected",
                         [("look", 17),
                          ("book", 7),
                          ("game", 20)])
def test_insert_empty(hash_ex, string, expected):
    """Check insert into empty cell"""
    hash_ex.insert(string, string)
    assert hash_ex.table[expected] is not None


def test_insert_list(hash_ex):
    """
    Check insert into occupied cell: a linked list
    should be created with all nodes with this key
    """
    hash_ex.insert("some", 23)
    hash_ex.insert("some2", 34)
    hash_ex.insert("some3", 45)
    assert hash_ex.table[9].length == 3


@pytest.mark.parametrize("string, value, expected",
                         [("look", 1, 17),
                          ("book", 2, 7),
                          ("game", 3, 20)])
def test_lookup(hash_ex, string, value, expected):
    """Check searching for a value in a cell that has only one node"""
    hash_ex.insert(string, value)
    assert hash_ex.lookup(string) == value


def test_lookup_list(hash_ex):
    """Check searching for a value in a cell that has linked list with nodes"""
    hash_ex.insert("some", 23)
    hash_ex.insert("some2", 34)
    hash_ex.insert("some3", 45)
    assert hash_ex.lookup("some2") == 34


def test_delete_list(hash_ex):
    """Check deleting for a value in a cell that has linked list with nodes"""
    hash_ex.insert("some", 23)
    hash_ex.insert("some2", 34)
    hash_ex.insert("some3", 45)
    hash_ex.delete("some")
    assert hash_ex.lookup("some") is None
