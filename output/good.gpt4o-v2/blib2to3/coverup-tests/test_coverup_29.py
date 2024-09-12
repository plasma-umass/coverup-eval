# file: src/blib2to3/pytree.py:229-238
# asked: {"lines": [229, 234, 235, 236, 237, 238], "branches": [[235, 236], [235, 237]]}
# gained: {"lines": [229, 234, 235, 236, 237, 238], "branches": [[235, 236], [235, 237]]}

import pytest
from unittest.mock import Mock

from blib2to3.pytree import Base

class TestableBase(Base):
    def __init__(self, next_sibling=None):
        self._next_sibling = next_sibling

    @property
    def next_sibling(self):
        return self._next_sibling

def test_get_suffix_with_next_sibling():
    # Create a mock next_sibling with a prefix
    mock_next_sibling = Mock()
    mock_next_sibling.prefix = 'suffix'

    # Create an instance of TestableBase and set the next_sibling property
    base_instance = TestableBase(next_sibling=mock_next_sibling)

    # Call get_suffix and assert the result
    assert base_instance.get_suffix() == 'suffix'

def test_get_suffix_without_next_sibling():
    # Create an instance of TestableBase with no next_sibling
    base_instance = TestableBase(next_sibling=None)

    # Call get_suffix and assert the result
    assert base_instance.get_suffix() == ''
