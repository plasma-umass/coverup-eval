# file: flutes/structure.py:49-57
# asked: {"lines": [49, 50, 55, 56, 57], "branches": []}
# gained: {"lines": [49, 50, 55, 56, 57], "branches": []}

import pytest
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR

def test_no_map_type_with_list():
    # Test with list type
    new_list_type = _no_map_type(list)
    assert new_list_type.__name__ == '_no_maplist'
    assert issubclass(new_list_type, list)
    instance = new_list_type()
    assert getattr(instance, _NO_MAP_INSTANCE_ATTR) is True

def test_no_map_type_with_dict():
    # Test with dict type
    new_dict_type = _no_map_type(dict)
    assert new_dict_type.__name__ == '_no_mapdict'
    assert issubclass(new_dict_type, dict)
    instance = new_dict_type()
    assert getattr(instance, _NO_MAP_INSTANCE_ATTR) is True

def test_no_map_type_cache():
    # Test the caching behavior
    new_list_type_1 = _no_map_type(list)
    new_list_type_2 = _no_map_type(list)
    assert new_list_type_1 is new_list_type_2

    new_dict_type_1 = _no_map_type(dict)
    new_dict_type_2 = _no_map_type(dict)
    assert new_dict_type_1 is new_dict_type_2
