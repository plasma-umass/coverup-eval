# file: src/blib2to3/pytree.py:177-190
# asked: {"lines": [177, 182, 183, 184, 185, 186, 187, 188, 189, 190], "branches": [[182, 183], [182, 190], [183, 184], [183, 190], [184, 183], [184, 185]]}
# gained: {"lines": [177, 182, 183, 184, 185, 186, 187, 188, 189, 190], "branches": [[182, 183], [182, 190], [183, 184], [184, 185]]}

import pytest
from unittest.mock import Mock

from blib2to3.pytree import Base

class TestBase(Base):
    def __init__(self):
        self.parent = None

@pytest.fixture
def base_with_parent():
    parent = Mock()
    parent.children = []
    base = TestBase()
    base.parent = parent
    parent.children.append(base)
    return base, parent

def test_remove_node_with_parent(base_with_parent):
    base, parent = base_with_parent
    assert base in parent.children
    position = base.remove()
    assert position == 0
    assert base not in parent.children
    parent.changed.assert_called_once()
    parent.invalidate_sibling_maps.assert_called_once()
    assert base.parent is None

def test_remove_node_without_parent():
    base = TestBase()
    assert base.remove() is None
