# file src/blib2to3/pytree.py:320-327
# lines [325, 326, 327]
# branches ['325->326', '325->327']

import pytest
from blib2to3.pytree import Node, Leaf
from blib2to3.pgen2 import token

def test_node_prefix_no_children():
    node = Node(type=256, children=[])
    assert node.prefix == ""

def test_node_prefix_with_children(mocker):
    child = Leaf(type=token.NAME, value="child")
    child.prefix = " "
    node = Node(type=256, children=[child])
    assert node.prefix == " "
