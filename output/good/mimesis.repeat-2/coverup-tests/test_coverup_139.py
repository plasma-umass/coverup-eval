# file mimesis/providers/internet.py:134-142
# lines [134, 142]
# branches []

import pytest
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_ip_v6(internet_provider):
    ip_v6 = internet_provider.ip_v6()
    assert isinstance(ip_v6, str)
    # Basic validation of IPv6 format
    assert ip_v6.count(':') == 7
    # Each block should be hexadecimal
    for block in ip_v6.split(':'):
        assert 0 <= int(block, 16) <= 0xFFFF
