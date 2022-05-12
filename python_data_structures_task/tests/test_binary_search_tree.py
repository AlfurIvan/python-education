import pytest
from ds_binary_search_tree import BinarySearchTree

ROOT = 50


@pytest.fixture()
def fix_bst():
    fix_bst = BinarySearchTree(ROOT)
    return fix_bst


@pytest.mark.parametrize("value",
                         [65, 43, 50, 14])
def test_insert(fix_bst, value):
    fix_bst.insert(value)
    if value < ROOT:
        assert fix_bst.root.left.value == value
    else:
        assert fix_bst.root.right.value == value


@pytest.mark.parametrize("values",
                         [(65, 43, 50, 14)])
def test_lookup_search(fix_bst, values):
    for val in values:
        fix_bst.insert(val)
    assert fix_bst.lookup(43).value == 43


@pytest.mark.parametrize("values",
                         [(65, 43, 57, 14)])
def test_delete_rebuild(fix_bst, values):
    for val in values:
        fix_bst.insert(val)
    fix_bst.delete(43)
    assert fix_bst.root.left.value != 43
