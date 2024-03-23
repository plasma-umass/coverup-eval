# file mimesis/builtins/pl.py:42-86
# lines [52, 64]
# branches ['51->52', '63->64', '65->68']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.enums import Gender
from datetime import datetime

@pytest.fixture
def poland_provider():
    return PolandSpecProvider()

def test_pesel_birth_date_and_gender_coverage(poland_provider):
    # Test for line 52
    pesel_without_birth_date = poland_provider.pesel()
    assert len(pesel_without_birth_date) == 11

    # Test for line 64 and branch 65->68
    birth_date_for_2100_2199 = datetime(year=2100, month=1, day=1)
    pesel_for_2100_2199 = poland_provider.pesel(birth_date=birth_date_for_2100_2199)
    assert len(pesel_for_2100_2199) == 11
    assert int(pesel_for_2100_2199[2:4]) - 40 == birth_date_for_2100_2199.month

    # Test for branch 65->68
    birth_date_for_2200_2299 = datetime(year=2200, month=1, day=1)
    pesel_for_2200_2299 = poland_provider.pesel(birth_date=birth_date_for_2200_2299)
    assert len(pesel_for_2200_2299) == 11
    assert int(pesel_for_2200_2299[2:4]) - 60 == birth_date_for_2200_2299.month
