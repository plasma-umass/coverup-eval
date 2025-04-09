# file: flutes/structure.py:49-57
# asked: {"lines": [55, 56, 57], "branches": []}
# gained: {"lines": [55, 56, 57], "branches": []}

import pytest
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR

def test_no_map_type():
    class CustomList(list):
        pass

    # Test with a custom list type
    new_type = _no_map_type(CustomList)
    assert issubclass(new_type, CustomList)
    assert getattr(new_type(), _NO_MAP_INSTANCE_ATTR) is True

    # Test with a built-in list type
    new_type = _no_map_type(list)
    assert issubclass(new_type, list)
    assert getattr(new_type(), _NO_MAP_INSTANCE_ATTR) is True

    # Ensure the cache is working by calling it again and checking the same type is returned
    cached_type = _no_map_type(list)
    assert cached_type is new_type
