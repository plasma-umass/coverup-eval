# file string_utils/validation.py:286-305
# lines [286, 305]
# branches []

import pytest
from string_utils.validation import is_camel_case

def test_is_camel_case():
    # Test a valid camel case string
    assert is_camel_case('MyString') == True

    # Test a string that is not camel case because it's all lowercase
    assert is_camel_case('mystring') == False

    # Test a string that is not camel case because it starts with a number
    assert is_camel_case('1MyString') == False

    # Test a string that is not camel case because it contains special characters
    assert is_camel_case('My_String') == False

    # Test a string that is not camel case because it's empty
    assert is_camel_case('') == False

    # Test a string that is not camel case because it's not a string
    assert is_camel_case(123) == False

    # Test a string that is not camel case because it contains spaces
    assert is_camel_case('My String') == False

    # Test a string that is camel case and contains numbers
    assert is_camel_case('MyString123') == True

    # Test a string that is camel case and starts with an uppercase letter
    assert is_camel_case('MyString') == True

    # Test a string that is camel case because it starts with a lowercase letter
    assert is_camel_case('myString') == True

    # Test a string that is not camel case because it's all uppercase
    assert is_camel_case('MYSTRING') == False
