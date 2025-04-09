# file: src/blib2to3/pytree.py:465-470
# asked: {"lines": [465, 466, 470], "branches": []}
# gained: {"lines": [465, 466, 470], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_prefix_getter():
    leaf = Leaf(type=1, value="value", prefix=" ")
    assert leaf.prefix == " "

def test_leaf_prefix_setter():
    leaf = Leaf(type=1, value="value")
    leaf.prefix = " "
    assert leaf.prefix == " "
