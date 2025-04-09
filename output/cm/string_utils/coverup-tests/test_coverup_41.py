# file string_utils/validation.py:516-529
# lines [516, 529]
# branches []

import pytest
from string_utils.validation import is_isogram

def test_is_isogram():
    # Test with an isogram string
    assert is_isogram('dermatoglyphics') == True, "Expected 'dermatoglyphics' to be an isogram"

    # Test with a non-isogram string
    assert is_isogram('hello') == False, "Expected 'hello' to not be an isogram"

    # Test with an empty string
    assert is_isogram('') == False, "Expected '' to not be an isogram"

    # Test with a string that has non-letter characters
    assert is_isogram('!@#$%^&*()') == True, "Expected '!@#$%^&*()' to be an isogram"

    # Test with a string that has mixed case letters, considering case sensitivity
    assert is_isogram('Python') == True, "Expected 'Python' to be an isogram"
    assert is_isogram('Pythonn') == False, "Expected 'Pythonn' to not be an isogram"
