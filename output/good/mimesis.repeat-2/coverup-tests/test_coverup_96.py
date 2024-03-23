# file mimesis/providers/internet.py:89-99
# lines [89, 97, 98]
# branches []

import pytest
from mimesis.providers.internet import Internet
from ipaddress import IPv4Address

@pytest.fixture
def internet_provider():
    return Internet()

def test_ip_v4_object(internet_provider):
    ip_v4_obj = internet_provider.ip_v4_object()
    assert isinstance(ip_v4_obj, IPv4Address), "The object must be an instance of IPv4Address"
    assert 0 <= int(ip_v4_obj) <= internet_provider._MAX_IPV4, "The IP address must be within the valid range"
