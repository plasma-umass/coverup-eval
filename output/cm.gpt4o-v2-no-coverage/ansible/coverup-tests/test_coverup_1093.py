# file: lib/ansible/module_utils/facts/network/generic_bsd.py:73-109
# asked: {"lines": [80, 81, 83, 85, 87, 88, 89, 90, 93, 94, 95, 97, 98, 99, 100, 101, 103, 104, 106, 107, 109], "branches": [[85, 87], [85, 109], [87, 88], [87, 89], [90, 93], [90, 94], [94, 85], [94, 95], [97, 94], [97, 98], [98, 99], [98, 100], [100, 101], [100, 103], [103, 104], [103, 106], [106, 94], [106, 107]]}
# gained: {"lines": [80, 81, 83, 85, 87, 88, 89, 90, 93, 94, 95, 97, 98, 99, 100, 101, 103, 104, 106, 107, 109], "branches": [[85, 87], [85, 109], [87, 88], [87, 89], [90, 93], [90, 94], [94, 85], [94, 95], [97, 98], [98, 99], [98, 100], [100, 101], [100, 103], [103, 104], [103, 106], [106, 94], [106, 107]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def network(mock_module):
    return GenericBsdIfconfigNetwork(mock_module)

def test_get_default_interfaces_v4(network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "interface: em0\ngateway: 192.168.1.1\nif address: 192.168.1.100", ""),
        (0, "", "")
    ]
    v4, v6 = network.get_default_interfaces('/sbin/route')
    assert v4 == {'interface': 'em0', 'gateway': '192.168.1.1', 'address': '192.168.1.100'}
    assert v6 == {}

def test_get_default_interfaces_v6(network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "interface: em0\ngateway: 192.168.1.1\nif address: 192.168.1.100", ""),
        (0, "interface: em1\ngateway: fe80::1\nlocal addr: fe80::2", "")
    ]
    with patch('socket.has_ipv6', True):
        v4, v6 = network.get_default_interfaces('/sbin/route')
    assert v4 == {'interface': 'em0', 'gateway': '192.168.1.1', 'address': '192.168.1.100'}
    assert v6 == {'interface': 'em1', 'gateway': 'fe80::1', 'address': 'fe80::2'}

def test_get_default_interfaces_no_output(network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "", ""),
        (0, "", "")
    ]
    v4, v6 = network.get_default_interfaces('/sbin/route')
    assert v4 == {}
    assert v6 == {}

def test_get_default_interfaces_v6_no_ipv6_support(network, mock_module):
    mock_module.run_command.side_effect = [
        (0, "interface: em0\ngateway: 192.168.1.1\nif address: 192.168.1.100", ""),
        (0, "", "")
    ]
    with patch('socket.has_ipv6', False):
        v4, v6 = network.get_default_interfaces('/sbin/route')
    assert v4 == {'interface': 'em0', 'gateway': '192.168.1.1', 'address': '192.168.1.100'}
    assert v6 == {}
