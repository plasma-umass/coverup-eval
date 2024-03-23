# file mimesis/builtins/pl.py:88-101
# lines [88, 93, 94, 95, 96, 97, 98, 99, 100, 101]
# branches ['98->99', '98->100']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.random import Random

@pytest.fixture
def poland_spec_provider(mocker):
    # Mock the randint to return a sequence that will result in a checksum > 9
    mocker.patch.object(Random, 'randint', side_effect=[8, 9, 2, 3, 4, 5, 6, 7])
    return PolandSpecProvider()

def test_regon_checksum_digit_greater_than_nine(poland_spec_provider):
    regon = poland_spec_provider.regon()
    assert len(regon) == 9
    # Calculate the expected checksum
    regon_coeffs = (8, 9, 2, 3, 4, 5, 6, 7)
    regon_digits = [8, 9, 2, 3, 4, 5, 6, 7]
    sum_v = sum([nc * nd for nc, nd in zip(regon_coeffs, regon_digits)])
    checksum_digit = sum_v % 11
    if checksum_digit > 9:
        checksum_digit = 0
    assert str(checksum_digit) == regon[-1]  # Check if the last digit is the correct checksum
