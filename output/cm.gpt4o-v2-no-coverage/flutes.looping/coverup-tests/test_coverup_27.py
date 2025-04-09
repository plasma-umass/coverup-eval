# file: flutes/structure.py:74-96
# asked: {"lines": [74, 75, 82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}
# gained: {"lines": [74, 75, 82, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}

import pytest
from collections import namedtuple

# Assuming _NO_MAP_TYPES and _NO_MAP_INSTANCE_ATTR are defined somewhere in the module
_NO_MAP_TYPES = (str, bytes)
_NO_MAP_INSTANCE_ATTR = '_no_map'

from flutes.structure import map_structure

def test_map_structure_with_list():
    result = map_structure(lambda x: x + 1, [1, 2, 3])
    assert result == [2, 3, 4]

def test_map_structure_with_nested_list():
    result = map_structure(lambda x: x + 1, [1, [2, 3], 4])
    assert result == [2, [3, 4], 5]

def test_map_structure_with_tuple():
    result = map_structure(lambda x: x + 1, (1, 2, 3))
    assert result == (2, 3, 4)

def test_map_structure_with_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    point = Point(1, 2)
    result = map_structure(lambda x: x + 1, point)
    assert result == Point(2, 3)

def test_map_structure_with_dict():
    result = map_structure(lambda x: x + 1, {'a': 1, 'b': 2})
    assert result == {'a': 2, 'b': 3}

def test_map_structure_with_ordereddict():
    from collections import OrderedDict
    result = map_structure(lambda x: x + 1, OrderedDict(a=1, b=2))
    assert result == OrderedDict(a=2, b=3)

def test_map_structure_with_set():
    result = map_structure(lambda x: x + 1, {1, 2, 3})
    assert result == {2, 3, 4}

def test_map_structure_with_no_map_type():
    result = map_structure(lambda x: x + "1", "string")
    assert result == "string1"

def test_map_structure_with_no_map_instance_attr():
    class NoMap:
        _no_map = True
        def __init__(self, value):
            self.value = value

    obj = NoMap(1)
    result = map_structure(lambda x: x, obj)
    assert result == obj
