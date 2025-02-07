# file: dataclasses_json/core.py:118-127
# asked: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}
# gained: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}

import pytest

class MockOverride:
    def __init__(self, letter_case=None):
        self.letter_case = letter_case

def mock_letter_case(field_name):
    return field_name.upper()

def test_decode_letter_case_overrides():
    from dataclasses_json.core import _decode_letter_case_overrides

    field_names = ['field1', 'field2', 'field3']
    overrides = {
        'field1': MockOverride(letter_case=mock_letter_case),
        'field2': MockOverride(letter_case=None),
        'field3': None
    }

    result = _decode_letter_case_overrides(field_names, overrides)
    
    assert result == {'FIELD1': 'field1'}

