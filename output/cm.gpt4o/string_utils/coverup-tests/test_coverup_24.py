# file string_utils/manipulation.py:500-526
# lines [500, 523, 524, 526]
# branches ['523->524', '523->526']

import pytest
from string_utils.manipulation import booleanize, InvalidInputError

def test_booleanize():
    # Test cases for positive boolean values
    assert booleanize('true') is True
    assert booleanize('TRUE') is True
    assert booleanize('1') is True
    assert booleanize('yes') is True
    assert booleanize('YES') is True
    assert booleanize('y') is True
    assert booleanize('Y') is True

    # Test cases for negative boolean values
    assert booleanize('false') is False
    assert booleanize('0') is False
    assert booleanize('no') is False
    assert booleanize('n') is False
    assert booleanize('nope') is False
    assert booleanize('') is False

    # Test case for invalid input
    with pytest.raises(InvalidInputError):
        booleanize(123)  # Non-string input

    with pytest.raises(InvalidInputError):
        booleanize(None)  # None input

# Mocking is_string function to ensure it is called correctly
def test_booleanize_is_string(mocker):
    mock_is_string = mocker.patch('string_utils.manipulation.is_string', return_value=True)
    assert booleanize('true') is True
    mock_is_string.assert_called_once_with('true')

    mock_is_string = mocker.patch('string_utils.manipulation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        booleanize('true')
    mock_is_string.assert_called_once_with('true')
