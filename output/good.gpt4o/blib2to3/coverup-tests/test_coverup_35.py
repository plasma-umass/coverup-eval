# file src/blib2to3/pytree.py:229-238
# lines [229, 234, 235, 236, 237, 238]
# branches ['235->236', '235->237']

import pytest
from unittest.mock import Mock

# Assuming the Base class is imported from blib2to3.pytree
from blib2to3.pytree import Base

class Derived(Base):
    def __init__(self, next_sibling=None):
        self._next_sibling = next_sibling

    @property
    def next_sibling(self):
        return self._next_sibling

    @next_sibling.setter
    def next_sibling(self, value):
        self._next_sibling = value

class TestBase:
    def test_get_suffix_with_next_sibling(self):
        # Create a mock next_sibling with a prefix
        mock_next_sibling = Mock()
        mock_next_sibling.prefix = "suffix"

        # Create an instance of Derived and set its next_sibling
        derived_instance = Derived(next_sibling=mock_next_sibling)

        # Call get_suffix and assert the result
        result = derived_instance.get_suffix()
        assert result == "suffix"

    def test_get_suffix_without_next_sibling(self):
        # Create an instance of Derived with no next_sibling
        derived_instance = Derived(next_sibling=None)

        # Call get_suffix and assert the result
        result = derived_instance.get_suffix()
        assert result == ""
