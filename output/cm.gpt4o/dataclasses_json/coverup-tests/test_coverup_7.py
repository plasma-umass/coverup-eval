# file dataclasses_json/undefined.py:169-191
# lines [169, 170, 176, 177, 179, 181, 182, 183, 184, 185, 189, 191]
# branches ['183->184', '183->185', '185->189', '185->191']

import pytest
import dataclasses
from dataclasses import field, Field
from dataclasses_json.undefined import _CatchAllUndefinedParameters

def test_get_default_with_default():
    @dataclasses.dataclass
    class TestClass:
        field_with_default: int = 42

    catch_all_field = TestClass.__dataclass_fields__['field_with_default']
    default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
    assert default_value == 42

def test_get_default_with_default_factory():
    @dataclasses.dataclass
    class TestClass:
        field_with_default_factory: list = field(default_factory=list)

    catch_all_field = TestClass.__dataclass_fields__['field_with_default_factory']
    default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
    assert default_value == []

def test_get_default_with_no_default():
    @dataclasses.dataclass
    class TestClass:
        field_without_default: int

    catch_all_field = TestClass.__dataclass_fields__['field_without_default']
    default_value = _CatchAllUndefinedParameters._get_default(catch_all_field)
    assert default_value == _CatchAllUndefinedParameters._SentinelNoDefault
