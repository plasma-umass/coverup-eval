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
    # Test for a specific birth date and male gender
    birth_date = datetime(year=1899, month=12, day=31)
    pesel = poland_provider.pesel(birth_date=birth_date, gender=Gender.MALE)
    assert pesel[2:4] == '92'  # Month should be 12 + 80 for years 1800-1899
    assert int(pesel[-2]) % 2 == 1  # Gender digit for males should be odd

    # Test for a specific birth date and female gender
    birth_date = datetime(year=2100, month=1, day=1)
    pesel = poland_provider.pesel(birth_date=birth_date, gender=Gender.FEMALE)
    assert pesel[2:4] == '41'  # Month should be 1 + 40 for years 2100-2199
    assert int(pesel[-2]) % 2 == 0  # Gender digit for females should be even

    # Test for a specific birth date without gender
    birth_date = datetime(year=2200, month=6, day=15)
    pesel = poland_provider.pesel(birth_date=birth_date)
    assert pesel[2:4] == '66'  # Month should be 6 + 60 for years 2200-2299

    # Test for a specific birth date and unspecified gender
    birth_date = datetime(year=2001, month=2, day=28)
    pesel = poland_provider.pesel(birth_date=birth_date, gender=None)
    assert pesel[0:2] == '01'  # Year should be 01 for years 2000-2099
    assert pesel[2:4] == '22'  # Month should be 2 + 20 for years 2000-2099
    assert int(pesel[-2]) in range(10)  # Gender digit should be in range 0-9
