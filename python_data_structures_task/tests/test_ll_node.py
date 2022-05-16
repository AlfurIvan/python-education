from _ds_scratch_ll_s_q import Node
import pytest

VALUE = 1000


@pytest.fixture()
def fix_node():
    fix_node = Node(VALUE)
    return fix_node


def test_has_value(fix_node):
    """method to compare the value with the node data"""
    assert fix_node.data == VALUE
