# file mimesis/providers/internet.py:144-159
# lines [144, 152, 153, 154, 155, 156, 158, 159]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.random import Random

@pytest.fixture
def internet_provider():
    return Internet()

def test_mac_address(internet_provider):
    mac = internet_provider.mac_address()
    mac_parts = mac.split(':')

    assert len(mac_parts) == 6
    assert all(len(part) == 2 for part in mac_parts)
    assert all(part.isalnum() for part in mac_parts)
    assert 0x00 <= int(mac_parts[0], 16) <= 0xff
    assert 0x00 <= int(mac_parts[1], 16) <= 0xff
    assert 0x00 <= int(mac_parts[2], 16) <= 0xff
    assert 0x00 <= int(mac_parts[3], 16) <= 0x7f
    assert 0x00 <= int(mac_parts[4], 16) <= 0xff
    assert 0x00 <= int(mac_parts[5], 16) <= 0xff
