# file mimesis/builtins/pl.py:42-86
# lines [42, 43, 50, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 80, 81, 82, 83, 84, 85, 86]
# branches ['51->52', '51->54', '59->60', '59->61', '61->62', '61->63', '63->64', '63->65', '65->66', '65->68', '73->74', '73->75', '75->76', '75->78']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.enums import Gender
from datetime import datetime

@pytest.fixture
def poland_provider():
    return PolandSpecProvider()

def test_pesel_birth_date_and_gender(poland_provider):
    # Test for a birth date in the 1800s and male gender
    birth_date_1800s = datetime(year=1890, month=5, day=23)
    pesel_1800s_male = poland_provider.pesel(birth_date=birth_date_1800s, gender=Gender.MALE)
    assert pesel_1800s_male[2] == '8'  # Month should be 80 + original month (5)
    assert int(pesel_1800s_male[-2]) % 2 == 1  # Gender digit for male should be odd

    # Test for a birth date in the 2200s and female gender
    birth_date_2200s = datetime(year=2250, month=4, day=15)
    pesel_2200s_female = poland_provider.pesel(birth_date=birth_date_2200s, gender=Gender.FEMALE)
    assert pesel_2200s_female[2] == '6'  # Month should be 60 + original month (4)
    assert int(pesel_2200s_female[-2]) % 2 == 0  # Gender digit for female should be even

    # Test for a birth date in the 2000s and unspecified gender
    birth_date_2000s = datetime(year=2010, month=1, day=1)
    pesel_2000s_unspecified = poland_provider.pesel(birth_date=birth_date_2000s)
    assert pesel_2000s_unspecified[2] == '2'  # Month should be 20 + original month (1)
    # No specific assertion for gender digit since it can be any

    # Test for a birth date in the 2100s and unspecified gender
    birth_date_2100s = datetime(year=2150, month=12, day=31)
    pesel_2100s_unspecified = poland_provider.pesel(birth_date=birth_date_2100s)
    assert pesel_2100s_unspecified[2] == '5'  # Month should be 40 + original month (12)
    # No specific assertion for gender digit since it can be any
