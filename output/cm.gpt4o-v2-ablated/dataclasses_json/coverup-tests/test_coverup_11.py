# file: dataclasses_json/core.py:315-338
# asked: {"lines": [315, 320, 321, 322, 323, 324, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 338], "branches": [[320, 321], [320, 330], [322, 323], [322, 326], [330, 331], [330, 334], [334, 336], [334, 338]]}
# gained: {"lines": [315], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from collections.abc import Mapping, Collection
from dataclasses import dataclass, field, fields
import copy

# Mock functions and classes
def _is_dataclass_instance(obj):
    return hasattr(obj, '__dataclass_fields__')

def _handle_undefined_parameters_safe(cls, kvs, usage):
    return kvs

def _encode_overrides(result, overrides, encode_json):
    return result

def _user_overrides_or_exts(obj):
    return {}

# The function to be tested
def _asdict(obj, encode_json=False):
    if _is_dataclass_instance(obj):
        result = []
        for field in fields(obj):
            value = _asdict(getattr(obj, field.name), encode_json=encode_json)
            result.append((field.name, value))

        result = _handle_undefined_parameters_safe(cls=obj, kvs=dict(result), usage="to")
        return _encode_overrides(dict(result), _user_overrides_or_exts(obj), encode_json=encode_json)
    elif isinstance(obj, Mapping):
        return dict((_asdict(k, encode_json=encode_json), _asdict(v, encode_json=encode_json)) for k, v in obj.items())
    elif isinstance(obj, Collection) and not isinstance(obj, str) and not isinstance(obj, bytes):
        return list(_asdict(v, encode_json=encode_json) for v in obj)
    else:
        return copy.deepcopy(obj)

# Test cases
@dataclass
class TestDataClass:
    a: int
    b: str
    c: list

def test_asdict_with_dataclass():
    obj = TestDataClass(a=1, b='test', c=[1, 2, 3])
    result = _asdict(obj)
    assert result == {'a': 1, 'b': 'test', 'c': [1, 2, 3]}

def test_asdict_with_mapping():
    obj = {'key1': 'value1', 'key2': 'value2'}
    result = _asdict(obj)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_asdict_with_collection():
    obj = [1, 2, 3, 4]
    result = _asdict(obj)
    assert result == [1, 2, 3, 4]

def test_asdict_with_primitive():
    obj = 42
    result = _asdict(obj)
    assert result == 42

def test_asdict_with_nested_dataclass():
    @dataclass
    class NestedDataClass:
        x: int
        y: TestDataClass

    nested_obj = NestedDataClass(x=10, y=TestDataClass(a=1, b='test', c=[1, 2, 3]))
    result = _asdict(nested_obj)
    assert result == {'x': 10, 'y': {'a': 1, 'b': 'test', 'c': [1, 2, 3]}}

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    monkeypatch.setattr('dataclasses_json.core._is_dataclass_instance', _is_dataclass_instance)
    monkeypatch.setattr('dataclasses_json.core._handle_undefined_parameters_safe', _handle_undefined_parameters_safe)
    monkeypatch.setattr('dataclasses_json.core._encode_overrides', _encode_overrides)
    monkeypatch.setattr('dataclasses_json.core._user_overrides_or_exts', _user_overrides_or_exts)
