# file: flutils/namedtupleutils.py:32-90
# asked: {"lines": [32, 90], "branches": []}
# gained: {"lines": [32, 90], "branches": []}

import pytest
from flutils.namedtupleutils import to_namedtuple
from collections import OrderedDict
from types import SimpleNamespace

def test_to_namedtuple_with_dict():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_list():
    lst = [{'a': 1}, {'b': 2}]
    result = to_namedtuple(lst)
    assert result[0].a == 1
    assert result[1].b == 2

def test_to_namedtuple_with_tuple():
    tpl = ({'a': 1}, {'b': 2})
    result = to_namedtuple(tpl)
    assert result[0].a == 1
    assert result[1].b == 2

def test_to_namedtuple_with_ordereddict():
    ord_dict = OrderedDict([('a', 1), ('b', 2)])
    result = to_namedtuple(ord_dict)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_simplenamespace():
    ns = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(ns)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_invalid_type():
    with pytest.raises(TypeError):
        to_namedtuple(123)

def test_to_namedtuple_with_nested_dict():
    nested_dict = {'a': {'b': 2}}
    result = to_namedtuple(nested_dict)
    assert result.a.b == 2

def test_to_namedtuple_with_underscore_key():
    dic = {'_a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert not hasattr(result, '_a')
    assert result.b == 2
