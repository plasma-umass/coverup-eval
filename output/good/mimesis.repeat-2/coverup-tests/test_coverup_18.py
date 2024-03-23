# file mimesis/builtins/pl.py:25-40
# lines [25, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40]
# branches ['37->38', '37->39']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.random import Random

@pytest.fixture
def poland_spec_provider(mocker):
    random = Random()
    mocker.patch.object(random, 'randint', side_effect=[999] + [9] * 6 + [0])
    return PolandSpecProvider(random)

def test_nip_recursion(poland_spec_provider):
    nip = poland_spec_provider.nip()
    assert len(nip) == 10
    assert nip.isdigit()
    # Check if the NIP number is valid according to the checksum calculation
    nip_coefficients = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    nip_digits = [int(d) for d in nip]
    sum_v = sum(nc * nd for nc, nd in zip(nip_coefficients, nip_digits[:-1]))
    checksum_digit = sum_v % 11
    if checksum_digit > 9:
        checksum_digit = 0
    assert nip_digits[-1] == checksum_digit
