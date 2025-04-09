# file: dataclasses_json/core.py:241-280
# asked: {"lines": [242, 243, 244, 247, 249, 250, 251, 254, 255, 256, 258, 262, 263, 264, 265, 267, 269, 270, 271, 272, 273, 274, 275, 277, 279, 280], "branches": [[242, 243], [242, 244], [244, 247], [244, 249], [249, 250], [249, 267], [250, 251], [250, 258], [267, 269], [267, 270], [270, 271], [270, 279], [272, 273], [272, 274], [274, 275], [274, 277]]}
# gained: {"lines": [242, 243, 244, 247, 249, 250, 251, 254, 255, 256, 258, 262, 263, 267, 269, 270, 271, 272, 273, 274, 277, 280], "branches": [[242, 243], [242, 244], [244, 247], [244, 249], [249, 250], [249, 267], [250, 251], [250, 258], [267, 269], [267, 270], [270, 271], [272, 273], [272, 274], [274, 277]]}

import pytest
from dataclasses import dataclass, is_dataclass
from enum import Enum
from typing import List, Dict, Optional, Any
from dataclasses_json.core import _decode_generic
from dataclasses_json.utils import _get_type_cons, _is_collection, _is_mapping, _is_optional, _issubclass_safe

# Mocking the utility functions
def mock_decode_dict_keys(k_type, keys, infer_missing):
    return [k_type(key) for key in keys]

def mock_decode_items(v_type, values, infer_missing):
    return [v_type(value) for value in values]

def mock_decode_dataclass(type_arg, value, infer_missing):
    return type_arg(**value)

def mock_support_extended_types(type_arg, value):
    return type_arg(value)

def mock_is_supported_generic(type_arg):
    return False

@pytest.fixture
def patch_utils(monkeypatch):
    monkeypatch.setattr('dataclasses_json.core._decode_dict_keys', mock_decode_dict_keys)
    monkeypatch.setattr('dataclasses_json.core._decode_items', mock_decode_items)
    monkeypatch.setattr('dataclasses_json.core._decode_dataclass', mock_decode_dataclass)
    monkeypatch.setattr('dataclasses_json.core._support_extended_types', mock_support_extended_types)
    monkeypatch.setattr('dataclasses_json.core._is_supported_generic', mock_is_supported_generic)

def test_decode_generic_none(patch_utils):
    assert _decode_generic(int, None, False) is None

def test_decode_generic_enum(patch_utils):
    class Color(Enum):
        RED = 'red'
        BLUE = 'blue'
    assert _decode_generic(Color, 'red', False) == Color.RED

def test_decode_generic_collection(patch_utils):
    assert _decode_generic(List[int], [1, 2, 3], False) == [1, 2, 3]

def test_decode_generic_mapping(patch_utils):
    assert _decode_generic(Dict[str, int], {'a': 1, 'b': 2}, False) == {'a': 1, 'b': 2}

def test_decode_generic_optional(patch_utils):
    assert _decode_generic(Optional[int], 1, False) == 1
    assert _decode_generic(Optional[int], None, False) is None

@dataclass
class ExampleDataClass:
    x: int
    y: str

def test_decode_generic_dataclass(patch_utils):
    data = {'x': 1, 'y': 'test'}
    assert _decode_generic(Optional[ExampleDataClass], data, False) == ExampleDataClass(x=1, y='test')

def test_decode_generic_any(patch_utils):
    assert _decode_generic(Any, 'any_value', False) == 'any_value'
