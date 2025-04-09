# file: dataclasses_json/undefined.py:169-191
# asked: {"lines": [184], "branches": [[183, 184]]}
# gained: {"lines": [184], "branches": [[183, 184]]}

import pytest
import dataclasses
from dataclasses import Field
from dataclasses_json.undefined import _CatchAllUndefinedParameters

@dataclasses.dataclass
class TestClass:
    field_with_default: int = 42

def test_get_default_with_default():
    field = TestClass.__dataclass_fields__['field_with_default']
    default_value = _CatchAllUndefinedParameters._get_default(field)
    assert default_value == 42

@dataclasses.dataclass
class TestClassWithFactory:
    field_with_default_factory: list = dataclasses.field(default_factory=list)

def test_get_default_with_default_factory():
    field = TestClassWithFactory.__dataclass_fields__['field_with_default_factory']
    default_value = _CatchAllUndefinedParameters._get_default(field)
    assert default_value == []

@dataclasses.dataclass
class TestClassWithoutDefault:
    field_without_default: int

def test_get_default_without_default():
    field = TestClassWithoutDefault.__dataclass_fields__['field_without_default']
    default_value = _CatchAllUndefinedParameters._get_default(field)
    assert default_value == _CatchAllUndefinedParameters._SentinelNoDefault
