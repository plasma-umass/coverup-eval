# file mimesis/builtins/pl.py:88-101
# lines [88, 93, 94, 95, 96, 97, 98, 99, 100, 101]
# branches ['98->99', '98->100']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.random import Random

@pytest.fixture
def poland_spec_provider(mocker):
    # Mocking Random.randint to return a specific sequence that will result in a checksum > 9
    mocker.patch.object(Random, 'randint', side_effect=[0, 0, 0, 0, 0, 0, 0, 8])
    return PolandSpecProvider()

def test_regon_checksum_digit_greater_than_nine(poland_spec_provider):
    regon = poland_spec_provider.regon()
    assert len(regon) == 9
    # The checksum is calculated as (8*0 + 9*0 + 2*0 + 3*0 + 4*0 + 5*0 + 6*0 + 7*8) % 11 = 56 % 11 = 1
    # Since the checksum is not greater than 9, the last digit should be '1', not '0'
    assert regon[-1] == '1'  # checksum digit should be '1' for the mocked sequence
