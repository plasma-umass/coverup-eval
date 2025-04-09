# file: dataclasses_json/cfg.py:44-97
# asked: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [84, 92], [85, 86], [85, 90], [94, 95], [94, 97]]}
# gained: {"lines": [44, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 70, 71, 72, 73, 75, 76, 77, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 92, 94, 95, 97], "branches": [[55, 56], [55, 58], [60, 61], [60, 63], [63, 64], [63, 66], [66, 67], [66, 69], [69, 70], [69, 79], [70, 72], [70, 75], [79, 80], [79, 82], [82, 84], [82, 94], [84, 85], [84, 92], [85, 86], [85, 90], [94, 95], [94, 97]]}

import pytest
from dataclasses_json.cfg import config
from dataclasses_json.undefined import Undefined, UndefinedParameterError
from marshmallow.fields import Field as MarshmallowField

def test_config_no_metadata():
    result = config()
    assert result == {'dataclasses_json': {}}

def test_config_with_metadata():
    metadata = {'existing': 'data'}
    result = config(metadata)
    assert result == {'existing': 'data', 'dataclasses_json': {}}

def test_config_with_encoder():
    encoder = lambda x: x
    result = config(encoder=encoder)
    assert result['dataclasses_json']['encoder'] is encoder

def test_config_with_decoder():
    decoder = lambda x: x
    result = config(decoder=decoder)
    assert result['dataclasses_json']['decoder'] is decoder

def test_config_with_mm_field():
    mm_field = MarshmallowField()
    result = config(mm_field=mm_field)
    assert result['dataclasses_json']['mm_field'] is mm_field

def test_config_with_letter_case():
    letter_case = lambda x: x.upper()
    result = config(letter_case=letter_case)
    assert result['dataclasses_json']['letter_case'] is letter_case

def test_config_with_field_name():
    result = config(field_name='test_field')
    assert result['dataclasses_json']['letter_case']('dummy') == 'test_field'

def test_config_with_field_name_and_letter_case():
    letter_case = lambda x: x.upper()
    result = config(field_name='test_field', letter_case=letter_case)
    assert result['dataclasses_json']['letter_case']('dummy') == 'TEST_FIELD'

def test_config_with_undefined():
    result = config(undefined=Undefined.EXCLUDE)
    assert result['dataclasses_json']['undefined'] == Undefined.EXCLUDE

def test_config_with_undefined_str():
    result = config(undefined='exclude')
    assert result['dataclasses_json']['undefined'] == Undefined.EXCLUDE

def test_config_with_invalid_undefined_str():
    with pytest.raises(UndefinedParameterError):
        config(undefined='invalid')

def test_config_with_exclude():
    exclude = lambda x, y: True
    result = config(exclude=exclude)
    assert result['dataclasses_json']['exclude'] is exclude
