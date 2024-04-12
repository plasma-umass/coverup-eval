# file dataclasses_json/core.py:118-127
# lines [118, 120, 121, 122, 123, 124, 125, 126, 127]
# branches ['121->122', '121->127', '123->121', '123->124', '125->121', '125->126']

import pytest
from dataclasses import dataclass
from dataclasses_json.core import _decode_letter_case_overrides

@dataclass
class MockFieldOverride:
    letter_case: callable = None

def test_decode_letter_case_overrides():
    field_names = ['testField', 'anotherField']
    overrides = {
        'testField': MockFieldOverride(letter_case=str.upper),
        'anotherField': MockFieldOverride(letter_case=str.lower)
    }
    
    result = _decode_letter_case_overrides(field_names, overrides)
    
    assert result == {'TESTFIELD': 'testField', 'anotherfield': 'anotherField'}

def test_decode_letter_case_overrides_without_overrides():
    field_names = ['testField', 'anotherField']
    overrides = {}
    
    result = _decode_letter_case_overrides(field_names, overrides)
    
    assert result == {}

def test_decode_letter_case_overrides_with_none_letter_case():
    field_names = ['testField', 'anotherField']
    overrides = {
        'testField': MockFieldOverride(letter_case=None),
        'anotherField': MockFieldOverride(letter_case=None)
    }
    
    result = _decode_letter_case_overrides(field_names, overrides)
    
    assert result == {}
