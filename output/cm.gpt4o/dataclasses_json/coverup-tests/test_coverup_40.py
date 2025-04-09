# file dataclasses_json/undefined.py:193-201
# lines [195, 196, 197, 198, 199, 200, 201]
# branches ['198->199', '198->201']

import pytest
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
from dataclasses_json.undefined import _CatchAllUndefinedParameters, _UndefinedParameterAction, UndefinedParameterError

@dataclass
class TestClass:
    defined_field: int
    catch_all: Dict[str, Any] = field(default_factory=dict)

    @staticmethod
    def _get_catch_all_field(obj):
        return obj.__dataclass_fields__['catch_all']

def test_handle_to_dict(mocker):
    mocker.patch.object(_CatchAllUndefinedParameters, '_get_catch_all_field', TestClass._get_catch_all_field)
    
    obj = TestClass(defined_field=1, catch_all={'extra_field': 'extra_value'})
    kvs = {'defined_field': 1, 'catch_all': {'extra_field': 'extra_value'}}
    
    result = _CatchAllUndefinedParameters.handle_to_dict(obj, kvs)
    
    assert 'extra_field' in result
    assert result['extra_field'] == 'extra_value'
    assert 'catch_all' not in result
