# file flutes/structure.py:74-96
# lines [82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96]
# branches ['82->83', '82->84', '84->85', '84->86', '86->87', '86->91', '87->88', '87->90', '91->93', '91->94', '94->95', '94->96']

import pytest
from collections import namedtuple, OrderedDict
from flutes.structure import map_structure

def test_map_structure_no_map_types(mocker):
    class NoMapType:
        pass

    obj = NoMapType()
    fn = mocker.Mock(return_value="mapped")
    result = map_structure(fn, obj)
    assert result == "mapped"
    fn.assert_called_once_with(obj)

def test_map_structure_no_map_instance_attr(mocker):
    class NoMapInstanceAttr:
        _no_map = True

    obj = NoMapInstanceAttr()
    fn = mocker.Mock(return_value="mapped")
    result = map_structure(fn, obj)
    assert result == "mapped"
    fn.assert_called_once_with(obj)

def test_map_structure_list(mocker):
    obj = [1, 2, 3]
    fn = mocker.Mock(side_effect=lambda x: x + 1)
    result = map_structure(fn, obj)
    assert result == [2, 3, 4]
    assert fn.call_count == 3

def test_map_structure_tuple(mocker):
    obj = (1, 2, 3)
    fn = mocker.Mock(side_effect=lambda x: x + 1)
    result = map_structure(fn, obj)
    assert result == (2, 3, 4)
    assert fn.call_count == 3

def test_map_structure_namedtuple(mocker):
    MyNamedTuple = namedtuple('MyNamedTuple', ['a', 'b', 'c'])
    obj = MyNamedTuple(1, 2, 3)
    fn = mocker.Mock(side_effect=lambda x: x + 1)
    result = map_structure(fn, obj)
    assert result == MyNamedTuple(2, 3, 4)
    assert fn.call_count == 3

def test_map_structure_dict(mocker):
    obj = {'a': 1, 'b': 2, 'c': 3}
    fn = mocker.Mock(side_effect=lambda x: x + 1)
    result = map_structure(fn, obj)
    assert result == {'a': 2, 'b': 3, 'c': 4}
    assert fn.call_count == 3

def test_map_structure_ordereddict(mocker):
    obj = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    fn = mocker.Mock(side_effect=lambda x: x + 1)
    result = map_structure(fn, obj)
    assert result == OrderedDict([('a', 2), ('b', 3), ('c', 4)])
    assert fn.call_count == 3

def test_map_structure_set(mocker):
    obj = {1, 2, 3}
    fn = mocker.Mock(side_effect=lambda x: x + 1)
    result = map_structure(fn, obj)
    assert result == {2, 3, 4}
    assert fn.call_count == 3

def test_map_structure_default(mocker):
    obj = 1
    fn = mocker.Mock(return_value="mapped")
    result = map_structure(fn, obj)
    assert result == "mapped"
    fn.assert_called_once_with(obj)
