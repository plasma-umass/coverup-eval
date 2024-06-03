# file src/blib2to3/pytree.py:206-218
# lines [206, 207, 212, 213, 215, 216, 217, 218]
# branches ['212->213', '212->215', '215->216', '215->217']

import pytest
from unittest.mock import Mock, create_autospec
from blib2to3.pytree import Base

class TestNode(Base):
    def __init__(self, parent=None):
        self.parent = parent

def test_prev_sibling_no_parent():
    node = TestNode()
    node.parent = None
    assert node.prev_sibling is None

def test_prev_sibling_with_parent_no_map(mocker):
    node = TestNode()
    parent = Mock()
    parent.prev_sibling_map = None
    node.parent = parent

    mocker.patch.object(parent, 'update_sibling_maps', autospec=None)
    parent.update_sibling_maps.side_effect = lambda: setattr(parent, 'prev_sibling_map', {id(node): None})

    assert node.prev_sibling is None
    parent.update_sibling_maps.assert_called_once()

def test_prev_sibling_with_parent_and_map():
    node = TestNode()
    sibling = TestNode()
    parent = Mock()
    parent.prev_sibling_map = {id(node): sibling}
    node.parent = parent

    assert node.prev_sibling is sibling
