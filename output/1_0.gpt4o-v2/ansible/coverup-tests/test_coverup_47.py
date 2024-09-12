# file: lib/ansible/module_utils/facts/network/openbsd.py:23-37
# asked: {"lines": [32, 36, 37], "branches": []}
# gained: {"lines": [32, 36, 37], "branches": []}

import pytest
from ansible.module_utils.facts.network.openbsd import OpenBSDNetwork
from unittest.mock import MagicMock

@pytest.fixture
def openbsd_network():
    module = MagicMock()
    return OpenBSDNetwork(module)

def test_get_interfaces_info(monkeypatch, openbsd_network):
    def mock_super_get_interfaces_info(self, ifconfig_path, ifconfig_options):
        return {'interface': 'info'}

    monkeypatch.setattr('ansible.module_utils.facts.network.generic_bsd.GenericBsdIfconfigNetwork.get_interfaces_info', mock_super_get_interfaces_info)
    
    result = openbsd_network.get_interfaces_info('/sbin/ifconfig')
    assert result == {'interface': 'info'}

def test_parse_lladdr_line(openbsd_network):
    current_if = {}
    words = ['lladdr', '00:11:22:33:44:55']
    ips = []

    openbsd_network.parse_lladdr_line(words, current_if, ips)
    
    assert current_if['macaddress'] == '00:11:22:33:44:55'
    assert current_if['type'] == 'ether'
