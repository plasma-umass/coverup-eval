# file mimesis/providers/internet.py:89-99
# lines [89, 97, 98]
# branches []

import pytest
from mimesis.providers.internet import Internet
from ipaddress import IPv4Address

def test_ip_v4_object():
    internet = Internet()
    ip_obj = internet.ip_v4_object()
    
    assert isinstance(ip_obj, IPv4Address)
    assert 0 <= int(ip_obj) <= internet._MAX_IPV4
