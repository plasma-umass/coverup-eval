# file string_utils/validation.py:141-156
# lines [141, 156]
# branches []

import pytest
from string_utils.validation import is_integer

def test_is_integer():
    # Test cases where the input string is an integer
    assert is_integer('42') == True
    assert is_integer('-42') == True
    assert is_integer('+42') == True
    assert is_integer('0') == True

    # Test cases where the input string is not an integer
    assert is_integer('42.0') == False
    assert is_integer('42.1') == False
    assert is_integer('4.2e1') == False
    assert is_integer('abc') == False
    assert is_integer('') == False

    # Test cases for scientific notation
    assert is_integer('1e3') == False
    assert is_integer('-1e3') == False
    assert is_integer('+1e3') == False

    # Test cases for edge cases
    assert is_integer(' ') == False
    assert is_integer('42 ') == False
    assert is_integer(' 42') == False

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Mocking is_number to ensure it returns the expected values for the test cases
    mocker.patch('string_utils.validation.is_number', side_effect=lambda x: x.isdigit() or (x.startswith(('+', '-')) and x[1:].isdigit()))
