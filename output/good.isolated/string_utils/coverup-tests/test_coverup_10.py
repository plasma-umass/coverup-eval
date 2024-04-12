# file string_utils/manipulation.py:116-156
# lines [116, 117, 118, 119, 122, 125, 128, 131, 133, 136, 142, 145, 146, 152, 154, 156]
# branches ['118->119', '118->122', '131->133', '131->156', '145->146', '145->152']

import pytest
from string_utils.manipulation import __RomanNumbers

def test_roman_numbers_decode():
    assert __RomanNumbers.decode('III') == 3
    assert __RomanNumbers.decode('IV') == 4
    assert __RomanNumbers.decode('IX') == 9
    assert __RomanNumbers.decode('LVIII') == 58
    assert __RomanNumbers.decode('MCMXCIV') == 1994

    with pytest.raises(ValueError):
        __RomanNumbers.decode('')

    with pytest.raises(ValueError):
        __RomanNumbers.decode('123')

    with pytest.raises(ValueError):
        __RomanNumbers.decode(None)
