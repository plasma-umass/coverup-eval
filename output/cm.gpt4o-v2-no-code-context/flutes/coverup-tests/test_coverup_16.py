# file: flutes/structure.py:99-127
# asked: {"lines": [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 114], [113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}
# gained: {"lines": [99, 100, 112, 113, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127], "branches": [[113, 115], [115, 116], [115, 117], [117, 118], [117, 122], [118, 119], [118, 121], [122, 124], [122, 125], [125, 126], [125, 127]]}

import pytest
from flutes.structure import map_structure_zip

def test_map_structure_zip_no_map_types():
    class NoMapType:
        pass

    obj = NoMapType()
    objs = [obj, obj]
    result = map_structure_zip(lambda x, y: x is y, objs)
    assert result is True

def test_map_structure_zip_list():
    objs = [[1, 2, 3], [4, 5, 6]]
    result = map_structure_zip(lambda x, y: x + y, objs)
    assert result == [5, 7, 9]

def test_map_structure_zip_tuple():
    objs = [(1, 2, 3), (4, 5, 6)]
    result = map_structure_zip(lambda x, y: x + y, objs)
    assert result == (5, 7, 9)

def test_map_structure_zip_namedtuple():
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    objs = [Point(1, 2), Point(3, 4)]
    result = map_structure_zip(lambda x, y: x + y, objs)
    assert result == Point(4, 6)

def test_map_structure_zip_dict():
    objs = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
    result = map_structure_zip(lambda x, y: x + y, objs)
    assert result == {'a': 4, 'b': 6}

def test_map_structure_zip_ordered_dict():
    from collections import OrderedDict
    objs = [OrderedDict(a=1, b=2), OrderedDict(a=3, b=4)]
    result = map_structure_zip(lambda x, y: x + y, objs)
    assert result == OrderedDict(a=4, b=6)

def test_map_structure_zip_set():
    objs = [{1, 2, 3}, {4, 5, 6}]
    with pytest.raises(ValueError, match="Structures cannot contain `set` because it's unordered"):
        map_structure_zip(lambda x, y: x + y, objs)

def test_map_structure_zip_default():
    objs = [1, 2]
    result = map_structure_zip(lambda x, y: x + y, objs)
    assert result == 3
