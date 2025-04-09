# file: flutes/structure.py:74-96
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

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
    obj = [1, 2, [3, 4]]
    result = map_structure(lambda x: x * 2, obj)
    assert result == [2, 4, [6, 8]]

def test_map_structure_tuple():
    obj = (1, 2, (3, 4))
    result = map_structure(lambda x: x * 2, obj)
    assert result == (2, 4, (6, 8))

def test_map_structure_namedtuple():
    MyTuple = namedtuple('MyTuple', ['a', 'b'])
    obj = MyTuple(1, 2)
    result = map_structure(lambda x: x * 2, obj)
    assert result == MyTuple(2, 4)

def test_map_structure_dict():
    obj = {'a': 1, 'b': {'c': 2}}
    result = map_structure(lambda x: x * 2, obj)
    assert result == {'a': 2, 'b': {'c': 4}}

def test_map_structure_set():
    obj = {1, 2, 3}
    result = map_structure(lambda x: x * 2, obj)
    assert result == {2, 4, 6}

def test_map_structure_default():
    obj = 5
    result = map_structure(lambda x: x * 2, obj)
    assert result == 10
