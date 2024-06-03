# file string_utils/validation.py:516-529
# lines [516, 529]
# branches []

import pytest
from string_utils.validation import is_isogram

def test_is_isogram(mocker):
    # Mocking is_full_string to control its behavior
    mock_is_full_string = mocker.patch('string_utils.validation.is_full_string')

    # Test case where is_full_string returns False
    mock_is_full_string.return_value = False
    assert not is_isogram('dermatoglyphics')

    # Test case where is_full_string returns True and input is an isogram
    mock_is_full_string.return_value = True
    assert is_isogram('dermatoglyphics')

    # Test case where is_full_string returns True and input is not an isogram
    assert not is_isogram('hello')

    # Test case where input is not a string
    mock_is_full_string.return_value = False
    assert not is_isogram(12345)
