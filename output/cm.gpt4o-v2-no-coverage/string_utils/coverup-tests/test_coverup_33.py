# file: string_utils/validation.py:286-305
# asked: {"lines": [286, 305], "branches": []}
# gained: {"lines": [286, 305], "branches": []}

import pytest
from string_utils.validation import is_camel_case
from string_utils._regex import CAMEL_CASE_TEST_RE

def test_is_camel_case_valid():
    assert is_camel_case('MyString') == True
    assert is_camel_case('myString123') == True

def test_is_camel_case_invalid():
    assert is_camel_case('mystring') == False
    assert is_camel_case('MYSTRING') == False
    assert is_camel_case('myString!') == False
    assert is_camel_case('123MyString') == False

def test_is_camel_case_non_string():
    assert is_camel_case(None) == False
    assert is_camel_case(123) == False
    assert is_camel_case(['MyString']) == False
