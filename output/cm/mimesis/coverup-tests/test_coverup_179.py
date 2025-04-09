# file mimesis/builtins/pl.py:42-86
# lines [52]
# branches ['51->52', '65->68']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.enums import Gender
from datetime import datetime

@pytest.fixture
def poland_provider():
    return PolandSpecProvider()

def test_pesel_birth_date_not_provided(poland_provider, mocker):
    mocker.patch('mimesis.builtins.pl.Datetime.datetime', return_value=datetime(1940, 1, 1))
    pesel = poland_provider.pesel()
    assert len(pesel) == 11
    assert pesel[:2] == '40'

def test_pesel_birth_date_in_22nd_century(poland_provider):
    birth_date = datetime(2200, 1, 1)
    pesel = poland_provider.pesel(birth_date=birth_date)
    assert len(pesel) == 11
    assert pesel[2:4] == '61'  # Month should be incremented by 60 for 22nd century
