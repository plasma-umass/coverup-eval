# file: flutils/namedtupleutils.py:141-177
# asked: {"lines": [147, 148, 149, 150, 151, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 167, 168, 169], "branches": [[146, 147], [148, 149], [148, 153], [154, 155], [156, 157], [156, 169], [159, 160], [159, 163], [163, 165], [163, 169]]}
# gained: {"lines": [147, 148, 149, 150, 151, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 165, 167, 168], "branches": [[146, 147], [148, 149], [148, 153], [154, 155], [156, 157], [159, 160], [159, 163], [163, 165]]}

import pytest
from collections import namedtuple
from typing import Sequence, NamedTuple, Union, List, Any, cast

# Assuming _to_namedtuple is imported from flutils.namedtupleutils
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_string():
    with pytest.raises(TypeError) as excinfo:
        _to_namedtuple("test_string")
    assert "Can convert only 'list', 'tuple', 'dict' to a NamedTuple" in str(excinfo.value)

def test_to_namedtuple_with_namedtuple():
    TestNamedTuple = namedtuple('TestNamedTuple', 'field1 field2')
    obj = TestNamedTuple(field1='value1', field2='value2')
    
    result = _to_namedtuple(obj)
    
    assert isinstance(result, tuple)
    assert result.field1 == 'value1'
    assert result.field2 == 'value2'

def test_to_namedtuple_with_empty_namedtuple():
    TestNamedTuple = namedtuple('TestNamedTuple', 'field1 field2')
    obj = TestNamedTuple(field1=None, field2=None)
    
    result = _to_namedtuple(obj)
    
    assert isinstance(result, tuple)
    assert result.field1 is None
    assert result.field2 is None

def test_to_namedtuple_with_list_of_namedtuples():
    TestNamedTuple = namedtuple('TestNamedTuple', 'field1 field2')
    obj = [TestNamedTuple(field1='value1', field2='value2'), TestNamedTuple(field1='value3', field2='value4')]
    
    result = _to_namedtuple(obj)
    
    assert isinstance(result, list)
    assert all(isinstance(item, tuple) for item in result)
    assert result[0].field1 == 'value1'
    assert result[0].field2 == 'value2'
    assert result[1].field1 == 'value3'
    assert result[1].field2 == 'value4'

def test_to_namedtuple_with_tuple_of_namedtuples():
    TestNamedTuple = namedtuple('TestNamedTuple', 'field1 field2')
    obj = (TestNamedTuple(field1='value1', field2='value2'), TestNamedTuple(field1='value3', field2='value4'))
    
    result = _to_namedtuple(obj)
    
    assert isinstance(result, tuple)
    assert all(isinstance(item, tuple) for item in result)
    assert result[0].field1 == 'value1'
    assert result[0].field2 == 'value2'
    assert result[1].field1 == 'value3'
    assert result[1].field2 == 'value4'
