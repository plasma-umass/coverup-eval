# file src/blib2to3/pytree.py:192-204
# lines [198, 199, 201, 202, 203, 204]
# branches ['198->199', '198->201', '201->202', '201->203']

import pytest
from unittest.mock import Mock, create_autospec

# Assuming the Base class is imported from blib2to3.pytree
from blib2to3.pytree import Base

class TestBase(Base):
    def __init__(self, parent=None):
        self._parent = parent

    @property
    def parent(self):
        return self._parent

def test_next_sibling_no_parent():
    base_instance = TestBase()
    base_instance._parent = None
    assert base_instance.next_sibling is None

def test_next_sibling_no_sibling_map(mocker):
    parent_mock = Mock()
    parent_mock.next_sibling_map = None
    parent_mock.update_sibling_maps = Mock()
    base_instance = TestBase(parent=parent_mock)

    # Mock the id function to return a consistent value
    mocker.patch('builtins.id', return_value=1234)

    # Ensure the next_sibling_map is updated after calling next_sibling
    def update_sibling_maps():
        parent_mock.next_sibling_map = {1234: 'sibling_node'}
    parent_mock.update_sibling_maps.side_effect = update_sibling_maps

    assert base_instance.next_sibling == 'sibling_node'
    parent_mock.update_sibling_maps.assert_called_once()

def test_next_sibling_with_sibling_map(mocker):
    parent_mock = Mock()
    parent_mock.next_sibling_map = {1234: 'sibling_node'}
    base_instance = TestBase(parent=parent_mock)

    # Mock the id function to return a consistent value
    mocker.patch('builtins.id', return_value=1234)

    assert base_instance.next_sibling == 'sibling_node'
    parent_mock.update_sibling_maps.assert_not_called()
