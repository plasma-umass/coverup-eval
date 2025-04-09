# file: dataclasses_json/cfg.py:44-97
# asked: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [84, 92], [85, 86], [85, 90], [94, 95], [94, 97]]}
# gained: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [85, 86], [85, 90], [94, 95], [94, 97]]}

import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError
from unittest.mock import Mock
import functools

def test_config_with_all_parameters():
    metadata = {}
    encoder = Mock()
    decoder = Mock()
    mm_field = Mock()
    letter_case = str.upper
    undefined = 'RAISE'
    field_name = 'test_field'
    exclude = Mock()

    result = config(metadata, encoder=encoder, decoder=decoder, mm_field=mm_field,
                    letter_case=letter_case, undefined=undefined, field_name=field_name,
                    exclude=exclude)

    assert 'dataclasses_json' in result
    lib_metadata = result['dataclasses_json']
    assert lib_metadata['encoder'] == encoder
    assert lib_metadata['decoder'] == decoder
    assert lib_metadata['mm_field'] == mm_field
    assert lib_metadata['letter_case']('test_field') == 'TEST_FIELD'
    assert lib_metadata['undefined'] == Undefined.RAISE
    assert lib_metadata['exclude'] == exclude

def test_config_with_invalid_undefined():
    with pytest.raises(UndefinedParameterError):
        config(undefined='INVALID')

def test_config_with_field_name_and_letter_case():
    metadata = {}
    field_name = 'test_field'
    letter_case = str.upper

    result = config(metadata, field_name=field_name, letter_case=letter_case)

    assert 'dataclasses_json' in result
    lib_metadata = result['dataclasses_json']
    assert lib_metadata['letter_case']('ignored') == 'TEST_FIELD'

def test_config_with_none_parameters():
    result = config()

    assert 'dataclasses_json' in result
    lib_metadata = result['dataclasses_json']
    assert lib_metadata == {}

def test_config_with_partial_parameters():
    metadata = {}
    encoder = Mock()
    field_name = 'test_field'

    result = config(metadata, encoder=encoder, field_name=field_name)

    assert 'dataclasses_json' in result
    lib_metadata = result['dataclasses_json']
    assert lib_metadata['encoder'] == encoder
    assert lib_metadata['letter_case']('ignored') == 'test_field'
