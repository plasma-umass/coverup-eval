# file typesystem/unique.py:20-22
# lines [20, 21, 22]
# branches []

import pytest
from typesystem.unique import Uniqueness

class TestUniqueness:
    def test_uniqueness_contains(self, mocker):
        # Mock the make_hashable method to return the item itself if it's 'test_item'
        # and a different value for other items to simulate the hashable conversion
        def make_hashable_side_effect(item):
            return 'test_item' if item == 'test_item' else 'different_value'
        mocker.patch.object(Uniqueness, 'make_hashable', side_effect=make_hashable_side_effect)
        
        # Create an instance of Uniqueness and add an item to the internal set
        uniqueness = Uniqueness()
        uniqueness._set = set()  # Initialize the internal set
        uniqueness._set.add('test_item')  # Add an item to the set
        
        # Test the __contains__ method
        assert 'test_item' in uniqueness  # Should return True because 'test_item' is in the set
        assert 'nonexistent_item' not in uniqueness  # Should return False because 'nonexistent_item' is not in the set

        # Verify that make_hashable was called for both checks
        assert Uniqueness.make_hashable.call_count == 2
        Uniqueness.make_hashable.assert_any_call('test_item')
        Uniqueness.make_hashable.assert_any_call('nonexistent_item')
