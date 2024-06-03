# file dataclasses_json/core.py:118-127
# lines []
# branches ['125->121']

import pytest
from unittest.mock import Mock

# Assuming the function is imported from dataclasses_json.core
from dataclasses_json.core import _decode_letter_case_overrides

def test_decode_letter_case_overrides_with_and_without_letter_case(mocker):
    # Mocking the letter_case function
    mock_letter_case = Mock()
    mock_letter_case.side_effect = lambda x: x.upper()

    # Creating mock overrides
    mock_override_with_case = Mock()
    mock_override_with_case.letter_case = mock_letter_case

    mock_override_without_case = Mock()
    mock_override_without_case.letter_case = None

    # Field names and overrides
    field_names = ['field_one', 'field_two', 'field_three']
    overrides = {
        'field_one': mock_override_with_case,
        'field_two': mock_override_without_case,
        'field_three': None
    }

    # Call the function
    result = _decode_letter_case_overrides(field_names, overrides)

    # Assertions
    assert result == {'FIELD_ONE': 'field_one'}
    mock_letter_case.assert_called_once_with('field_one')

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
