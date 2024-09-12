# file: dataclasses_json/undefined.py:203-207
# asked: {"lines": [203, 204, 205, 206, 207], "branches": []}
# gained: {"lines": [203, 204, 205, 206, 207], "branches": []}

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters, UndefinedParameterError
from dataclasses_json.utils import CatchAllVar

@dataclass
class TestClass:
    defined_field: int
    catch_all: Optional[CatchAllVar] = field(default_factory=dict)

def test_handle_dump():
    obj = TestClass(defined_field=1)
    obj.catch_all['undefined_field'] = 'value'
    
    result = _CatchAllUndefinedParameters.handle_dump(obj)
    
    assert result == obj.catch_all

def test_handle_dump_no_catch_all_field():
    @dataclass
    class NoCatchAllField:
        defined_field: int

    obj = NoCatchAllField(defined_field=1)
    
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(obj)

def test_handle_dump_multiple_catch_all_fields():
    @dataclass
    class MultipleCatchAllFields:
        defined_field: int
        catch_all1: Optional[CatchAllVar] = field(default_factory=dict)
        catch_all2: Optional[CatchAllVar] = field(default_factory=dict)

    obj = MultipleCatchAllFields(defined_field=1)
    
    with pytest.raises(UndefinedParameterError):
        _CatchAllUndefinedParameters.handle_dump(obj)
