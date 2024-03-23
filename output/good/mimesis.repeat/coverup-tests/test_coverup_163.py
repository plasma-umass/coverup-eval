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

def test_pesel_year_2200_to_2299(poland_provider, mocker):
    mocker.patch('mimesis.builtins.pl.Datetime.datetime', return_value=datetime(2200, 1, 1))
    pesel = poland_provider.pesel()
    assert len(pesel) == 11
    assert pesel[2:4] == '61'  # Month should be 01 + 60 for years 2200-2299
