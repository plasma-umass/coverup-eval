# file dataclasses_json/undefined.py:203-207
# lines [203, 204, 205, 206, 207]
# branches []

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters, _UndefinedParameterAction, UndefinedParameterError

# Mocking the CatchAllVar type for the purpose of this test
class CatchAllVar:
    pass

@dataclass
class TestClass:
    existing_field: int
    catch_all: Optional[Dict[str, Any]] = field(default_factory=dict)

    @staticmethod
    def _get_catch_all_field(cls):
        return cls.__dataclass_fields__['catch_all']

def test_handle_dump(mocker):
    # Mocking the _get_catch_all_field method to return the correct field
    mocker.patch.object(_CatchAllUndefinedParameters, '_get_catch_all_field', return_value=TestClass._get_catch_all_field(TestClass))
    
    obj = TestClass(existing_field=1, catch_all={'extra_field': 'extra_value'})
    
    result = _CatchAllUndefinedParameters.handle_dump(obj)
    
    assert result == {'extra_field': 'extra_value'}
