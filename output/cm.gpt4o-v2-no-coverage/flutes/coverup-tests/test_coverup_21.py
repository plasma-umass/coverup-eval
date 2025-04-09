# file: flutes/structure.py:99-127
# asked: {"lines": [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 114], [113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}
# gained: {"lines": [99, 100, 112, 113, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}

import pytest
from collections import namedtuple

# Assuming _NO_MAP_TYPES and _NO_MAP_INSTANCE_ATTR are defined somewhere in the module
_NO_MAP_TYPES = (str, bytes)
_NO_MAP_INSTANCE_ATTR = '_no_map'

from flutes.structure import map_structure_zip

def test_map_structure_zip_with_list():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, [[1, 2], [3, 4]])
    assert result == [4, 6]

def test_map_structure_zip_with_tuple():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, [(1, 2), (3, 4)])
    assert result == (4, 6)

def test_map_structure_zip_with_namedtuple():
    def add(x, y):
        return x + y

    Point = namedtuple('Point', ['x', 'y'])
    result = map_structure_zip(add, [Point(1, 2), Point(3, 4)])
    assert result == Point(4, 6)

def test_map_structure_zip_with_dict():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
    assert result == {'a': 4, 'b': 6}

def test_map_structure_zip_with_no_map_type():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, ['foo', 'bar'])
    assert result == 'foobar'

def test_map_structure_zip_with_no_map_instance_attr(monkeypatch):
    def add(x, y):
        return (x, y)

    class NoMap:
        _no_map = True

    obj1 = NoMap()
    obj2 = NoMap()
    monkeypatch.setattr(obj1, '_no_map', True)
    monkeypatch.setattr(obj2, '_no_map', True)

    result = map_structure_zip(add, [obj1, obj2])
    assert result == (obj1, obj2)

def test_map_structure_zip_with_set():
    def add(x, y):
        return x + y

    with pytest.raises(ValueError, match="Structures cannot contain `set` because it's unordered"):
        map_structure_zip(add, [set([1, 2]), set([3, 4])])
