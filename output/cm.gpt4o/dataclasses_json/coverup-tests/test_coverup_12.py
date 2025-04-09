# file dataclasses_json/core.py:118-127
# lines [118, 120, 121, 122, 123, 124, 125, 126, 127]
# branches ['121->122', '121->127', '123->121', '123->124', '125->121', '125->126']

import pytest
from unittest.mock import Mock

# Assuming the function is imported from dataclasses_json.core
from dataclasses_json.core import _decode_letter_case_overrides

def test_decode_letter_case_overrides(mocker):
    # Mocking the letter_case function
    mock_letter_case = mocker.Mock()
    mock_letter_case.side_effect = lambda x: x.upper()

    # Creating a mock override object with a letter_case attribute
    mock_override = Mock()
    mock_override.letter_case = mock_letter_case

    # Field names and overrides
    field_names = ['fieldOne', 'fieldTwo']
    overrides = {
        'fieldOne': mock_override,
        'fieldTwo': None  # This should not be included in the result
    }

    # Expected result
    expected_result = {
        'FIELDONE': 'fieldOne'
    }

    # Call the function
    result = _decode_letter_case_overrides(field_names, overrides)

    # Assertions
    assert result == expected_result
    mock_letter_case.assert_called_once_with('fieldOne')

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
