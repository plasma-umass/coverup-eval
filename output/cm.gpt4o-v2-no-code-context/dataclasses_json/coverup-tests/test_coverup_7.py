# file: dataclasses_json/core.py:118-127
# asked: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}
# gained: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}

import pytest

# Assuming the _decode_letter_case_overrides function is imported from dataclasses_json.core
from dataclasses_json.core import _decode_letter_case_overrides

class MockOverride:
    def __init__(self, letter_case=None):
        self.letter_case = letter_case

def test_decode_letter_case_overrides_no_overrides():
    field_names = ['field_one', 'field_two']
    overrides = {}
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {}

def test_decode_letter_case_overrides_with_overrides(monkeypatch):
    field_names = ['field_one', 'field_two']
    
    def mock_letter_case(name):
        return name.upper()
    
    overrides = {
        'field_one': MockOverride(letter_case=mock_letter_case),
        'field_two': MockOverride(letter_case=None)
    }
    
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {'FIELD_ONE': 'field_one'}

def test_decode_letter_case_overrides_partial_overrides(monkeypatch):
    field_names = ['field_one', 'field_two', 'field_three']
    
    def mock_letter_case(name):
        return name.upper()
    
    overrides = {
        'field_one': MockOverride(letter_case=mock_letter_case),
        'field_two': MockOverride(letter_case=None),
        'field_three': MockOverride(letter_case=mock_letter_case)
    }
    
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {'FIELD_ONE': 'field_one', 'FIELD_THREE': 'field_three'}
