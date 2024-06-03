# file dataclasses_json/undefined.py:17-56
# lines [17, 18, 19, 20, 24, 26, 27, 31, 33, 34, 38, 40, 41, 42, 44, 45, 50, 51, 52, 53, 54, 55, 56]
# branches []

import pytest
from unittest import mock
from dataclasses import dataclass, fields
from typing import Any, Dict, Tuple, Callable

# Assuming the code provided is in a module named dataclasses_json.undefined
from dataclasses_json.undefined import _UndefinedParameterAction

@dataclass
class DummyClass:
    a: int
    b: str

class TestUndefinedParameterAction(_UndefinedParameterAction):
    @staticmethod
    def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
        return kvs

def test_handle_to_dict():
    obj = DummyClass(a=1, b='test')
    kvs = {'a': 1, 'b': 'test'}
    result = TestUndefinedParameterAction.handle_to_dict(obj, kvs)
    assert result == kvs

def test_handle_dump():
    obj = DummyClass(a=1, b='test')
    result = TestUndefinedParameterAction.handle_dump(obj)
    assert result == {}

def test_create_init():
    obj = DummyClass(a=1, b='test')
    init_func = TestUndefinedParameterAction.create_init(obj)
    assert init_func == obj.__init__

def test_separate_defined_undefined_kvs():
    kvs = {'a': 1, 'b': 'test', 'c': 3.14}
    known, unknown = TestUndefinedParameterAction._separate_defined_undefined_kvs(DummyClass, kvs)
    assert known == {'a': 1, 'b': 'test'}
    assert unknown == {'c': 3.14}
