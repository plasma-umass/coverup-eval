# file: dataclasses_json/core.py:241-280
# asked: {"lines": [250, 251, 254, 255, 256, 258, 262, 263, 264, 265, 269, 274, 275, 277], "branches": [[249, 250], [250, 251], [250, 258], [267, 269], [272, 274], [274, 275], [274, 277]]}
# gained: {"lines": [250, 251, 254, 255, 256, 262, 263, 274, 275, 277], "branches": [[249, 250], [250, 251], [272, 274], [274, 275], [274, 277]]}

import pytest
from unittest.mock import patch
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Union, Optional, Any

# Assuming the following functions and classes are defined in dataclasses_json/core.py
from dataclasses_json.core import _decode_generic, _issubclass_safe, _is_collection, _is_mapping, _decode_dict_keys, _decode_items, _get_type_cons, _is_optional, _is_supported_generic, _support_extended_types, _decode_dataclass

class SampleEnum(Enum):
    A = "a"
    B = "b"

@dataclass
class SampleDataClass:
    field: int

def test_decode_generic_with_mapping(monkeypatch):
    def mock_issubclass_safe(type_, classinfo):
        return False

    def mock_is_collection(type_):
        return True

    def mock_is_mapping(type_):
        return True

    def mock_decode_dict_keys(k_type, keys, infer_missing):
        return list(keys)

    def mock_decode_items(v_type, values, infer_missing):
        return list(values)

    def mock_get_type_cons(type_):
        return dict

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_mapping', mock_is_mapping)
    monkeypatch.setattr('dataclasses_json.core._decode_dict_keys', mock_decode_dict_keys)
    monkeypatch.setattr('dataclasses_json.core._decode_items', mock_decode_items)
    monkeypatch.setattr('dataclasses_json.core._get_type_cons', mock_get_type_cons)

    type_ = Dict[str, int]
    value = {"key1": 1, "key2": 2}
    infer_missing = False

    result = _decode_generic(type_, value, infer_missing)
    assert result == value

def test_decode_generic_with_optional(monkeypatch):
    def mock_issubclass_safe(type_, classinfo):
        return False

    def mock_is_collection(type_):
        return False

    def mock_is_optional(type_):
        return True

    def mock_is_supported_generic(type_):
        return False

    def mock_support_extended_types(type_arg, value):
        return value

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_optional', mock_is_optional)
    monkeypatch.setattr('dataclasses_json.core._is_supported_generic', mock_is_supported_generic)
    monkeypatch.setattr('dataclasses_json.core._support_extended_types', mock_support_extended_types)

    type_ = Optional[int]
    value = 10
    infer_missing = False

    result = _decode_generic(type_, value, infer_missing)
    assert result == value

def test_decode_generic_with_supported_generic(monkeypatch):
    def mock_issubclass_safe(type_, classinfo):
        return False

    def mock_is_collection(type_):
        return False

    def mock_is_optional(type_):
        return True

    def mock_is_supported_generic(type_):
        return True

    def mock_decode_generic(type_arg, value, infer_missing):
        return value

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_optional', mock_is_optional)
    monkeypatch.setattr('dataclasses_json.core._is_supported_generic', mock_is_supported_generic)
    monkeypatch.setattr('dataclasses_json.core._decode_generic', mock_decode_generic)

    type_ = Optional[List[int]]
    value = [1, 2, 3]
    infer_missing = False

    result = _decode_generic(type_, value, infer_missing)
    assert result == value

def test_decode_generic_with_dataclass(monkeypatch):
    def mock_issubclass_safe(type_, classinfo):
        return False

    def mock_is_collection(type_):
        return False

    def mock_is_optional(type_):
        return True

    def mock_is_supported_generic(type_):
        return False

    def mock_is_dataclass(type_):
        return True

    def mock_decode_dataclass(type_arg, value, infer_missing):
        return SampleDataClass(field=value)

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_optional', mock_is_optional)
    monkeypatch.setattr('dataclasses_json.core._is_supported_generic', mock_is_supported_generic)
    monkeypatch.setattr('dataclasses_json.core.is_dataclass', mock_is_dataclass)
    monkeypatch.setattr('dataclasses_json.core._decode_dataclass', mock_decode_dataclass)

    type_ = Optional[SampleDataClass]
    value = 10
    infer_missing = False

    result = _decode_generic(type_, value, infer_missing)
    assert result == SampleDataClass(field=10)
