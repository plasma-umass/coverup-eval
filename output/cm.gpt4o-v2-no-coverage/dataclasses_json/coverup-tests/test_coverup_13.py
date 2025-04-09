# file: dataclasses_json/core.py:118-127
# asked: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}
# gained: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}

import pytest

class MockOverride:
    def __init__(self, letter_case=None):
        self.letter_case = letter_case

def test_decode_letter_case_overrides_all_cases():
    from dataclasses_json.core import _decode_letter_case_overrides

    # Test data
    field_names = ['fieldOne', 'fieldTwo', 'fieldThree']
    overrides = {
        'fieldOne': MockOverride(str.upper),
        'fieldTwo': MockOverride(str.lower),
        'fieldThree': MockOverride(None)
    }

    # Expected result
    expected = {
        'FIELDONE': 'fieldOne',
        'fieldtwo': 'fieldTwo'
    }

    # Run the function
    result = _decode_letter_case_overrides(field_names, overrides)

    # Assertions
    assert result == expected

def test_decode_letter_case_overrides_no_overrides():
    from dataclasses_json.core import _decode_letter_case_overrides

    # Test data
    field_names = ['fieldOne', 'fieldTwo']
    overrides = {}

    # Expected result
    expected = {}

    # Run the function
    result = _decode_letter_case_overrides(field_names, overrides)

    # Assertions
    assert result == expected

def test_decode_letter_case_overrides_partial_overrides():
    from dataclasses_json.core import _decode_letter_case_overrides

    # Test data
    field_names = ['fieldOne', 'fieldTwo']
    overrides = {
        'fieldOne': MockOverride(str.upper)
    }

    # Expected result
    expected = {
        'FIELDONE': 'fieldOne'
    }

    # Run the function
    result = _decode_letter_case_overrides(field_names, overrides)

    # Assertions
    assert result == expected

def test_decode_letter_case_overrides_none_letter_case():
    from dataclasses_json.core import _decode_letter_case_overrides

    # Test data
    field_names = ['fieldOne', 'fieldTwo']
    overrides = {
        'fieldOne': MockOverride(None)
    }

    # Expected result
    expected = {}

    # Run the function
    result = _decode_letter_case_overrides(field_names, overrides)

    # Assertions
    assert result == expected
