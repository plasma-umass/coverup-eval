# file: flutes/structure.py:99-127
# asked: {"lines": [112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 114], [113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}
# gained: {"lines": [112, 113, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}

import pytest
from collections import namedtuple, OrderedDict

# Assuming the function map_structure_zip is imported from flutes.structure
from flutes.structure import map_structure_zip

def test_map_structure_zip_with_list():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, [[1, 2, 3], [4, 5, 6]])
    assert result == [5, 7, 9]

def test_map_structure_zip_with_tuple():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, [(1, 2, 3), (4, 5, 6)])
    assert result == (5, 7, 9)

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

def test_map_structure_zip_with_ordereddict():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, [OrderedDict(a=1, b=2), OrderedDict(a=3, b=4)])
    assert result == OrderedDict(a=4, b=6)

def test_map_structure_zip_with_no_map_types():
    def add(x, y):
        return x + y

    result = map_structure_zip(add, [1, 2])
    assert result == 3

def test_map_structure_zip_with_set():
    def add(x, y):
        return x + y

    with pytest.raises(ValueError, match="Structures cannot contain `set` because it's unordered"):
        map_structure_zip(add, [set([1, 2]), set([3, 4])])
