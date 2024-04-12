# file mimesis/builtins/pl.py:25-40
# lines [25, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40]
# branches ['37->38', '37->39']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.random import Random

@pytest.fixture
def poland_provider(mocker):
    random = Random()
    mocker.patch.object(random, 'randint', side_effect=[999] + [9] * 6 + [10])
    return PolandSpecProvider(random)

def test_nip_recursion(poland_provider):
    nip = poland_provider.nip()
    assert len(nip) == 10
    assert nip.isdigit()
    # Check if the NIP number does not contain the invalid checksum (10)
    assert '10' not in nip
