# file: dataclasses_json/undefined.py:243-256
# asked: {"lines": [243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 256], "branches": [[248, 249], [248, 251], [251, 252], [251, 256]]}
# gained: {"lines": [243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 256], "branches": [[248, 249], [248, 251], [251, 252], [251, 256]]}

import pytest
from dataclasses import dataclass, field, fields
from typing import Optional, Dict
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError
from dataclasses_json.utils import CatchAllVar

@dataclass
class SingleCatchAll:
    catch_all: Optional[CatchAllVar] = field(default=None)

@dataclass
class NoCatchAll:
    regular_field: Optional[str] = field(default=None)

@dataclass
class MultipleCatchAll:
    catch_all_1: Optional[CatchAllVar] = field(default=None)
    catch_all_2: Optional[CatchAllVar] = field(default=None)

def test_single_catch_all():
    assert _CatchAllUndefinedParameters._get_catch_all_field(SingleCatchAll) == fields(SingleCatchAll)[0]

def test_no_catch_all():
    with pytest.raises(UndefinedParameterError, match="No field of type dataclasses_json.CatchAll defined"):
        _CatchAllUndefinedParameters._get_catch_all_field(NoCatchAll)

def test_multiple_catch_all():
    with pytest.raises(UndefinedParameterError, match="Multiple catch-all fields supplied: 2."):
        _CatchAllUndefinedParameters._get_catch_all_field(MultipleCatchAll)
