# file: flutes/structure.py:49-57
# asked: {"lines": [49, 50, 55, 56, 57], "branches": []}
# gained: {"lines": [49, 50, 55, 56, 57], "branches": []}

import pytest
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR

def test_no_map_type_creates_subtype():
    class CustomList(list):
        pass

    # Test with built-in type
    no_map_list = _no_map_type(list)
    assert issubclass(no_map_list, list)
    assert getattr(no_map_list(), _NO_MAP_INSTANCE_ATTR, False) is True

    # Test with user-defined type
    no_map_custom_list = _no_map_type(CustomList)
    assert issubclass(no_map_custom_list, CustomList)
    assert getattr(no_map_custom_list(), _NO_MAP_INSTANCE_ATTR, False) is True

    # Ensure the cache is working by checking the same type is returned
    assert _no_map_type(list) is no_map_list
    assert _no_map_type(CustomList) is no_map_custom_list

@pytest.fixture(autouse=True)
def clear_lru_cache():
    _no_map_type.cache_clear()
    yield
    _no_map_type.cache_clear()
