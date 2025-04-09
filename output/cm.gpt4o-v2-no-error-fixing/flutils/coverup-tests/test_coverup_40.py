# file: flutils/namedtupleutils.py:32-90
# asked: {"lines": [32, 90], "branches": []}
# gained: {"lines": [32, 90], "branches": []}

import pytest
from collections import OrderedDict
from types import SimpleNamespace
from flutils.namedtupleutils import to_namedtuple

def test_to_namedtuple_with_list():
    obj = [1, 2, 3]
    result = to_namedtuple(obj)
    assert isinstance(result, list)
    assert result == obj

def test_to_namedtuple_with_tuple():
    obj = (1, 2, 3)
    result = to_namedtuple(obj)
    assert isinstance(result, tuple)
    assert result == obj

def test_to_namedtuple_with_dict():
    obj = {'a': 1, 'b': 2}
    result = to_namedtuple(obj)
    assert isinstance(result, tuple)
    assert result._fields == ('a', 'b')
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_ordered_dict():
    obj = OrderedDict([('a', 1), ('b', 2)])
    result = to_namedtuple(obj)
    assert isinstance(result, tuple)
    assert result._fields == ('a', 'b')
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_simplenamespace():
    obj = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(obj)
    assert isinstance(result, tuple)
    assert result._fields == ('a', 'b')
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_nested_dict():
    obj = {'a': 1, 'b': {'c': 2}}
    result = to_namedtuple(obj)
    assert isinstance(result, tuple)
    assert result._fields == ('a', 'b')
    assert result.a == 1
    assert isinstance(result.b, tuple)
    assert result.b._fields == ('c',)
    assert result.b.c == 2

def test_to_namedtuple_with_invalid_type():
    with pytest.raises(TypeError):
        to_namedtuple(123)
