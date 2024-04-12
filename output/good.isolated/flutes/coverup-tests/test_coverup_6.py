# file flutes/structure.py:49-57
# lines [49, 50, 55, 56, 57]
# branches []

import pytest
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR

def test_no_map_type():
    # Test the _no_map_type function for a built-in type like list
    NoMapList = _no_map_type(list)
    no_map_list_instance = NoMapList()

    # Assert that the new type is a subclass of the original
    assert issubclass(NoMapList, list)
    # Assert that the instance has the special attribute set to True
    assert getattr(no_map_list_instance, _NO_MAP_INSTANCE_ATTR) == True

    # Clean up the cache to not affect other tests
    _no_map_type.cache_clear()
