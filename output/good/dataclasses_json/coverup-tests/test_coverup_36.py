# file dataclasses_json/cfg.py:44-97
# lines [61, 64, 67, 70, 71, 72, 73, 75, 76, 77, 80, 85, 86, 87, 88, 89, 90, 95]
# branches ['55->58', '60->61', '63->64', '66->67', '69->70', '70->72', '70->75', '79->80', '82->94', '84->85', '85->86', '85->90', '94->95']

import pytest
from dataclasses_json.cfg import config
from dataclasses_json.undefined import Undefined, UndefinedParameterError
from marshmallow.fields import Field as MarshmallowField
from typing import Callable

def test_config_full_coverage():
    # Test encoder branch
    def dummy_encoder(value):
        return str(value)
    
    # Test decoder branch
    def dummy_decoder(value):
        return int(value)
    
    # Test mm_field branch
    dummy_mm_field = MarshmallowField()
    
    # Test letter_case branch with field_name
    def dummy_letter_case(value):
        return value.upper()
    
    # Test undefined branch with invalid string
    with pytest.raises(UndefinedParameterError):
        config(undefined="invalid")
    
    # Test undefined branch with valid string
    config(undefined="include")
    
    # Test exclude branch
    def dummy_exclude(field_name, field_type):
        return True
    
    # Execute all branches
    result = config(
        encoder=dummy_encoder,
        decoder=dummy_decoder,
        mm_field=dummy_mm_field,
        letter_case=dummy_letter_case,
        field_name="test_field",
        undefined="include",
        exclude=dummy_exclude
    )
    
    # Assertions to verify postconditions
    assert 'dataclasses_json' in result
    lib_metadata = result['dataclasses_json']
    assert lib_metadata['encoder'] == dummy_encoder
    assert lib_metadata['decoder'] == dummy_decoder
    assert lib_metadata['mm_field'] == dummy_mm_field
    assert callable(lib_metadata['letter_case'])
    assert lib_metadata['letter_case']("test") == "TEST_FIELD"
    assert lib_metadata['undefined'] == Undefined.INCLUDE
    assert lib_metadata['exclude'] == dummy_exclude
