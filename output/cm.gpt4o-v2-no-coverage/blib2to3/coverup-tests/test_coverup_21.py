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

@pytest.fixture
def base_instance():
    return TestableBase()

def test_get_suffix_no_next_sibling(base_instance):
    base_instance._next_sibling = None
    assert base_instance.get_suffix() == ""

def test_get_suffix_with_next_sibling(base_instance):
    next_sibling_mock = Mock()
    next_sibling_mock.prefix = "test_prefix"
    base_instance._next_sibling = next_sibling_mock
    assert base_instance.get_suffix() == "test_prefix"
