# file src/blib2to3/pytree.py:63-80
# lines [63, 65, 75, 76, 77, 78, 79]
# branches []

import pytest
from blib2to3.pytree import Base
from typing import Optional, List

class TestBase(Base):
    def __init__(self, type: int, children: Optional[List] = None):
        self.type = type
        self.children = children if children is not None else []

def test_base_initialization():
    node_type = 999
    test_node = TestBase(node_type)
    assert test_node.type == node_type
    assert test_node.parent is None
    assert test_node.children == []
    assert not test_node.was_changed
    assert not test_node.was_checked
