# file: src/blib2to3/pytree.py:472-475
# asked: {"lines": [472, 473, 474, 475], "branches": []}
# gained: {"lines": [472, 473, 474, 475], "branches": []}

import pytest
from blib2to3.pytree import Leaf

def test_leaf_prefix_setter():
    leaf = Leaf(type=1, value="value")
    leaf.prefix = "new_prefix"
    assert leaf._prefix == "new_prefix"
    assert leaf.was_changed

