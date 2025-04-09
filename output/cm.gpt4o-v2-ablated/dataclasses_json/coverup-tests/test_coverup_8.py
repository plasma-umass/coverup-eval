# file: dataclasses_json/cfg.py:44-97
# asked: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [84, 92], [85, 86], [85, 90], [94, 95], [94, 97]]}
# gained: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [84, 92], [85, 86], [85, 90], [94, 95], [94, 97]]}

import pytest
from dataclasses_json.cfg import config, Undefined, UndefinedParameterError
from unittest.mock import Mock
import functools

def test_config_defaults():
    result = config()
    assert result == {'dataclasses_json': {}}

def test_config_with_metadata():
    metadata = {'existing_key': 'existing_value'}
    result = config(metadata)
    assert result == {'existing_key': 'existing_value', 'dataclasses_json': {}}

def test_config_with_encoder():
    encoder = Mock()
    result = config(encoder=encoder)
    assert result['dataclasses_json']['encoder'] is encoder

def test_config_with_decoder():
    decoder = Mock()
    result = config(decoder=decoder)
    assert result['dataclasses_json']['decoder'] is decoder

def test_config_with_mm_field():
    mm_field = Mock()
    result = config(mm_field=mm_field)
    assert result['dataclasses_json']['mm_field'] is mm_field

def test_config_with_letter_case():
    def letter_case(s: str) -> str:
        return s.upper()
    result = config(letter_case=letter_case)
    assert result['dataclasses_json']['letter_case'] is letter_case

def test_config_with_field_name():
    result = config(field_name='test_field')
    assert 'letter_case' in result['dataclasses_json']
    assert result['dataclasses_json']['letter_case']('ignored') == 'test_field'

def test_config_with_field_name_and_letter_case():
    def letter_case(s: str) -> str:
        return s.upper()
    result = config(field_name='test_field', letter_case=letter_case)
    assert 'letter_case' in result['dataclasses_json']
    assert result['dataclasses_json']['letter_case']('ignored') == 'TEST_FIELD'

def test_config_with_undefined_str():
    result = config(undefined='EXCLUDE')
    assert result['dataclasses_json']['undefined'] == Undefined.EXCLUDE

def test_config_with_invalid_undefined_str():
    with pytest.raises(UndefinedParameterError):
        config(undefined='INVALID')

def test_config_with_undefined_enum():
    result = config(undefined=Undefined.EXCLUDE)
    assert result['dataclasses_json']['undefined'] == Undefined.EXCLUDE

def test_config_with_exclude():
    exclude = Mock()
    result = config(exclude=exclude)
    assert result['dataclasses_json']['exclude'] is exclude
