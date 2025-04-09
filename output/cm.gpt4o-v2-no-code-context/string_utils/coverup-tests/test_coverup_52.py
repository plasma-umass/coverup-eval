# file: string_utils/manipulation.py:116-156
# asked: {"lines": [119], "branches": [[118, 119]]}
# gained: {"lines": [119], "branches": [[118, 119]]}

import pytest
from string_utils.manipulation import __RomanNumbers

def test_decode_empty_string():
    with pytest.raises(ValueError, match='Input must be a non empty string'):
        __RomanNumbers.decode('')

def test_decode_non_string():
    with pytest.raises(ValueError, match='Input must be a non empty string'):
        __RomanNumbers.decode(None)

def test_decode_valid_roman():
    assert __RomanNumbers.decode('IX') == 9
    assert __RomanNumbers.decode('XII') == 12
    assert __RomanNumbers.decode('XXI') == 21

def test_decode_lowercase_roman():
    assert __RomanNumbers.decode('ix') == 9
    assert __RomanNumbers.decode('xii') == 12
    assert __RomanNumbers.decode('xxi') == 21

def test_decode_complex_roman():
    assert __RomanNumbers.decode('MCMXCIV') == 1994
    assert __RomanNumbers.decode('MMXX') == 2020
    assert __RomanNumbers.decode('CDXLIV') == 444
