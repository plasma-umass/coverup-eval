# file: flutils/namedtupleutils.py:32-90
# asked: {"lines": [32, 90], "branches": []}
# gained: {"lines": [32, 90], "branches": []}

import pytest
from collections import namedtuple, OrderedDict
from types import SimpleNamespace
from flutils.namedtupleutils import to_namedtuple

def test_to_namedtuple_with_dict():
    dic = {'a': 1, 'b': 2}
    result = to_namedtuple(dic)
    assert isinstance(result, tuple)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_list():
    lst = [{'a': 1}, {'b': 2}]
    result = to_namedtuple(lst)
    assert isinstance(result, list)
    assert isinstance(result[0], tuple)
    assert result[0].a == 1
    assert isinstance(result[1], tuple)
    assert result[1].b == 2

def test_to_namedtuple_with_tuple():
    tpl = ({'a': 1}, {'b': 2})
    result = to_namedtuple(tpl)
    assert isinstance(result, tuple)
    assert isinstance(result[0], tuple)
    assert result[0].a == 1
    assert isinstance(result[1], tuple)
    assert result[1].b == 2

def test_to_namedtuple_with_ordered_dict():
    ord_dict = OrderedDict([('a', 1), ('b', 2)])
    result = to_namedtuple(ord_dict)
    assert isinstance(result, tuple)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_simple_namespace():
    ns = SimpleNamespace(a=1, b=2)
    result = to_namedtuple(ns)
    assert isinstance(result, tuple)
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_invalid_type():
    with pytest.raises(TypeError):
        to_namedtuple(123)
