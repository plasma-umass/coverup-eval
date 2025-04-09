# file lib/ansible/module_utils/facts/network/aix.py:32-51
# lines []
# branches ['43->41', '47->41']

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/usr/bin/netstat'
    return module

def test_get_default_interfaces_v4(mock_module):
    network = AIXNetwork(mock_module)
    mock_module.run_command.return_value = (0, 'default 192.168.1.1 UG 0 0 en0\n', '')

    v4, v6 = network.get_default_interfaces('/some/path')

    assert v4 == {'gateway': '192.168.1.1', 'interface': 'en0'}
    assert v6 == {}

def test_get_default_interfaces_v6(mock_module):
    network = AIXNetwork(mock_module)
    mock_module.run_command.return_value = (0, 'default fe80::1 UG 0 0 en0\n', '')

    v4, v6 = network.get_default_interfaces('/some/path')

    assert v4 == {}
    assert v6 == {'gateway': 'fe80::1', 'interface': 'en0'}

def test_get_default_interfaces_no_default(mock_module):
    network = AIXNetwork(mock_module)
    mock_module.run_command.return_value = (0, 'notdefault 192.168.1.1 UG 0 0 en0\n', '')

    v4, v6 = network.get_default_interfaces('/some/path')

    assert v4 == {}
    assert v6 == {}
