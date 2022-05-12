"""Tests for Graph class"""

import pytest
from ds_graph import Graph
from ds_linked_list import SingleLinkedList


@pytest.fixture()
def fixture_graph():
    """Create Graph object"""
    return Graph()


def test_insert(fixture_graph):
    """Test insert method"""
    fixture_graph.insert()
    assert fixture_graph.vertices[0].value == 0


def test_add_neighbours_edges(fixture_graph):
    """Check the addition of the neighbors and the formation of edges"""
    fixture_graph.insert()
    ex = SingleLinkedList()
    ex.append_item(0)
    fixture_graph.insert(ex)
    assert fixture_graph.vertices.length == 2 \
           and fixture_graph.vertices[1].neighbours.length == 1 \
           and fixture_graph.edges.length == 1


def test_lookup(fixture_graph):
    """Check lookup function"""
    fixture_graph.insert()
    ex = SingleLinkedList()
    ex.append_item(0)
    fixture_graph.insert(ex)
    assert fixture_graph.lookup(0) == fixture_graph.vertices[0] \
           and fixture_graph.lookup(1) == fixture_graph.vertices[1]


def test_delete(fixture_graph):
    """
    Check the removal of nodes, edges with them and the removal
    of these nodes from the list of neighbours of other nodes
    """
    fixture_graph.insert()
    ex = SingleLinkedList()
    ex.append_item(0)
    fixture_graph.insert(ex)
    node = fixture_graph.vertices[0]
    fixture_graph.delete(node)
    assert fixture_graph.vertices[0].neighbours.length == 0 \
           and fixture_graph.vertices.length == 1 \
           and fixture_graph.edges.length == 0
