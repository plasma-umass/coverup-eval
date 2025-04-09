# file: flutes/structure.py:99-127
# asked: {"lines": [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 114], [113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}
# gained: {"lines": [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 114], [113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}

import pytest
from collections import namedtuple

from flutes.structure import map_structure_zip

def test_map_structure_zip_with_list():
    result = map_structure_zip(lambda x, y: x + y, [[1, 2], [3, 4]])
    assert result == [4, 6]

def test_map_structure_zip_with_tuple():
    result = map_structure_zip(lambda x, y: x + y, [(1, 2), (3, 4)])
    assert result == (4, 6)

def test_map_structure_zip_with_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    result = map_structure_zip(lambda x, y: x + y, [Point(1, 2), Point(3, 4)])
    assert result == Point(4, 6)

def test_map_structure_zip_with_dict():
    result = map_structure_zip(lambda x, y: x + y, [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
    assert result == {'a': 4, 'b': 6}

def test_map_structure_zip_with_no_map_instance_attr():
    class NoMap:
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            return NoMap(self.value + other.value)

    setattr(NoMap, '--no-map--', True)
    
    result = map_structure_zip(lambda x, y: x + y, [NoMap(1), NoMap(2)])
    assert result.value == 3

def test_map_structure_zip_with_set():
    with pytest.raises(ValueError, match="Structures cannot contain `set` because it's unordered"):
        map_structure_zip(lambda x, y: x + y, [set([1, 2]), set([3, 4])])

def test_map_structure_zip_with_no_map_types():
    class NoMapType:
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            return NoMapType(self.value + other.value)

    result = map_structure_zip(lambda x, y: x + y, [NoMapType(1), NoMapType(2)])
    assert result.value == 3
