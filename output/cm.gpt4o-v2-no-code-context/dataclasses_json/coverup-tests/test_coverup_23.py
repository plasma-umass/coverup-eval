# file: dataclasses_json/core.py:234-238
# asked: {"lines": [234, 235, 236, 237, 238], "branches": []}
# gained: {"lines": [234, 235, 236, 237, 238], "branches": []}

import pytest
from dataclasses_json.core import _is_supported_generic
from enum import Enum

def test_is_supported_generic_with_collection(monkeypatch):
    class MockCollection:
        pass

    def mock_issubclass_safe(type_, classinfo):
        if type_ is MockCollection and classinfo is str:
            return False
        if type_ is MockCollection and classinfo is Enum:
            return False
        return False

    def mock_is_collection(type_):
        return type_ is MockCollection

    def mock_is_optional(type_):
        return False

    def mock_is_union_type(type_):
        return False

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_optional', mock_is_optional)
    monkeypatch.setattr('dataclasses_json.core.is_union_type', mock_is_union_type)

    assert _is_supported_generic(MockCollection) is True

def test_is_supported_generic_with_optional(monkeypatch):
    class MockOptional:
        pass

    def mock_issubclass_safe(type_, classinfo):
        if type_ is MockOptional and classinfo is str:
            return False
        if type_ is MockOptional and classinfo is Enum:
            return False
        return False

    def mock_is_collection(type_):
        return False

    def mock_is_optional(type_):
        return type_ is MockOptional

    def mock_is_union_type(type_):
        return False

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_optional', mock_is_optional)
    monkeypatch.setattr('dataclasses_json.core.is_union_type', mock_is_union_type)

    assert _is_supported_generic(MockOptional) is True

def test_is_supported_generic_with_union_type(monkeypatch):
    class MockUnionType:
        pass

    def mock_issubclass_safe(type_, classinfo):
        if type_ is MockUnionType and classinfo is str:
            return False
        if type_ is MockUnionType and classinfo is Enum:
            return False
        return False

    def mock_is_collection(type_):
        return False

    def mock_is_optional(type_):
        return False

    def mock_is_union_type(type_):
        return type_ is MockUnionType

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_optional', mock_is_optional)
    monkeypatch.setattr('dataclasses_json.core.is_union_type', mock_is_union_type)

    assert _is_supported_generic(MockUnionType) is True

def test_is_supported_generic_with_enum(monkeypatch):
    class MockEnum(Enum):
        A = 1

    def mock_issubclass_safe(type_, classinfo):
        if type_ is MockEnum and classinfo is str:
            return False
        if type_ is MockEnum and classinfo is Enum:
            return True
        return False

    def mock_is_collection(type_):
        return False

    def mock_is_optional(type_):
        return False

    def mock_is_union_type(type_):
        return False

    monkeypatch.setattr('dataclasses_json.core._issubclass_safe', mock_issubclass_safe)
    monkeypatch.setattr('dataclasses_json.core._is_collection', mock_is_collection)
    monkeypatch.setattr('dataclasses_json.core._is_optional', mock_is_optional)
    monkeypatch.setattr('dataclasses_json.core.is_union_type', mock_is_union_type)

    assert _is_supported_generic(MockEnum) is True
