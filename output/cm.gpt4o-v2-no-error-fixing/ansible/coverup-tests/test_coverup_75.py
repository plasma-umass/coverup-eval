# file: lib/ansible/module_utils/facts/network/hpux.py:61-77
# asked: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "branches": [[65, 66], [65, 77], [67, 65], [67, 68], [68, 67], [68, 69]]}
# gained: {"lines": [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], "branches": [[65, 66], [65, 77], [67, 65], [67, 68], [68, 67], [68, 69]]}

import pytest
from unittest.mock import Mock

from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture
def hpux_network():
    module = Mock()
    return HPUXNetwork(module)

def test_get_interfaces_info(hpux_network):
    command_output = (
        "Name  Mtu  Network     Address            Ipkts Ierrs    Opkts Oerrs  Coll\n"
        "lan0  1500 192.168.1.0 192.168.1.1        1000  0        1000  0      0\n"
        "lan1  1500 10.0.0.0    10.0.0.1           2000  0        2000  0      0\n"
    )
    hpux_network.module.run_command = Mock(return_value=(0, command_output, ''))

    interfaces_info = hpux_network.get_interfaces_info()

    expected_interfaces_info = {
        'lan0': {
            'device': 'lan0',
            'ipv4': {
                'network': '192.168.1.0',
                'interface': 'lan0',
                'address': '192.168.1.1'
            }
        },
        'lan1': {
            'device': 'lan1',
            'ipv4': {
                'network': '10.0.0.0',
                'interface': 'lan1',
                'address': '10.0.0.1'
            }
        }
    }

    assert interfaces_info == expected_interfaces_info
    hpux_network.module.run_command.assert_called_once_with("/usr/bin/netstat -niw")
