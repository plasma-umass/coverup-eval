# file flutes/structure.py:49-57
# lines [55, 56, 57]
# branches []

import pytest
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR

def test_no_map_type():
    class CustomList(list):
        pass

    # Test with a built-in type
    no_map_list_type = _no_map_type(list)
    assert no_map_list_type.__name__ == "_no_maplist"
    instance = no_map_list_type()
    assert getattr(instance, _NO_MAP_INSTANCE_ATTR) is True

    # Test with a user-defined type
    no_map_custom_list_type = _no_map_type(CustomList)
    assert no_map_custom_list_type.__name__ == "_no_mapCustomList"
    custom_instance = no_map_custom_list_type()
    assert getattr(custom_instance, _NO_MAP_INSTANCE_ATTR) is True

    # Clean up the cache to avoid side effects on other tests
    _no_map_type.cache_clear()
