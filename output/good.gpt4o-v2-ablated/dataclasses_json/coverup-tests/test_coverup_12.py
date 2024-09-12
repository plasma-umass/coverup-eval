# file: dataclasses_json/undefined.py:17-56
# asked: {"lines": [24, 31, 38, 42, 50, 51, 52, 53, 54, 55, 56], "branches": []}
# gained: {"lines": [31, 38, 42, 50, 51, 52, 53, 54, 55, 56], "branches": []}

import pytest
from unittest import mock
from dataclasses import dataclass, fields
from typing import Any, Dict, Tuple, Callable

# Assuming the code is in a module named undefined
from dataclasses_json.undefined import _UndefinedParameterAction

@dataclass
class DummyClass:
    a: int
    b: str

class TestUndefinedParameterAction:
    def test_handle_from_dict(self):
        class TestAction(_UndefinedParameterAction):
            @staticmethod
            def handle_from_dict(cls, kvs: Dict[Any, Any]) -> Dict[str, Any]:
                return kvs

        kvs = {'a': 1, 'b': 'test'}
        result = TestAction.handle_from_dict(DummyClass, kvs)
        assert result == kvs

    def test_handle_to_dict(self):
        kvs = {'a': 1, 'b': 'test'}
        result = _UndefinedParameterAction.handle_to_dict(None, kvs)
        assert result == kvs

    def test_handle_dump(self):
        result = _UndefinedParameterAction.handle_dump(None)
        assert result == {}

    def test_create_init(self):
        obj = DummyClass(1, 'test')
        init_method = _UndefinedParameterAction.create_init(obj)
        assert init_method == obj.__init__

    def test_separate_defined_undefined_kvs(self):
        kvs = {'a': 1, 'b': 'test', 'c': 3.14}
        known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(DummyClass, kvs)
        assert known == {'a': 1, 'b': 'test'}
        assert unknown == {'c': 3.14}
