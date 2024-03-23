# file typesystem/unique.py:24-26
# lines [24, 25, 26]
# branches []

import pytest
import typing
from typesystem.unique import Uniqueness

class TestUniqueness:
    def test_add(self, mocker):
        # Mock the make_hashable method to return the item itself
        mocker.patch.object(Uniqueness, 'make_hashable', return_value='mocked_item')
        
        # Create an instance of Uniqueness
        uniqueness = Uniqueness()
        # Manually add the _set attribute since it's not defined in the provided code snippet
        uniqueness._set = set()
        
        # Call the add method
        uniqueness.add('item')
        
        # Assert that make_hashable was called with 'item'
        Uniqueness.make_hashable.assert_called_once_with('item')
        # Assert that 'mocked_item' was added to the _set
        assert 'mocked_item' in uniqueness._set
