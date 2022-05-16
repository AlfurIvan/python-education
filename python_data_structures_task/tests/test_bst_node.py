import pytest
from ds_binary_search_tree import BinaryTreeNode

ROOT = 234
VALUE_L = 123
VALUE_R = 345


@pytest.fixture()
def fix_bst_node():
    fix_bst_node = BinaryTreeNode(ROOT)
    return fix_bst_node


def test_insert_l_or_r(fix_bst_node):
    """method to compare the value with the node data"""
    fix_bst_node.insert_left(VALUE_L)
    fix_bst_node.insert_right(VALUE_R)
    assert fix_bst_node.value == ROOT
    assert fix_bst_node.left.value == VALUE_L
    assert fix_bst_node.right.value == VALUE_R
