# file dataclasses_json/undefined.py:243-256
# lines [249, 250, 252, 253, 254]
# branches ['248->249', '251->252']

import pytest
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, CatchAll
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError
from typing import Optional

@dataclass_json
@dataclass
class NoCatchAll:
    name: str

@dataclass_json
@dataclass
class MultipleCatchAll:
    name: str
    extras1: Optional[CatchAll] = field(default=None)
    extras2: Optional[CatchAll] = field(default=None)

def test_no_catch_all_field():
    with pytest.raises(UndefinedParameterError) as exc_info:
        _CatchAllUndefinedParameters._get_catch_all_field(NoCatchAll)
    assert str(exc_info.value) == "No field of type dataclasses_json.CatchAll defined"

def test_multiple_catch_all_fields():
    with pytest.raises(UndefinedParameterError) as exc_info:
        _CatchAllUndefinedParameters._get_catch_all_field(MultipleCatchAll)
    assert "Multiple catch-all fields supplied" in str(exc_info.value)
