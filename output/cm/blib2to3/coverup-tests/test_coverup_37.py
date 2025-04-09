# file src/blib2to3/pytree.py:465-470
# lines [465, 466, 470]
# branches []

import pytest
from blib2to3.pytree import Leaf

def test_leaf_prefix_property():
    leaf = Leaf(type=0, value='', context=('', (1, 0)))
    leaf._prefix = " "
    assert leaf.prefix == " ", "The prefix property should return the correct whitespace"
