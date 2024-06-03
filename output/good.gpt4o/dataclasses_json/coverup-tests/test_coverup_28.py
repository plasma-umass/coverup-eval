# file dataclasses_json/cfg.py:44-97
# lines [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97]
# branches ['55->56', '55->58', '60->61', '60->63', '63->64', '63->66', '66->67', '66->69', '69->70', '69->79', '70->72', '70->75', '79->80', '79->82', '82->84', '82->94', '84->85', '84->92', '85->86', '85->90', '94->95', '94->97']

import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError
from unittest.mock import Mock
import functools

def test_config():
    # Test with all parameters set
    encoder = Mock()
    decoder = Mock()
    mm_field = Mock()
    letter_case = Mock(return_value="test_case")
    undefined = "RAISE"
    field_name = "test_field"
    exclude = Mock(return_value=True)
    
    metadata = config(
        metadata={},
        encoder=encoder,
        decoder=decoder,
        mm_field=mm_field,
        letter_case=letter_case,
        undefined=undefined,
        field_name=field_name,
        exclude=exclude
    )
    
    lib_metadata = metadata['dataclasses_json']
    
    assert lib_metadata['encoder'] == encoder
    assert lib_metadata['decoder'] == decoder
    assert lib_metadata['mm_field'] == mm_field
    assert lib_metadata['letter_case']("dummy") == "test_case"
    assert lib_metadata['undefined'] == Undefined.RAISE
    assert lib_metadata['exclude']("dummy", "dummy_value") == True

    # Test with invalid undefined parameter
    with pytest.raises(UndefinedParameterError):
        config(undefined="INVALID")

    # Test with letter_case and field_name
    letter_case = Mock(return_value="test_case")
    metadata = config(
        metadata={},
        letter_case=letter_case,
        field_name=field_name
    )
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['letter_case']("dummy") == "test_case"

    # Test with only metadata
    metadata = config(metadata={"existing_key": "existing_value"})
    assert metadata["existing_key"] == "existing_value"
    assert "dataclasses_json" in metadata

    # Test with no parameters
    metadata = config()
    assert "dataclasses_json" in metadata

    # Test with only encoder
    encoder = Mock()
    metadata = config(encoder=encoder)
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['encoder'] == encoder

    # Test with only decoder
    decoder = Mock()
    metadata = config(decoder=decoder)
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['decoder'] == decoder

    # Test with only mm_field
    mm_field = Mock()
    metadata = config(mm_field=mm_field)
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['mm_field'] == mm_field

    # Test with only letter_case
    letter_case = Mock(return_value="test_case")
    metadata = config(letter_case=letter_case)
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['letter_case']("dummy") == "test_case"

    # Test with only undefined
    undefined = "RAISE"
    metadata = config(undefined=undefined)
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['undefined'] == Undefined.RAISE

    # Test with only exclude
    exclude = Mock(return_value=True)
    metadata = config(exclude=exclude)
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['exclude']("dummy", "dummy_value") == True

    # Test with letter_case and field_name without letter_case override
    metadata = config(
        metadata={},
        field_name=field_name
    )
    lib_metadata = metadata['dataclasses_json']
    assert lib_metadata['letter_case']("dummy") == "test_field"
