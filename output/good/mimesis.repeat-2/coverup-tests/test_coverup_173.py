# file mimesis/builtins/pl.py:25-40
# lines [38]
# branches ['37->38']

import pytest
from mimesis.builtins.pl import PolandSpecProvider
from mimesis.random import Random

@pytest.fixture
def poland_spec_provider(mocker):
    random = Random()
    mocker.patch.object(random, 'randint', side_effect=[101] + [9] * 6 + [10])
    return PolandSpecProvider(random)

def test_nip_recursion(poland_spec_provider):
    nip = poland_spec_provider.nip()
    assert nip is not None
    assert len(nip) == 10
    assert nip.isdigit()
