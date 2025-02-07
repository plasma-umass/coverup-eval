# file: dataclasses_json/undefined.py:79-118
# asked: {"lines": [88, 89, 90, 91, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118], "branches": []}
# gained: {"lines": [88, 89, 90, 91, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118], "branches": []}

import pytest
from unittest.mock import patch
from dataclasses import dataclass, field
from typing import Any, Dict

# Assuming the classes are imported from dataclasses_json.undefined
from dataclasses_json.undefined import _IgnoreUndefinedParameters, _UndefinedParameterAction, _CatchAllUndefinedParameters

@dataclass
class TestClass:
    defined_param: Any = field(default=None)

def test_handle_from_dict():
    kvs = {'defined_param': 1, 'undefined_param': 2}
    result = _IgnoreUndefinedParameters.handle_from_dict(TestClass, kvs)
    assert result == {'defined_param': 1}

def test_create_init(monkeypatch):
    @dataclass
    class TestClass:
        defined_param: Any = field(default=None)

    def mock_separate_defined_undefined_kvs(cls, kvs: Dict):
        return {'defined_param': 1}, {'undefined_param': 2}

    monkeypatch.setattr(_UndefinedParameterAction, '_separate_defined_undefined_kvs', mock_separate_defined_undefined_kvs)
    monkeypatch.setattr(_CatchAllUndefinedParameters, '_separate_defined_undefined_kvs', mock_separate_defined_undefined_kvs)

    init_func = _IgnoreUndefinedParameters.create_init(TestClass)
    instance = TestClass.__new__(TestClass)
    init_func(instance, defined_param=1, undefined_param=2)
    assert instance.defined_param == 1
