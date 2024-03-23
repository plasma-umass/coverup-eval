# file mimesis/builtins/nl.py:11-56
# lines [11, 12, 14, 16, 18, 19, 21, 23, 31, 32, 33, 35, 36, 37, 38, 40, 41, 43, 44, 46, 47, 49, 51, 56]
# branches ['35->36', '35->40', '46->47', '46->49']

import pytest
from mimesis.builtins.nl import NetherlandsSpecProvider

@pytest.fixture
def netherlands_provider():
    return NetherlandsSpecProvider()

def test_bsn_generation(netherlands_provider):
    bsn = netherlands_provider.bsn()
    assert bsn is not None
    assert len(bsn) == 9
    assert bsn.isdigit()
    # Validate BSN using the checksum method
    total = 0
    multiplier = 9
    for char in bsn:
        multiplier = -multiplier if multiplier == 1 else multiplier
        total += int(char) * multiplier
        multiplier -= 1
    assert total % 11 == 0

def test_burgerservicenummer_alias(netherlands_provider):
    bsn = netherlands_provider.burgerservicenummer()
    assert bsn is not None
    assert len(bsn) == 9
    assert bsn.isdigit()
    # Validate BSN using the checksum method
    total = 0
    multiplier = 9
    for char in bsn:
        multiplier = -multiplier if multiplier == 1 else multiplier
        total += int(char) * multiplier
        multiplier -= 1
    assert total % 11 == 0
