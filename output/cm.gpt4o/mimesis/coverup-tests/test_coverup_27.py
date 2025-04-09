# file mimesis/builtins/pl.py:42-86
# lines [42, 43, 50, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 73, 74, 75, 76, 78, 80, 81, 82, 83, 84, 85, 86]
# branches ['51->52', '51->54', '59->60', '59->61', '61->62', '61->63', '63->64', '63->65', '65->66', '65->68', '73->74', '73->75', '75->76', '75->78']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.enums import Gender
from datetime import datetime

@pytest.fixture
def poland_spec_provider():
    return PolandSpecProvider()

def test_pesel_with_birth_date(poland_spec_provider):
    birth_date = datetime(1990, 5, 15)
    pesel = poland_spec_provider.pesel(birth_date=birth_date)
    assert len(pesel) == 11
    assert pesel[:2] == '90'
    assert pesel[2:4] == '05'
    assert pesel[4:6] == '15'

def test_pesel_with_gender_male(poland_spec_provider):
    pesel = poland_spec_provider.pesel(gender=Gender.MALE)
    assert len(pesel) == 11
    assert int(pesel[9]) % 2 == 1

def test_pesel_with_gender_female(poland_spec_provider):
    pesel = poland_spec_provider.pesel(gender=Gender.FEMALE)
    assert len(pesel) == 11
    assert int(pesel[9]) % 2 == 0

def test_pesel_with_year_1800(poland_spec_provider):
    birth_date = datetime(1885, 5, 15)
    pesel = poland_spec_provider.pesel(birth_date=birth_date)
    assert len(pesel) == 11
    assert pesel[2:4] == '85'
    assert pesel[4:6] == '15'
    assert int(pesel[2]) >= 8

def test_pesel_with_year_2000(poland_spec_provider):
    birth_date = datetime(2005, 5, 15)
    pesel = poland_spec_provider.pesel(birth_date=birth_date)
    assert len(pesel) == 11
    assert pesel[2:4] == '25'
    assert pesel[4:6] == '15'

def test_pesel_with_year_2100(poland_spec_provider):
    birth_date = datetime(2105, 5, 15)
    pesel = poland_spec_provider.pesel(birth_date=birth_date)
    assert len(pesel) == 11
    assert pesel[2:4] == '45'
    assert pesel[4:6] == '15'

def test_pesel_with_year_2200(poland_spec_provider):
    birth_date = datetime(2205, 5, 15)
    pesel = poland_spec_provider.pesel(birth_date=birth_date)
    assert len(pesel) == 11
    assert pesel[2:4] == '65'
    assert pesel[4:6] == '15'
