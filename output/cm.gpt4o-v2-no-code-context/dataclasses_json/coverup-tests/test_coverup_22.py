# file: dataclasses_json/undefined.py:169-191
# asked: {"lines": [169, 170, 176, 177, 179, 181, 182, 183, 184, 185, 189, 191], "branches": [[183, 184], [183, 185], [185, 189], [185, 191]]}
# gained: {"lines": [169, 170], "branches": []}

import pytest
import dataclasses
from dataclasses import field, Field
from dataclasses_json.undefined import _UndefinedParameterAction
from typing import Any

class _CatchAllUndefinedParameters(_UndefinedParameterAction):
    _SentinelNoDefault = object()

    @staticmethod
    def _get_default(catch_all_field: Field) -> Any:
        has_default = not isinstance(catch_all_field.default, dataclasses._MISSING_TYPE)
        has_default_factory = not isinstance(catch_all_field.default_factory, dataclasses._MISSING_TYPE)
        default_value = _CatchAllUndefinedParameters._SentinelNoDefault
        if has_default:
            default_value = catch_all_field.default
        elif has_default_factory:
            default_value = catch_all_field.default_factory()  # type: ignore
        return default_value

def test_get_default_with_default():
    @dataclasses.dataclass
    class TestClass:
        field_with_default: int = 42

    field_info = TestClass.__dataclass_fields__['field_with_default']
    result = _CatchAllUndefinedParameters._get_default(field_info)
    assert result == 42

def test_get_default_with_default_factory():
    @dataclasses.dataclass
    class TestClass:
        field_with_default_factory: list = field(default_factory=list)

    field_info = TestClass.__dataclass_fields__['field_with_default_factory']
    result = _CatchAllUndefinedParameters._get_default(field_info)
    assert result == []

def test_get_default_with_no_default_or_factory():
    @dataclasses.dataclass
    class TestClass:
        field_without_default: int

    field_info = TestClass.__dataclass_fields__['field_without_default']
    result = _CatchAllUndefinedParameters._get_default(field_info)
    assert result == _CatchAllUndefinedParameters._SentinelNoDefault
