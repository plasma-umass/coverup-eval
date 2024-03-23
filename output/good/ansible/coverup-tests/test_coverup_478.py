# file lib/ansible/module_utils/facts/network/linux.py:30-46
# lines [30, 31, 38, 39, 40, 41, 42, 43, 44]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.linux import LinuxNetwork

@pytest.fixture
def linux_network(mocker):
    mock_module = MagicMock()
    return LinuxNetwork(module=mock_module)

def test_linux_network_interface_types(linux_network):
    assert linux_network.INTERFACE_TYPE['1'] == 'ether'
    assert linux_network.INTERFACE_TYPE['32'] == 'infiniband'
    assert linux_network.INTERFACE_TYPE['512'] == 'ppp'
    assert linux_network.INTERFACE_TYPE['772'] == 'loopback'
    assert linux_network.INTERFACE_TYPE['65534'] == 'tunnel'
