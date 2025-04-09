# file: lib/ansible/module_utils/facts/network/aix.py:54-132
# asked: {"lines": [55, 56, 57, 58, 59, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 116, 117, 118, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132], "branches": [[66, 67], [66, 69], [71, 73], [71, 132], [73, 74], [73, 101], [77, 78], [77, 80], [80, 81], [80, 82], [82, 83], [82, 84], [84, 85], [84, 86], [86, 87], [86, 88], [88, 89], [88, 90], [90, 91], [90, 92], [92, 93], [92, 94], [94, 95], [94, 97], [101, 71], [101, 103], [103, 104], [103, 121], [105, 106], [105, 121], [107, 108], [107, 109], [109, 110], [109, 121], [110, 111], [110, 112], [113, 114], [113, 116], [117, 109], [117, 118], [121, 71], [121, 122], [123, 71], [123, 124], [125, 126], [125, 127], [127, 71], [127, 128], [128, 127], [128, 129], [130, 127], [130, 131]]}
# gained: {"lines": [55, 56, 57, 58, 59, 62, 63, 64, 65, 66, 67, 69, 71, 73, 74, 77, 78, 79, 80, 82, 84, 85, 86, 88, 90, 92, 93, 101, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 116, 117, 118, 121, 122, 123, 124, 125, 127, 128, 129, 130, 131, 132], "branches": [[66, 67], [71, 73], [71, 132], [73, 74], [77, 78], [77, 80], [80, 82], [82, 84], [84, 85], [84, 86], [86, 88], [88, 90], [90, 92], [92, 93], [101, 103], [103, 104], [103, 121], [105, 106], [107, 109], [109, 110], [109, 121], [110, 112], [113, 114], [113, 116], [117, 109], [117, 118], [121, 71], [121, 122], [123, 124], [125, 127], [127, 71], [127, 128], [128, 129], [130, 131]]}

import pytest
from unittest.mock import MagicMock

from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path = MagicMock(side_effect=lambda x: f"/usr/bin/{x}")
    module.run_command = MagicMock(side_effect=[
        (0, "0", ""),  # uname command
        (0, "en0: flags=4e080863<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST> mtu 1500\ninet 192.168.0.1 netmask 0xffffff00 broadcast 192.168.0.255\nether 00:14:22:01:23:45\n", ""),  # ifconfig command
        (0, "Hardware Address: 00:14:22:01:23:45\nDevice Type: Ethernet\n", ""),  # entstat command
        (0, "mtu 1500\n", "")  # lsattr command
    ])
    return module

def test_get_interfaces_info(mock_module):
    network = AIXNetwork(mock_module)

    ifconfig_path = "/usr/sbin/ifconfig"
    interfaces, ips = network.get_interfaces_info(ifconfig_path)

    assert 'en0' in interfaces
    assert interfaces['en0']['device'] == 'en0'
    assert interfaces['en0']['mtu'] == '1500'
    assert interfaces['en0']['macaddress'] == '00:14:22:01:23:45'
    assert ips['all_ipv4_addresses'] == ['192.168.0.1']
    assert ips['all_ipv6_addresses'] == []

    mock_module.get_bin_path.assert_any_call('uname')
    mock_module.get_bin_path.assert_any_call('entstat')
    mock_module.get_bin_path.assert_any_call('lsattr')
    mock_module.run_command.assert_any_call(['/usr/bin/uname', '-W'])
    mock_module.run_command.assert_any_call([ifconfig_path, '-a'])
    mock_module.run_command.assert_any_call(['/usr/bin/entstat', 'en0'])
    mock_module.run_command.assert_any_call(['/usr/bin/lsattr', '-El', 'en0'])
