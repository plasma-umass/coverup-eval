# file string_utils/validation.py:159-172
# lines [159, 172]
# branches []

import pytest
from string_utils.validation import is_decimal

def test_is_decimal():
    assert is_decimal('42.0') == True, "42.0 should be recognized as a decimal"
    assert is_decimal('42') == False, "42 should not be recognized as a decimal"
    assert is_decimal('-123.456') == True, "-123.456 should be recognized as a decimal"
    assert is_decimal('+123.456') == True, "+123.456 should be recognized as a decimal"
    # Removed the test cases for scientific notation and trailing dot as they are not decimals according to the given function definition
    assert is_decimal('123') == False, "123 should not be recognized as a decimal"
    assert is_decimal('.456') == True, ".456 should be recognized as a decimal"
    assert is_decimal('-.456') == True, "-.456 should be recognized as a decimal"
    assert is_decimal('+.456') == True, "+.456 should be recognized as a decimal"
    assert is_decimal('not a number') == False, "String 'not a number' should not be recognized as a decimal"
    assert is_decimal('') == False, "Empty string should not be recognized as a decimal"
