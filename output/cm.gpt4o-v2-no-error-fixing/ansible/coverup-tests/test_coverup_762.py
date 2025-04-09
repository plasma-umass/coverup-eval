# file: lib/ansible/module_utils/facts/network/hpux.py:31-46
# asked: {"lines": [32, 33, 35, 36, 38, 39, 41, 42, 43, 44, 46], "branches": [[35, 36], [35, 38], [43, 44], [43, 46]]}
# gained: {"lines": [32, 33, 35, 36, 38, 39, 41, 42, 43, 44, 46], "branches": [[35, 36], [35, 38], [43, 44], [43, 46]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.network.hpux import HPUXNetwork

@pytest.fixture
def hpux_network():
    return HPUXNetwork(module=MagicMock())

def test_populate_no_netstat_path(hpux_network):
    hpux_network.module.get_bin_path = MagicMock(return_value=None)
    result = hpux_network.populate()
    assert result == {}

def test_populate_with_netstat_path(hpux_network):
    hpux_network.module.get_bin_path = MagicMock(return_value='/usr/bin/netstat')
    hpux_network.get_default_interfaces = MagicMock(return_value={'default_interface': 'eth0'})
    hpux_network.get_interfaces_info = MagicMock(return_value={'eth0': {'ipv4': '192.168.1.1'}})
    
    result = hpux_network.populate()
    
    assert result['default_interface'] == 'eth0'
    assert 'eth0' in result['interfaces']
    assert result['eth0'] == {'ipv4': '192.168.1.1'}
