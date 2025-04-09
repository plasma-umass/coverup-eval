# file: dataclasses_json/undefined.py:203-207
# asked: {"lines": [203, 204, 205, 206, 207], "branches": []}
# gained: {"lines": [203, 204, 205, 206, 207], "branches": []}

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters
from dataclasses_json.utils import CatchAllVar
from dataclasses_json.undefined import UndefinedParameterError

@dataclass
class TestClass:
    defined_field: int
    catch_all: Optional[CatchAllVar] = field(default_factory=dict)

def test_handle_dump():
    obj = TestClass(defined_field=1, catch_all={'extra_field': 'extra_value'})
    result = _CatchAllUndefinedParameters.handle_dump(obj)
    assert result == {'extra_field': 'extra_value'}

def test_handle_dump_no_catch_all_field():
    @dataclass
    class NoCatchAllFieldClass:
        defined_field: int

    obj = NoCatchAllFieldClass(defined_field=1)
    with pytest.raises(UndefinedParameterError, match='No field of type dataclasses_json.CatchAll defined'):
        _CatchAllUndefinedParameters.handle_dump(obj)

def test_handle_dump_multiple_catch_all_fields():
    @dataclass
    class MultipleCatchAllFieldClass:
        defined_field: int
        catch_all1: Optional[CatchAllVar] = field(default_factory=dict)
        catch_all2: Optional[CatchAllVar] = field(default_factory=dict)

    obj = MultipleCatchAllFieldClass(defined_field=1)
    with pytest.raises(UndefinedParameterError, match='Multiple catch-all fields supplied: 2.'):
        _CatchAllUndefinedParameters.handle_dump(obj)
