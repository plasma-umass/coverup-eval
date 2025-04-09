# file: lib/ansible/module_utils/facts/network/generic_bsd.py:36-64
# asked: {"lines": [36, 37, 38, 40, 41, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 59, 60, 61, 62, 64], "branches": [[40, 41], [40, 43], [45, 46], [45, 48], [56, 57], [56, 59]]}
# gained: {"lines": [36, 37, 38, 40, 41, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 59, 60, 61, 62, 64], "branches": [[40, 41], [40, 43], [45, 46], [45, 48], [56, 59]]}

import pytest
from unittest.mock import MagicMock

from ansible.module_utils.facts.network.generic_bsd import GenericBsdIfconfigNetwork

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path = MagicMock(side_effect=lambda x: f"/usr/sbin/{x}" if x in ['ifconfig', 'route'] else None)
    module.run_command = MagicMock(return_value=(0, "interface: em0\ngateway: 192.168.1.1\nif address: 192.168.1.2\n", ""))
    return module

def test_populate_with_valid_paths(mock_module):
    network = GenericBsdIfconfigNetwork(mock_module)
    facts = network.populate()
    
    assert 'interfaces' in facts
    assert 'default_ipv4' in facts
    assert 'default_ipv6' in facts
    assert 'all_ipv4_addresses' in facts
    assert 'all_ipv6_addresses' in facts

def test_populate_without_ifconfig_path(mock_module):
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: None if x == 'ifconfig' else f"/usr/sbin/{x}")
    network = GenericBsdIfconfigNetwork(mock_module)
    facts = network.populate()
    
    assert facts == {}

def test_populate_without_route_path(mock_module):
    mock_module.get_bin_path = MagicMock(side_effect=lambda x: None if x == 'route' else f"/usr/sbin/{x}")
    network = GenericBsdIfconfigNetwork(mock_module)
    facts = network.populate()
    
    assert facts == {}
