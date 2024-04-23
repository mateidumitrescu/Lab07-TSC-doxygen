import pytest
from tree import Tree

def test_find_existing_node():
    tree = Tree()
    # Adding nodes to the tree
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(1)
    tree.add(4)

    # Test finding an existing node
    result = tree.find(4)
    assert result is not None, "Should find the node"
    assert result.data == 4, "The node data should be 4"

def test_find_non_existing_node():
    tree = Tree()
    # Adding nodes to the tree
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(1)
    tree.add(4)

    # Test finding a non-existing node
    result = tree.find(10)
    assert result is None, "Should not find any node, as 10 is not in the tree"