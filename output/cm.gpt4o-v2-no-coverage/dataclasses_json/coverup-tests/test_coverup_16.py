# file: dataclasses_json/core.py:234-238
# asked: {"lines": [234, 235, 236, 237, 238], "branches": []}
# gained: {"lines": [234, 235, 236, 237, 238], "branches": []}

import pytest
from enum import Enum
from typing import List, Union, Optional, Any
from dataclasses_json.utils import _is_collection, _is_optional, _issubclass_safe
from dataclasses_json.core import _is_supported_generic

class TestEnum(Enum):
    A = 1
    B = 2

class TestClass:
    pass

def test_is_supported_generic_with_collection():
    assert _is_supported_generic(List[int]) is True

def test_is_supported_generic_with_optional():
    assert _is_supported_generic(Optional[int]) is True

def test_is_supported_generic_with_union():
    assert _is_supported_generic(Union[int, str]) is True

def test_is_supported_generic_with_enum():
    assert _is_supported_generic(TestEnum) is True

def test_is_supported_generic_with_str():
    assert _is_supported_generic(str) is False

def test_is_supported_generic_with_non_supported_type():
    assert _is_supported_generic(TestClass) is False

def test_issubclass_safe_with_valid_subclass():
    assert _issubclass_safe(TestEnum, Enum) is True

def test_issubclass_safe_with_invalid_subclass():
    assert _issubclass_safe(TestClass, Enum) is False

def test_is_collection_with_list():
    assert _is_collection(List[int]) is True

def test_is_optional_with_optional():
    assert _is_optional(Optional[int]) is True

def test_is_optional_with_any():
    assert _is_optional(Any) is True

def test_is_optional_with_none_type(monkeypatch):
    def mock_hasargs(type_, arg):
        return type_ is Optional or arg is type(None)
    
    monkeypatch.setattr('dataclasses_json.utils._hasargs', mock_hasargs)
    assert _is_optional(type(None)) is True

def test_is_optional_with_non_optional():
    assert _is_optional(int) is False
