# file: dataclasses_json/undefined.py:79-118
# asked: {"lines": [79, 80, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118], "branches": []}
# gained: {"lines": [79, 80, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses import dataclass, field
from typing import Any, Dict

# Assuming the classes are imported from dataclasses_json.undefined
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _UndefinedParameterAction, _CatchAllUndefinedParameters

@dataclass
class TestClass:
    a: int
    b: int = field(default=0)

def test_handle_from_dict():
    kvs = {'a': 1, 'b': 2, 'c': 3}
    result = _IgnoreUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == {'a': 1, 'b': 2}

def test_create_init(monkeypatch):
    @dataclass
    class TestClass:
        a: int
        b: int = field(default=0)

    def mock_separate_defined_undefined_kvs(cls, kvs: Dict) -> Dict[str, Any]:
        return {'a': 1, 'b': 2}, {'c': 3}

    monkeypatch.setattr(_CatchAllUndefinedParameters, '_separate_defined_undefined_kvs', mock_separate_defined_undefined_kvs)

    init_func = _IgnoreUndefinedParameters.create_init(TestClass)
    obj = TestClass.__new__(TestClass)
    init_func(obj, a=1, b=2, c=3)
    assert obj.a == 1
    assert obj.b == 2

