# file: flutes/structure.py:74-96
# asked: {"lines": [82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}
# gained: {"lines": [82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}

import pytest
from collections import namedtuple

from flutes.structure import map_structure

def test_map_structure_no_map_types(monkeypatch):
    class NoMapType:
        pass

    monkeypatch.setattr('flutes.structure._NO_MAP_TYPES', (NoMapType,))
    
    obj = NoMapType()
    result = map_structure(lambda x: x, obj)
    assert result is obj

def test_map_structure_no_map_instance_attr():
    class NoMapInstanceAttr:
        __no_map__ = True

    obj = NoMapInstanceAttr()
    result = map_structure(lambda x: x, obj)
    assert result is obj

def test_map_structure_list():
    obj = [1, 2, 3]
    result = map_structure(lambda x: x + 1, obj)
    assert result == [2, 3, 4]

def test_map_structure_tuple():
    obj = (1, 2, 3)
    result = map_structure(lambda x: x + 1, obj)
    assert result == (2, 3, 4)

def test_map_structure_namedtuple():
    MyTuple = namedtuple('MyTuple', ['a', 'b', 'c'])
    obj = MyTuple(1, 2, 3)
    result = map_structure(lambda x: x + 1, obj)
    assert result == MyTuple(2, 3, 4)

def test_map_structure_dict():
    obj = {'a': 1, 'b': 2, 'c': 3}
    result = map_structure(lambda x: x + 1, obj)
    assert result == {'a': 2, 'b': 3, 'c': 4}

def test_map_structure_set():
    obj = {1, 2, 3}
    result = map_structure(lambda x: x + 1, obj)
    assert result == {2, 3, 4}

def test_map_structure_default():
    obj = 1
    result = map_structure(lambda x: x + 1, obj)
    assert result == 2
