# file: dataclasses_json/undefined.py:17-56
# asked: {"lines": [17, 18, 19, 20, 24, 26, 27, 31, 33, 34, 38, 40, 41, 42, 44, 45, 50, 51, 52, 53, 54, 55, 56], "branches": []}
# gained: {"lines": [17, 18, 19, 20, 26, 27, 31, 33, 34, 38, 40, 41, 42, 44, 45, 50, 51, 52, 53, 54, 55, 56], "branches": []}

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict
from dataclasses_json.undefined import _UndefinedParameterAction

class TestUndefinedParameterAction:
    
    def test_handle_to_dict(self):
        obj = object()
        kvs = {"key1": "value1", "key2": "value2"}
        result = _UndefinedParameterAction.handle_to_dict(obj, kvs)
        assert result == kvs

    def test_handle_dump(self):
        obj = object()
        result = _UndefinedParameterAction.handle_dump(obj)
        assert result == {}

    def test_create_init(self):
        @dataclass
        class SampleClass:
            a: int
            b: str
        
        obj = SampleClass(1, "test")
        init_method = _UndefinedParameterAction.create_init(obj)
        assert init_method == obj.__init__

    def test_separate_defined_undefined_kvs(self):
        @dataclass
        class SampleClass:
            a: int
            b: str
        
        kvs = {"a": 1, "b": "test", "c": 3.14}
        known, unknown = _UndefinedParameterAction._separate_defined_undefined_kvs(SampleClass, kvs)
        assert known == {"a": 1, "b": "test"}
        assert unknown == {"c": 3.14}
