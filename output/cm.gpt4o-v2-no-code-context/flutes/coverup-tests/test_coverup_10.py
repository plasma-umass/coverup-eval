# file: flutes/structure.py:49-57
# asked: {"lines": [49, 50, 55, 56, 57], "branches": []}
# gained: {"lines": [49, 50, 55, 56, 57], "branches": []}

import pytest
from flutes.structure import _no_map_type, _NO_MAP_INSTANCE_ATTR
from functools import lru_cache

def test_no_map_type_list():
    # Test with list type
    new_type = _no_map_type(list)
    assert issubclass(new_type, list)
    instance = new_type()
    assert getattr(instance, _NO_MAP_INSTANCE_ATTR) is True

def test_no_map_type_dict():
    # Test with dict type
    new_type = _no_map_type(dict)
    assert issubclass(new_type, dict)
    instance = new_type()
    assert getattr(instance, _NO_MAP_INSTANCE_ATTR) is True

def test_no_map_type_set():
    # Test with set type
    new_type = _no_map_type(set)
    assert issubclass(new_type, set)
    instance = new_type()
    assert getattr(instance, _NO_MAP_INSTANCE_ATTR) is True

def test_no_map_type_tuple():
    # Test with tuple type
    new_type = _no_map_type(tuple)
    assert issubclass(new_type, tuple)
    instance = new_type()
    assert getattr(instance, _NO_MAP_INSTANCE_ATTR) is True

@pytest.fixture(autouse=True)
def clear_lru_cache():
    # Clear the LRU cache before each test to avoid state pollution
    _no_map_type.cache_clear()
    yield
    _no_map_type.cache_clear()
