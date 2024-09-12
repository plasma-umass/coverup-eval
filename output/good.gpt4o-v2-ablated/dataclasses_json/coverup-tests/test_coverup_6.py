# file: dataclasses_json/core.py:118-127
# asked: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}
# gained: {"lines": [118, 120, 121, 122, 123, 124, 125, 126, 127], "branches": [[121, 122], [121, 127], [123, 121], [123, 124], [125, 121], [125, 126]]}

import pytest

class MockOverride:
    def __init__(self, letter_case=None):
        self.letter_case = letter_case

def test_decode_letter_case_overrides_all_branches():
    from dataclasses_json.core import _decode_letter_case_overrides

    # Test with no overrides
    field_names = ['field1', 'field2']
    overrides = {}
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {}

    # Test with overrides but no letter_case
    overrides = {
        'field1': MockOverride(),
        'field2': MockOverride()
    }
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {}

    # Test with overrides and letter_case
    overrides = {
        'field1': MockOverride(letter_case=str.upper),
        'field2': MockOverride(letter_case=str.lower)
    }
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {'FIELD1': 'field1', 'field2': 'field2'}

    # Test with some fields having overrides and some not
    overrides = {
        'field1': MockOverride(letter_case=str.upper)
    }
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {'FIELD1': 'field1'}

    # Test with empty field_names
    field_names = []
    result = _decode_letter_case_overrides(field_names, overrides)
    assert result == {}

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Cleanup code if necessary
    yield
    # No state pollution to clean up in this case
