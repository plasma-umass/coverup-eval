# file lib/ansible/module_utils/facts/network/generic_bsd.py:73-109
# lines [88]
# branches ['87->88', '97->94']

import pytest
import socket
from unittest.mock import MagicMock

# Assuming the module structure and class are as follows:
# lib/ansible/module_utils/facts/network/generic_bsd.py
from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

# Mock the module for testing
@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.run_command = MagicMock()
    return mock_module

# Test function to cover line 88 and branch 97->94
def test_get_default_interfaces_no_ipv6(mock_module, mocker):
    # Set has_ipv6 to False to cover line 88
    mocker.patch('socket.has_ipv6', new=False)

    # Prepare the mock run_command output to cover branch 97->94
    mock_module.run_command.side_effect = [
        (0, 'interface: en0\ngateway: 192.168.1.1\n', ''),  # v4
        (0, '', '')  # v6, no output to simulate the condition
    ]

    network = GenericBsdIfconfigNetwork(mock_module)
    v4_interface, v6_interface = network.get_default_interfaces('/sbin/route')

    # Assertions to verify postconditions and improve coverage
    assert v4_interface['interface'] == 'en0'
    assert v4_interface['gateway'] == '192.168.1.1'
    assert v6_interface == {}  # v6 should be empty due to socket.has_ipv6 == False

    # Verify that run_command was called correctly for v4
    mock_module.run_command.assert_any_call(['/sbin/route', '-n', 'get', 'default'])
    # Verify that run_command was not called for v6 due to socket.has_ipv6 == False
    mock_module.run_command.assert_called_once()
