# file mimesis/providers/internet.py:120-132
# lines [120, 128, 129, 130]
# branches []

import pytest
from mimesis.providers.internet import Internet
from ipaddress import IPv6Address

def test_ip_v6_object():
    internet = Internet()
    ipv6_obj = internet.ip_v6_object()
    
    assert isinstance(ipv6_obj, IPv6Address)
    assert 0 <= int(ipv6_obj) <= internet._MAX_IPV6
