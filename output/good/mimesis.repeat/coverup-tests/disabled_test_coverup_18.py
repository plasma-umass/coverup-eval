# file mimesis/builtins/pl.py:25-40
# lines [25, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40]
# branches ['37->38', '37->39']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.random import Random

@pytest.fixture
def poland_spec_provider(mocker):
    random = Random()
    mocker.patch.object(random, 'randint', side_effect=[101, 0, 0, 0, 0, 0, 0, 0])
    return PolandSpecProvider(random)

def test_nip_checksum_digit_greater_than_nine(poland_spec_provider):
    nip = poland_spec_provider.nip()
    assert len(nip) == 10
    assert nip.isdigit()
    # Verify that the checksum digit is not greater than 9
    nip_coefficients = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    nip_digits = [int(d) for d in nip[:-1]]
    checksum_digit = int(nip[-1])
    sum_v = sum([nc * nd for nc, nd in zip(nip_coefficients, nip_digits)])
    assert (sum_v + checksum_digit) % 11 != 10
