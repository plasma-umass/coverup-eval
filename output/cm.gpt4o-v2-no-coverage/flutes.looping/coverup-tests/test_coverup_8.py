# file: flutes/structure.py:49-57
# asked: {"lines": [49, 50, 55, 56, 57], "branches": []}
# gained: {"lines": [49, 50, 55, 56, 57], "branches": []}

import pytest
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR

def test_no_map_type():
    # Test with a built-in type
    new_list_type = _no_map_type(list)
    assert new_list_type.__name__ == '_no_maplist'
    assert issubclass(new_list_type, list)
    assert getattr(new_list_type(), _NO_MAP_INSTANCE_ATTR) is True

    # Test with a user-defined type
    class CustomType:
        pass

    new_custom_type = _no_map_type(CustomType)
    assert new_custom_type.__name__ == '_no_mapCustomType'
    assert issubclass(new_custom_type, CustomType)
    assert getattr(new_custom_type(), _NO_MAP_INSTANCE_ATTR) is True

    # Test cache functionality
    assert _no_map_type(list) is new_list_type
    assert _no_map_type(CustomType) is new_custom_type

    # Clean up the cache to avoid state pollution
    _no_map_type.cache_clear()
