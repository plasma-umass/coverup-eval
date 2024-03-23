# file mimesis/providers/internet.py:101-118
# lines [101, 102, 112, 114, 115, 116, 118]
# branches ['114->115', '114->118']

import pytest
from mimesis.enums import PortRange
from mimesis.providers.internet import Internet

@pytest.fixture
def internet_provider():
    return Internet()

def test_ip_v4_with_port_all_range(internet_provider):
    ip_with_port = internet_provider.ip_v4(with_port=True, port_range=PortRange.ALL)
    ip, port = ip_with_port.split(':')
    assert len(ip.split('.')) == 4  # Check if IP is valid
    assert ip_with_port.count(':') == 1  # Check if only one port is appended
    assert 0 <= int(port) <= 65535  # Check if port is in valid range

def test_ip_v4_with_port_well_known(internet_provider):
    ip_with_port = internet_provider.ip_v4(with_port=True, port_range=PortRange.WELL_KNOWN)
    ip, port = ip_with_port.split(':')
    assert len(ip.split('.')) == 4  # Check if IP is valid
    assert ip_with_port.count(':') == 1  # Check if only one port is appended
    assert 0 <= int(port) <= 1023  # Check if port is in well-known range

def test_ip_v4_with_port_ephemeral(internet_provider):
    ip_with_port = internet_provider.ip_v4(with_port=True, port_range=PortRange.EPHEMERAL)
    ip, port = ip_with_port.split(':')
    assert len(ip.split('.')) == 4  # Check if IP is valid
    assert ip_with_port.count(':') == 1  # Check if only one port is appended
    assert 49152 <= int(port) <= 65535  # Check if port is in ephemeral range

def test_ip_v4_without_port(internet_provider):
    ip = internet_provider.ip_v4()
    assert len(ip.split('.')) == 4  # Check if IP is valid
    assert ':' not in ip  # Check that no port is appended
