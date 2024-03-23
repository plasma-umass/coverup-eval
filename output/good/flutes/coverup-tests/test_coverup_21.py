# file flutes/structure.py:99-127
# lines [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127]
# branches ['113->114', '113->115', '115->116', '115->117', '117->118', '117->122', '118->119', '118->121', '122->124', '122->125', '125->126', '125->127']

import pytest
from flutes.structure import map_structure_zip
from collections import namedtuple, OrderedDict

def test_map_structure_zip_with_namedtuple():
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(x=1, y=2)
    p2 = Point(x=3, y=4)
    result = map_structure_zip(lambda a, b: a + b, [p1, p2])
    assert result == Point(x=4, y=6)

def test_map_structure_zip_with_ordered_dict():
    d1 = OrderedDict([('a', 1), ('b', 2)])
    d2 = OrderedDict([('a', 3), ('b', 4)])
    result = map_structure_zip(lambda a, b: a + b, [d1, d2])
    assert result == OrderedDict([('a', 4), ('b', 6)])

def test_map_structure_zip_with_set():
    s1 = {1, 2}
    s2 = {3, 4}
    with pytest.raises(ValueError):
        map_structure_zip(lambda a, b: a + b, [s1, s2])

def test_map_structure_zip_with_no_map_type():
    class NoMapType:
        pass

    obj1 = NoMapType()
    obj2 = NoMapType()
    result = map_structure_zip(lambda a, b: (a, b), [obj1, obj2])
    assert result == (obj1, obj2)

def test_map_structure_zip_with_no_map_instance_attr():
    class NoMapInstance:
        _no_map = True

    obj1 = NoMapInstance()
    obj2 = NoMapInstance()
    result = map_structure_zip(lambda a, b: (a, b), [obj1, obj2])
    assert result == (obj1, obj2)

# Register the tests for pytest
def test_suite():
    test_map_structure_zip_with_namedtuple()
    test_map_structure_zip_with_ordered_dict()
    test_map_structure_zip_with_set()
    test_map_structure_zip_with_no_map_type()
    test_map_structure_zip_with_no_map_instance_attr()
