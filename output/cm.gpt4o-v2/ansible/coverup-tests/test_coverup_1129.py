# file: lib/ansible/module_utils/facts/network/aix.py:32-51
# asked: {"lines": [33, 35, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51], "branches": [[37, 38], [37, 51], [41, 42], [41, 51], [43, 41], [43, 44], [44, 45], [44, 47], [47, 41], [47, 48]]}
# gained: {"lines": [33, 35, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51], "branches": [[37, 38], [37, 51], [41, 42], [41, 51], [43, 41], [43, 44], [44, 45], [44, 47], [47, 48]]}

import pytest
from unittest.mock import Mock
from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/netstat')
    module.run_command = Mock(return_value=(0, 'default 192.168.1.1 UG 0 0 en0\ndefault fe80::1 UG 0 0 en1', ''))
    return module

@pytest.fixture
def network(mock_module):
    return AIXNetwork(module=mock_module)

def test_get_default_interfaces_v4_v6(network):
    v4, v6 = network.get_default_interfaces('/some/route/path')

    assert v4 == {'gateway': '192.168.1.1', 'interface': 'en0'}
    assert v6 == {'gateway': 'fe80::1', 'interface': 'en1'}

def test_get_default_interfaces_no_netstat(network, mock_module):
    mock_module.get_bin_path = Mock(return_value=None)

    v4, v6 = network.get_default_interfaces('/some/route/path')

    assert v4 == {}
    assert v6 == {}

def test_get_default_interfaces_no_default_route(network, mock_module):
    mock_module.run_command = Mock(return_value=(0, 'notdefault 192.168.1.1 UG 0 0 en0', ''))

    v4, v6 = network.get_default_interfaces('/some/route/path')

    assert v4 == {}
    assert v6 == {}
