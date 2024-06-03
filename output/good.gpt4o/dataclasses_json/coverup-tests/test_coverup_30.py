# file dataclasses_json/cfg.py:44-97
# lines []
# branches ['84->92']

import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError

def test_config_with_invalid_undefined_string():
    metadata = {}
    invalid_undefined = "invalid_action"
    
    with pytest.raises(UndefinedParameterError) as excinfo:
        config(metadata, undefined=invalid_undefined)
    
    assert "Invalid undefined parameter action" in str(excinfo.value)

def test_config_with_valid_undefined_string():
    metadata = {}
    valid_undefined = "EXCLUDE"
    
    result = config(metadata, undefined=valid_undefined)
    
    assert 'dataclasses_json' in result
    assert 'undefined' in result['dataclasses_json']
    assert result['dataclasses_json']['undefined'] == Undefined.EXCLUDE

def test_config_with_undefined_enum():
    metadata = {}
    undefined_enum = Undefined.EXCLUDE
    
    result = config(metadata, undefined=undefined_enum)
    
    assert 'dataclasses_json' in result
    assert 'undefined' in result['dataclasses_json']
    assert result['dataclasses_json']['undefined'] == undefined_enum
