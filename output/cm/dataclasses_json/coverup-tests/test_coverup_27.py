# file dataclasses_json/undefined.py:133-167
# lines [133, 134, 135, 136, 137, 138, 140, 142, 143, 144, 145, 148, 149, 150, 151, 152, 154, 155, 156, 158, 160, 161, 162, 164, 166, 167]
# branches ['140->142', '140->164', '148->149', '148->150', '150->151', '150->152', '152->154', '152->158', '155->156', '155->166']

import pytest
from dataclasses import dataclass, field
from typing import Dict, Any
from dataclasses_json.undefined import UndefinedParameterError, _CatchAllUndefinedParameters
from dataclasses_json import CatchAll

@dataclass
class MockDataClassWithCatchAll:
    catch_all: CatchAll = field(default_factory=dict)

def test_catch_all_undefined_parameters_handle_from_dict():
    # Test case where catch_all field already has a parsed dict and unknown fields are present
    cls = MockDataClassWithCatchAll
    kvs = {'catch_all': {'existing': 1}, 'unknown_field': 2}
    result = _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
    assert result == {'catch_all': {'existing': 1, 'unknown_field': 2}}

    # Test case where catch_all field has the default value and unknown fields are present
    cls = MockDataClassWithCatchAll
    kvs = {'catch_all': {}, 'unknown_field': 2}
    result = _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
    assert result == {'catch_all': {'unknown_field': 2}}

    # Test case where catch_all field has the default value and no unknown fields are present
    cls = MockDataClassWithCatchAll
    kvs = {'catch_all': {}}
    result = _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
    assert result == {'catch_all': {}}

    # Test case where catch_all field is not in known and unknown fields are present
    cls = MockDataClassWithCatchAll
    kvs = {'unknown_field': 2}
    result = _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
    assert result == {'catch_all': {'unknown_field': 2}}

    # Test case where catch_all field is not in known and no unknown fields are present
    cls = MockDataClassWithCatchAll
    kvs = {}
    result = _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
    assert result == {'catch_all': {}}

    # Test case where catch_all field has a non-dict non-default value
    cls = MockDataClassWithCatchAll
    kvs = {'catch_all': 'non_default_value'}
    with pytest.raises(UndefinedParameterError) as exc_info:
        _CatchAllUndefinedParameters.handle_from_dict(cls, kvs)
    assert "Received input field with same name as catch-all field" in str(exc_info.value)
