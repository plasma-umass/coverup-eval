# file: flutes/structure.py:74-96
# asked: {"lines": [74, 75, 82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}
# gained: {"lines": [74, 75, 82, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}

import pytest
from collections import namedtuple
from flutes.structure import map_structure, _NO_MAP_INSTANCE_ATTR

def test_map_structure_no_map_instance_attr(monkeypatch):
    class NoMap:
        _NO_MAP_INSTANCE_ATTR = True

    def fn(x):
        if isinstance(x, NoMap):
            return x
        return x * 2

    obj = NoMap()
    result = map_structure(fn, obj)
    assert result == obj

def test_map_structure_list():
    def fn(x):
        return x * 2

    obj = [1, 2, 3]
    result = map_structure(fn, obj)
    assert result == [2, 4, 6]

def test_map_structure_tuple():
    def fn(x):
        return x * 2

    obj = (1, 2, 3)
    result = map_structure(fn, obj)
    assert result == (2, 4, 6)

def test_map_structure_namedtuple():
    def fn(x):
        return x * 2

    Point = namedtuple('Point', ['x', 'y'])
    obj = Point(1, 2)
    result = map_structure(fn, obj)
    assert result == Point(2, 4)

def test_map_structure_dict():
    def fn(x):
        return x * 2

    obj = {'a': 1, 'b': 2}
    result = map_structure(fn, obj)
    assert result == {'a': 2, 'b': 4}

def test_map_structure_set():
    def fn(x):
        return x * 2

    obj = {1, 2, 3}
    result = map_structure(fn, obj)
    assert result == {2, 4, 6}

def test_map_structure_default():
    def fn(x):
        return x * 2

    obj = 5
    result = map_structure(fn, obj)
    assert result == 10
