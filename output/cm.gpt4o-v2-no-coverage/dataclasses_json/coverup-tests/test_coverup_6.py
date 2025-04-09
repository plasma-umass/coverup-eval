# file: dataclasses_json/undefined.py:243-256
# asked: {"lines": [243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 256], "branches": [[248, 249], [248, 251], [251, 252], [251, 256]]}
# gained: {"lines": [243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 256], "branches": [[248, 249], [248, 251], [251, 252], [251, 256]]}

import pytest
from dataclasses import dataclass, Field
from typing import Optional
from dataclasses_json.utils import CatchAllVar
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError

@dataclass
class TestClassSingleCatchAll:
    catch_all: Optional[CatchAllVar] = None

@dataclass
class TestClassNoCatchAll:
    regular_field: int = 0

@dataclass
class TestClassMultipleCatchAll:
    catch_all1: Optional[CatchAllVar] = None
    catch_all2: Optional[CatchAllVar] = None

def test_get_catch_all_field_single():
    field = _CatchAllUndefinedParameters._get_catch_all_field(TestClassSingleCatchAll)
    assert isinstance(field, Field)
    assert field.name == "catch_all"

def test_get_catch_all_field_none():
    with pytest.raises(UndefinedParameterError, match="No field of type dataclasses_json.CatchAll defined"):
        _CatchAllUndefinedParameters._get_catch_all_field(TestClassNoCatchAll)

def test_get_catch_all_field_multiple():
    with pytest.raises(UndefinedParameterError, match="Multiple catch-all fields supplied: 2."):
        _CatchAllUndefinedParameters._get_catch_all_field(TestClassMultipleCatchAll)
