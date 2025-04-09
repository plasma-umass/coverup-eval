# file string_utils/manipulation.py:637-649
# lines [637, 649]
# branches []

import pytest
from string_utils.manipulation import roman_decode

class __RomanNumbers:
    @staticmethod
    def decode(roman: str) -> int:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman)):
            if i > 0 and roman_numerals[roman[i]] > roman_numerals[roman[i - 1]]:
                result += roman_numerals[roman[i]] - 2 * roman_numerals[roman[i - 1]]
            else:
                result += roman_numerals[roman[i]]
        return result

def test_roman_decode():
    assert roman_decode('III') == 3
    assert roman_decode('IV') == 4
    assert roman_decode('IX') == 9
    assert roman_decode('LVIII') == 58
    assert roman_decode('MCMXCIV') == 1994
