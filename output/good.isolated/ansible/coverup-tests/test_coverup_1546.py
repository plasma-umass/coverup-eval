# file lib/ansible/module_utils/facts/network/hpux.py:61-77
# lines [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
# branches ['65->66', '65->77', '67->65', '67->68', '68->67', '68->69']

import pytest
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture
def mock_module(mocker):
    module_mock = mocker.MagicMock()
    module_mock.run_command = mocker.MagicMock(return_value=(0, 
        "Name  Mtu   Network       Address            Ipkts Ierrs    Opkts Oerrs  Coll\n"
        "lan0  1500  192.168.1.0   192.168.1.100      63683     0    112233     0     0\n"
        "lan1  1500  10.0.0.0      10.0.0.1           12345     0    67890      0     0\n", ''))
    return module_mock

def test_get_interfaces_info(mock_module):
    expected_interfaces = {
        'lan0': {
            'device': 'lan0',
            'ipv4': {
                'network': '192.168.1.0',
                'interface': 'lan0',
                'address': '192.168.1.100'
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

    hpux_network = HPUXNetwork(module=mock_module)
    interfaces = hpux_network.get_interfaces_info()

    assert interfaces == expected_interfaces
    mock_module.run_command.assert_called_once_with("/usr/bin/netstat -niw")
