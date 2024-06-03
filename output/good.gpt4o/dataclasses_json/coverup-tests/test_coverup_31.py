# file dataclasses_json/undefined.py:243-256
# lines [245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 256]
# branches ['248->249', '248->251', '251->252', '251->256']

import pytest
from dataclasses import dataclass, field, fields
from typing import Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError, CatchAllVar

@dataclass
class TestClassNoCatchAll:
    a: int

@dataclass
class TestClassMultipleCatchAll:
    a: int
    b: Optional[CatchAllVar] = field(default=None)
    c: Optional[CatchAllVar] = field(default=None)

@dataclass
class TestClassSingleCatchAll:
    a: int
    b: Optional[CatchAllVar] = field(default=None)

def test_no_catch_all_field():
    with pytest.raises(UndefinedParameterError, match="No field of type dataclasses_json.CatchAll defined"):
        _CatchAllUndefinedParameters._get_catch_all_field(TestClassNoCatchAll)

def test_multiple_catch_all_fields():
    with pytest.raises(UndefinedParameterError, match="Multiple catch-all fields supplied: 2."):
        _CatchAllUndefinedParameters._get_catch_all_field(TestClassMultipleCatchAll)

def test_single_catch_all_field():
    field = _CatchAllUndefinedParameters._get_catch_all_field(TestClassSingleCatchAll)
    assert field.name == 'b'
    assert field.type == Optional[CatchAllVar]
