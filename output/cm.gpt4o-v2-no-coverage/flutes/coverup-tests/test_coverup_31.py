# file: flutes/structure.py:74-96
# asked: {"lines": [82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}
# gained: {"lines": [82, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}

import pytest
from collections import namedtuple

# Assuming _NO_MAP_TYPES and _NO_MAP_INSTANCE_ATTR are defined somewhere in the module
_NO_MAP_TYPES = (str, bytes)
_NO_MAP_INSTANCE_ATTR = '_no_map'

from flutes.structure import map_structure

def test_map_structure_no_map_types():
    assert map_structure(lambda x: x.upper(), "test") == "TEST"
    assert map_structure(lambda x: x + 1, 123) == 124

def test_map_structure_no_map_instance_attr(monkeypatch):
    class NoMap:
        _no_map = True
        def __init__(self, value):
            self.value = value

    obj = NoMap(10)
    monkeypatch.setattr(obj, '_no_map', True)
    assert map_structure(lambda x: x.value + 1 if hasattr(x, 'value') else x + 1, obj) == 11

def test_map_structure_list():
    assert map_structure(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]

def test_map_structure_tuple():
    assert map_structure(lambda x: x + 1, (1, 2, 3)) == (2, 3, 4)

def test_map_structure_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    assert map_structure(lambda x: x + 1, p) == Point(2, 3)

def test_map_structure_dict():
    assert map_structure(lambda x: x + 1, {'a': 1, 'b': 2}) == {'a': 2, 'b': 3}

def test_map_structure_set():
    assert map_structure(lambda x: x + 1, {1, 2, 3}) == {2, 3, 4}
