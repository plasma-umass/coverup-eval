# file pysnooper/variables.py:111-121
# lines [115, 118, 119, 120, 121]
# branches []

import pytest
from unittest.mock import patch
from pysnooper.variables import Indices, BaseVariable

class MockSource:
    def __str__(self):
        return "mock_source"

def test_indices_keys():
    mock_source = MockSource()
    indices = Indices(str(mock_source))
    main_value = [1, 2, 3, 4, 5]
    
    # Test _keys method
    keys = indices._keys(main_value)
    assert list(keys) == list(range(len(main_value)))
    
    # Test __getitem__ method with a slice
    sliced_indices = indices[slice(1, 3)]
    assert isinstance(sliced_indices, Indices)
    assert sliced_indices._slice == slice(1, 3)
    
    # Ensure the original indices object is not modified
    assert indices._slice == slice(None)
    
    # Test _keys method with the sliced indices
    sliced_keys = sliced_indices._keys(main_value)
    assert list(sliced_keys) == list(range(len(main_value)))[1:3]
