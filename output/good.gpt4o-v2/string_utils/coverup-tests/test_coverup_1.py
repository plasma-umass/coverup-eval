# file: string_utils/validation.py:159-172
# asked: {"lines": [159, 172], "branches": []}
# gained: {"lines": [159, 172], "branches": []}

import pytest
from string_utils.validation import is_decimal

def test_is_decimal():
    assert is_decimal('42.0') == True
    assert is_decimal('42') == False
    assert is_decimal('-42.0') == True
    assert is_decimal('+42.0') == True
    assert is_decimal('4.2e1') == True
    assert is_decimal('4e1') == False
    assert is_decimal('abc') == False
    assert is_decimal('') == False
