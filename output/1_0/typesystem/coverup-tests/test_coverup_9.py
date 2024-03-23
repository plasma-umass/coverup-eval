# file typesystem/unique.py:15-18
# lines [15, 16, 17, 18]
# branches ['17->exit', '17->18']

import pytest
from typesystem.unique import Uniqueness

def test_uniqueness_initialization_with_items():
    # Test initialization with a list of items
    items = [1, 2, 3, 3, 2, 1]
    uniqueness = Uniqueness(items)
    assert len(uniqueness._set) == 3, "Uniqueness should have 3 unique items"
    assert all(item in uniqueness._set for item in set(items)), "All unique items should be in the Uniqueness set"

def test_uniqueness_initialization_without_items():
    # Test initialization without providing items
    uniqueness = Uniqueness()
    assert len(uniqueness._set) == 0, "Uniqueness should be initialized with an empty set"
