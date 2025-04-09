# file: flutes/structure.py:74-96
# asked: {"lines": [74, 75, 82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}
# gained: {"lines": [74, 75, 82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96], "branches": [[82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 91], [87, 88], [87, 90], [91, 93], [91, 94], [94, 95], [94, 96]]}

import pytest
from collections import namedtuple, OrderedDict
from flutes.structure import map_structure

def test_map_structure_no_map_types(monkeypatch):
    class NoMapType:
        pass

    obj = NoMapType()
    fn = lambda x: x

    import flutes.structure
    monkeypatch.setattr(flutes.structure, '_NO_MAP_TYPES', {NoMapType})
    assert map_structure(fn, obj) is obj

def test_map_structure_no_map_instance_attr(monkeypatch):
    class NoMapInstanceAttr:
        _no_map = True

    obj = NoMapInstanceAttr()
    fn = lambda x: x

    import flutes.structure
    monkeypatch.setattr(flutes.structure, '_NO_MAP_INSTANCE_ATTR', '_no_map')
    assert map_structure(fn, obj) is obj

def test_map_structure_list():
    obj = [1, 2, [3, 4]]
    fn = lambda x: x + 1
    result = map_structure(fn, obj)
    assert result == [2, 3, [4, 5]]

def test_map_structure_tuple():
    obj = (1, 2, (3, 4))
    fn = lambda x: x + 1
    result = map_structure(fn, obj)
    assert result == (2, 3, (4, 5))

def test_map_structure_namedtuple():
    MyNamedTuple = namedtuple('MyNamedTuple', ['a', 'b'])
    obj = MyNamedTuple(a=1, b=2)
    fn = lambda x: x + 1
    result = map_structure(fn, obj)
    assert result == MyNamedTuple(a=2, b=3)

def test_map_structure_dict():
    obj = {'a': 1, 'b': {'c': 2}}
    fn = lambda x: x + 1
    result = map_structure(fn, obj)
    assert result == {'a': 2, 'b': {'c': 3}}

def test_map_structure_ordereddict():
    obj = OrderedDict([('a', 1), ('b', OrderedDict([('c', 2)]))])
    fn = lambda x: x + 1
    result = map_structure(fn, obj)
    assert result == OrderedDict([('a', 2), ('b', OrderedDict([('c', 3)]))])

def test_map_structure_set():
    obj = {1, 2, 3}
    fn = lambda x: x + 1
    result = map_structure(fn, obj)
    assert result == {2, 3, 4}

def test_map_structure_default():
    obj = 1
    fn = lambda x: x + 1
    result = map_structure(fn, obj)
    assert result == 2
