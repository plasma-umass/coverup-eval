# file string_utils/manipulation.py:282-297
# lines [282, 294, 295, 297]
# branches ['294->295', '294->297']

import pytest
from string_utils.manipulation import reverse
from string_utils.errors import InvalidInputError

def test_reverse_valid_string():
    assert reverse('hello') == 'olleh', "The reverse function did not return the expected reversed string."

def test_reverse_empty_string():
    assert reverse('') == '', "The reverse function should return an empty string for an empty input."

def test_reverse_invalid_input():
    with pytest.raises(InvalidInputError):
        reverse(123)  # This is not a string, should raise InvalidInputError
