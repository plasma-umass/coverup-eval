# file: dataclasses_json/undefined.py:17-56
# asked: {"lines": [24, 31, 38, 42], "branches": []}
# gained: {"lines": [31, 38, 42], "branches": []}

import pytest
from unittest.mock import MagicMock
from dataclasses import dataclass, field
from typing import Any, Dict, Callable
from dataclasses_json.undefined import _UndefinedParameterAction

@dataclass
class DummyClass:
    a: int
    b: str = field(default="default")

class TestUndefinedParameterAction:
    
    def test_handle_from_dict(self):
        class ConcreteUndefinedParameterAction(_UndefinedParameterAction):
            @staticmethod
            def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
                return kvs

        kvs = {'a': 1, 'b': 'test'}
        result = ConcreteUndefinedParameterAction.handle_from_dict(DummyClass, kvs)
        assert result == kvs

    def test_handle_to_dict(self):
        obj = DummyClass(a=1, b='test')
        kvs = {'a': 1, 'b': 'test'}
        result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
        assert result == kvs

    def test_handle_dump(self):
        obj = DummyClass(a=1, b='test')
        result = _UndefinedParameterAction.handle_dump(obj)
        assert result == {}

    def test_create_init(self):
        obj = DummyClass(a=1, b='test')
        init_method = _UndefinedParameterAction.create_init(obj)
        assert isinstance(init_method, Callable)
        assert init_method == obj.__init__
