# file lib/ansible/module_utils/facts/network/generic_bsd.py:73-109
# lines [73, 80, 81, 83, 85, 87, 88, 89, 90, 93, 94, 95, 97, 98, 99, 100, 101, 103, 104, 106, 107, 109]
# branches ['85->87', '85->109', '87->88', '87->89', '90->93', '90->94', '94->85', '94->95', '97->94', '97->98', '98->99', '98->100', '100->101', '100->103', '103->104', '103->106', '106->94', '106->107']

import pytest
import socket
from unittest.mock import MagicMock

# Assuming the module structure is as follows:
# lib/ansible/module_utils/facts/network/generic_bsd.py
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_module(mocker):
    module_mock = MagicMock()
    module_mock.run_command = mocker.MagicMock()
    return module_mock

@pytest.fixture
def mock_socket_has_ipv6(mocker):
    return mocker.patch('socket.has_ipv6', new_callable=mocker.PropertyMock)

def test_get_default_interfaces_ipv4(mock_module, mock_socket_has_ipv6):
    mock_module.run_command.side_effect = [
        (0, 'interface: em0\ngateway: 192.168.1.1\nif address: 192.168.1.100\n', ''),
        (0, '', '')  # Simulate no output for IPv6
    ]
    mock_socket_has_ipv6.return_value = True
    network = GenericBsdIfconfigNetwork(module=mock_module)
    v4, v6 = network.get_default_interfaces(route_path='/sbin/route')
    assert v4 == {'interface': 'em0', 'gateway': '192.168.1.1', 'address': '192.168.1.100'}
    assert v6 == {}

def test_get_default_interfaces_ipv6(mock_module, mock_socket_has_ipv6):
    mock_module.run_command.side_effect = [
        (0, '', ''),  # Simulate no output for IPv4
        (0, 'interface: em0\ngateway: fe80::1\nlocal addr: fe80::2\n', '')  # IPv6 output
    ]
    mock_socket_has_ipv6.return_value = True
    network = GenericBsdIfconfigNetwork(module=mock_module)
    v4, v6 = network.get_default_interfaces(route_path='/sbin/route')
    assert v4 == {}
    assert v6 == {'interface': 'em0', 'gateway': 'fe80::1', 'address': 'fe80::2'}

def test_get_default_interfaces_no_ipv6_support(mock_module, mock_socket_has_ipv6):
    mock_module.run_command.side_effect = [
        (0, 'interface: em0\ngateway: 192.168.1.1\nif address: 192.168.1.100\n', ''),
        (0, '', '')  # Simulate no output for IPv6
    ]
    mock_socket_has_ipv6.return_value = False
    network = GenericBsdIfconfigNetwork(module=mock_module)
    v4, v6 = network.get_default_interfaces(route_path='/sbin/route')
    assert v4 == {'interface': 'em0', 'gateway': '192.168.1.1', 'address': '192.168.1.100'}
    assert v6 == {}

def test_get_default_interfaces_no_output(mock_module, mock_socket_has_ipv6):
    mock_module.run_command.side_effect = [
        (0, '', ''),  # Simulate no output for IPv4
        (0, '', '')  # Simulate no output for IPv6
    ]
    mock_socket_has_ipv6.return_value = True
    network = GenericBsdIfconfigNetwork(module=mock_module)
    v4, v6 = network.get_default_interfaces(route_path='/sbin/route')
    assert v4 == {}
    assert v6 == {}
