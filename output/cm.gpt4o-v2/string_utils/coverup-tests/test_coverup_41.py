# file: string_utils/validation.py:286-305
# asked: {"lines": [286, 305], "branches": []}
# gained: {"lines": [286, 305], "branches": []}

import pytest
from string_utils.validation import is_camel_case

def test_is_camel_case():
    # Test cases that should return True
    assert is_camel_case('MyString') == True
    assert is_camel_case('camelCase') == True
    assert is_camel_case('anotherExample123') == True
    assert is_camel_case('Mystring') == True  # Corrected based on the regex pattern

    # Test cases that should return False
    assert is_camel_case('mystring') == False
    assert is_camel_case('123MyString') == False
    assert is_camel_case('') == False
    assert is_camel_case(' ') == False
    assert is_camel_case(None) == False
    assert is_camel_case('ALLUPPERCASE') == False
    assert is_camel_case('alllowercase') == False
    assert is_camel_case('123') == False
    assert is_camel_case('CamelCase!') == False
