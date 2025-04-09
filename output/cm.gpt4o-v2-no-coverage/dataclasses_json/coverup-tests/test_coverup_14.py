# file: dataclasses_json/undefined.py:169-191
# asked: {"lines": [169, 170, 176, 177, 179, 181, 182, 183, 184, 185, 189, 191], "branches": [[183, 184], [183, 185], [185, 189], [185, 191]]}
# gained: {"lines": [169, 170, 176, 177, 179, 181, 182, 183, 184, 185, 189, 191], "branches": [[183, 184], [183, 185], [185, 189], [185, 191]]}

import pytest
import dataclasses
from dataclasses import Field
from typing import Any
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@dataclasses.dataclass
class TestClass:
    field_without_default: Any = dataclasses.field(default=dataclasses.MISSING)
    field_with_default: int = 42
    field_with_default_factory: list = dataclasses.field(default_factory=list)

def test_get_default_with_default():
    field = TestClass.__dataclass_fields__['field_with_default']
    default_value = _CatchAllUndefinedParameters._get_default(field)
    assert default_value == 42

def test_get_default_with_default_factory():
    field = TestClass.__dataclass_fields__['field_with_default_factory']
    default_value = _CatchAllUndefinedParameters._get_default(field)
    assert default_value == []

def test_get_default_without_default(monkeypatch):
    field = TestClass.__dataclass_fields__['field_without_default']
    default_value = _CatchAllUndefinedParameters._get_default(field)
    assert default_value == _CatchAllUndefinedParameters._SentinelNoDefault
