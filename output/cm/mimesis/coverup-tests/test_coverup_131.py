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
    # Assert that the generated IP v6 is not empty
    assert ip_v6
    # Assert that the generated IP v6 contains colons, typical of IPv6 format
    assert ':' in ip_v6
    # Assert that the generated IP v6 has the correct number of segments
    assert len(ip_v6.split(':')) == 8
