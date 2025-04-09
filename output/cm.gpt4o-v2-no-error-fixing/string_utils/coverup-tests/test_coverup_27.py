# file: string_utils/manipulation.py:52-76
# asked: {"lines": [52, 53, 55, 56, 59, 60, 63, 64, 67, 68, 71, 72, 73, 76], "branches": [[55, 56], [55, 59], [59, 60], [59, 63], [63, 64], [63, 67], [67, 68], [67, 71], [71, 72], [71, 76]]}
# gained: {"lines": [52, 53, 55, 56, 59, 60, 63, 64, 67, 68, 71, 72, 73, 76], "branches": [[55, 56], [55, 59], [59, 60], [59, 63], [63, 64], [63, 67], [67, 68], [67, 71], [71, 72], [71, 76]]}

import pytest
from string_utils.manipulation import __RomanNumbers

def test_encode_digit_zero():
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 0) == ''

def test_encode_digit_one_to_three():
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 1) == 'I'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 2) == 'II'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 3) == 'III'

def test_encode_digit_four():
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 4) == 'IV'

def test_encode_digit_five():
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 5) == 'V'

def test_encode_digit_six_to_eight():
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 6) == 'VI'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 7) == 'VII'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 8) == 'VIII'

def test_encode_digit_nine():
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 9) == 'IX'

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: monkeypatch any state if necessary
    yield
    # Teardown: clean up any state if necessary
