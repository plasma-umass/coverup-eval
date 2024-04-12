# file dataclasses_json/undefined.py:17-56
# lines [17, 18, 19, 20, 24, 26, 27, 31, 33, 34, 38, 40, 41, 42, 44, 45, 50, 51, 52, 53, 54, 55, 56]
# branches []

import pytest
from dataclasses import dataclass, fields
from typing import Dict, Any, Tuple, Callable
from abc import ABC, abstractmethod
from dataclasses_json.undefined import _UndefinedParameterAction

class ConcreteUndefinedParameterAction(_UndefinedParameterAction):
    @staticmethod
    def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
        return kvs

@dataclass
class Example:
    a: int
    b: int

@pytest.fixture
def mock_cls():
    return Example

def test_handle_from_dict(mock_cls):
    kvs = {'a': 1, 'b': 2}
    result = ConcreteUndefinedParameterAction.handle_from_dict(mock_cls, kvs)
    assert result == kvs

def test_handle_to_dict():
    obj = Example(a=1, b=2)
    kvs = {'a': 1, 'b': 2}
    result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
    assert result == kvs

def test_handle_dump():
    obj = Example(a=1, b=2)
    result = _UndefinedParameterAction.handle_dump(obj)
    assert result == {}

def test_create_init(mock_cls):
    init_method = _UndefinedParameterAction.create_init(mock_cls)
    assert callable(init_method)

def test_separate_defined_undefined_kvs(mock_cls):
    kvs = {'a': 1, 'b': 2, 'c': 3}
    known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(mock_cls, kvs)
    assert known == {'a': 1, 'b': 2}
    assert unknown == {'c': 3}
