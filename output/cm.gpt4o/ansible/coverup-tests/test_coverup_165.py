# file lib/ansible/module_utils/facts/network/hpux.py:61-77
# lines [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
# branches ['65->66', '65->77', '67->65', '67->68', '68->67', '68->69']

import pytest
from unittest.mock import Mock

# Assuming the HPUXNetwork class is imported from ansible.module_utils.facts.network.hpux
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def hpux_network(mock_module):
    return HPUXNetwork(module=mock_module)

def test_get_interfaces_info(hpux_network, mock_module):
    # Mock the output of the run_command method
    mock_module.run_command.return_value = (0, "Name  Mtu  Network     Address            Ipkts Ierrs    Opkts Oerrs  Coll\n"
                                               "lan0  1500  192.168.1  192.168.1.10       1000  0        1000  0     0\n"
                                               "lan1  1500  10.0.0     10.0.0.1           2000  0        2000  0     0\n", "")

    expected_interfaces = {
        'lan0': {
            'device': 'lan0',
            'ipv4': {
                'network': '192.168.1',
                'interface': 'lan0',
                'address': '192.168.1.10'
            }
        },
        'lan1': {
            'device': 'lan1',
            'ipv4': {
                'network': '10.0.0',
                'interface': 'lan1',
                'address': '10.0.0.1'
            }
        }
    }

    interfaces_info = hpux_network.get_interfaces_info()
    assert interfaces_info == expected_interfaces

    # Ensure the run_command was called with the correct command
    mock_module.run_command.assert_called_once_with("/usr/bin/netstat -niw")
