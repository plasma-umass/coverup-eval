# file flutils/namedtupleutils.py:32-90
# lines [32, 90]
# branches []

import pytest
from collections import namedtuple, OrderedDict
from types import SimpleNamespace
from flutils.namedtupleutils import to_namedtuple

def test_to_namedtuple_with_dict():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_list():
    lst = [1, 2, {'a': 3}]
    result = to_namedtuple(lst)
    assert result[0] == 1
    assert result[1] == 2
    assert result[2].a == 3

def test_to_namedtuple_with_tuple():
    tpl = (1, 2, {'a': 3})
    result = to_namedtuple(tpl)
    assert result[0] == 1
    assert result[1] == 2
    assert result[2].a == 3

def test_to_namedtuple_with_ordereddict():
    od = OrderedDict([('a', 1), ('b', 2)])
    result = to_namedtuple(od)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_simplenamespace():
    ns = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(ns)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_nested_dict():
    nested_dic = {'a': 1, 'b': {'c': 2}}
    result = to_namedtuple(nested_dic)
    assert result.a == 1
    assert result.b.c == 2

def test_to_namedtuple_with_invalid_identifier():
    dic = {'a': 1, '_b': 2}
    result = to_namedtuple(dic)
    assert result.a == 1
    assert not hasattr(result, '_b')

@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
