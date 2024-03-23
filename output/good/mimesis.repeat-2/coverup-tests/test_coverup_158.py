# file mimesis/builtins/pl.py:88-101
# lines [93, 94, 95, 96, 97, 98, 99, 100, 101]
# branches ['98->99', '98->100']

import pytest
from mimesis.builtins.pl import PolandSpecProvider

def test_regon_checksum_digit_less_than_10(mocker):
    provider = PolandSpecProvider()
    mocker.patch.object(provider.random, 'randint', side_effect=[1, 2, 3, 4, 5, 6, 7, 8])
    regon = provider.regon()
    assert len(regon) == 9
    assert regon[-1] != '0'  # Ensures that checksum digit is not 0

def test_regon_checksum_digit_equal_to_10(mocker):
    provider = PolandSpecProvider()
    # Side effect values are chosen to make the sum_v % 11 equal to 10
    mocker.patch.object(provider.random, 'randint', side_effect=[0, 0, 0, 0, 0, 0, 0, 3])
    regon = provider.regon()
    assert len(regon) == 9
    assert regon[-1] == '0'  # Ensures that checksum digit is 0 when sum_v % 11 equals 10
