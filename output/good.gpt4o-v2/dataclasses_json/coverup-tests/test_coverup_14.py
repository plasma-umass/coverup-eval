# file: dataclasses_json/cfg.py:44-97
# asked: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [84, 92], [85, 86], [85, 90], [94, 95], [94, 97]]}
# gained: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [85, 86], [85, 90], [94, 95], [94, 97]]}

import pytest
from dataclasses_json.cfg import config
from dataclasses_json.undefined import Undefined, UndefinedParameterError
from marshmallow.fields import Field as MarshmallowField

def test_config_with_all_parameters():
    def encoder(x):
        return str(x)
    
    def decoder(x):
        return int(x)
    
    def letter_case(s):
        return s.upper()
    
    def exclude(field_name, value):
        return field_name == "exclude_me"
    
    metadata = {
        "existing_key": "existing_value"
    }
    
    result = config(
        metadata=metadata,
        encoder=encoder,
        decoder=decoder,
        mm_field=MarshmallowField(),
        letter_case=letter_case,
        undefined="RAISE",
        field_name="test_field",
        exclude=exclude
    )
    
    assert result["existing_key"] == "existing_value"
    lib_metadata = result["dataclasses_json"]
    assert lib_metadata["encoder"] == encoder
    assert lib_metadata["decoder"] == decoder
    assert isinstance(lib_metadata["mm_field"], MarshmallowField)
    assert lib_metadata["letter_case"]("test") == "TEST_FIELD"
    assert lib_metadata["undefined"] == Undefined.RAISE
    assert lib_metadata["exclude"]("exclude_me", None) == True
    assert lib_metadata["exclude"]("keep_me", None) == False

def test_config_with_invalid_undefined():
    with pytest.raises(UndefinedParameterError):
        config(undefined="INVALID")

def test_config_with_partial_parameters():
    def encoder(x):
        return str(x)
    
    metadata = {}
    
    result = config(
        metadata=metadata,
        encoder=encoder
    )
    
    lib_metadata = result["dataclasses_json"]
    assert lib_metadata["encoder"] == encoder
    assert "decoder" not in lib_metadata
    assert "mm_field" not in lib_metadata
    assert "letter_case" not in lib_metadata
    assert "undefined" not in lib_metadata
    assert "exclude" not in lib_metadata

def test_config_with_none_metadata():
    result = config()
    assert "dataclasses_json" in result
    assert result["dataclasses_json"] == {}

def test_config_with_field_name_and_letter_case():
    def letter_case(s):
        return s.upper()
    
    result = config(
        field_name="test_field",
        letter_case=letter_case
    )
    
    lib_metadata = result["dataclasses_json"]
    assert lib_metadata["letter_case"]("test") == "TEST_FIELD"

def test_config_with_field_name_without_letter_case():
    result = config(
        field_name="test_field"
    )
    
    lib_metadata = result["dataclasses_json"]
    assert lib_metadata["letter_case"]("test") == "test_field"
