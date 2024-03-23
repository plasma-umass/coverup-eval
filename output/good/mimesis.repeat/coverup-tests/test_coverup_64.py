# file mimesis/providers/internet.py:120-132
# lines [120, 128, 129, 130]
# branches []

import pytest
from mimesis.providers.internet import Internet
from ipaddress import IPv6Address

@pytest.fixture
def internet_provider():
    return Internet()

def test_ip_v6_object(internet_provider):
    ip_v6 = internet_provider.ip_v6_object()
    assert isinstance(ip_v6, IPv6Address), "The object must be an instance of IPv6Address"
    assert 0 <= int(ip_v6) <= internet_provider._MAX_IPV6, "The IPv6 address must be within the valid range"
