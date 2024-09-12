# file: string_utils/manipulation.py:52-76
# asked: {"lines": [56, 64], "branches": [[55, 56], [63, 64]]}
# gained: {"lines": [56, 64], "branches": [[55, 56], [63, 64]]}

import pytest
from string_utils.manipulation import __RomanNumbers

@pytest.fixture
def setup_mappings(monkeypatch):
    mappings = [
        {1: 'I', 5: 'V'},
        {1: 'X', 5: 'L'},
        {1: 'C', 5: 'D'},
        {1: 'M', 5: ''}
    ]
    monkeypatch.setattr(__RomanNumbers, '_RomanNumbers__mappings', mappings)

def test_encode_digit_zero(setup_mappings):
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 0) == ''

def test_encode_digit_one_to_three(setup_mappings):
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 1) == 'I'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 2) == 'II'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 3) == 'III'

def test_encode_digit_four(setup_mappings):
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 4) == 'IV'

def test_encode_digit_five(setup_mappings):
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 5) == 'V'

def test_encode_digit_six_to_eight(setup_mappings):
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 6) == 'VI'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 7) == 'VII'
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 8) == 'VIII'

def test_encode_digit_nine(setup_mappings):
    assert __RomanNumbers._RomanNumbers__encode_digit(0, 9) == 'IX'
