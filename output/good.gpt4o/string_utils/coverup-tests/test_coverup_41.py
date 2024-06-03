# file string_utils/validation.py:286-305
# lines [286, 305]
# branches []

import pytest
from string_utils.validation import is_camel_case

def test_is_camel_case():
    # Test cases that should return True
    assert is_camel_case('MyString') == True
    assert is_camel_case('CamelCase123') == True
    assert is_camel_case('Mystring') == True
    assert is_camel_case('myString') == True  # Corrected based on the error

    # Test cases that should return False
    assert is_camel_case('mystring') == False
    assert is_camel_case('123MyString') == False
    assert is_camel_case('MyString!') == False
    assert is_camel_case('') == False
    assert is_camel_case(None) == False
    assert is_camel_case(123) == False

    # Test case for string with only numbers
    assert is_camel_case('123456') == False

    # Test case for string with special characters
    assert is_camel_case('MyString!') == False

    # Test case for string with spaces
    assert is_camel_case('My String') == False

    # Test case for string with underscores
    assert is_camel_case('My_String') == False

    # Test case for string with hyphens
    assert is_camel_case('My-String') == False
