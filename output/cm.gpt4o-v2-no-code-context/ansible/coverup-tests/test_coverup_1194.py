# file: lib/ansible/module_utils/facts/network/aix.py:32-51
# asked: {"lines": [], "branches": [[43, 41], [47, 41]]}
# gained: {"lines": [], "branches": [[43, 41]]}

import pytest
from unittest.mock import Mock

# Assuming AIXNetwork and GenericBsdIfconfigNetwork are imported from the appropriate module
from ansible.module_utils.facts.network.aix import AIXNetwork

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/netstat')
    return module

@pytest.fixture
def network(mock_module):
    return AIXNetwork(module=mock_module)

def test_get_default_interfaces_v4(network, mock_module, monkeypatch):
    def mock_run_command(cmd):
        return (0, "default 192.168.1.1 UG 0 0 en0", "")
    
    monkeypatch.setattr(mock_module, 'run_command', mock_run_command)
    
    v4, v6 = network.get_default_interfaces('/some/path')
    
    assert v4 == {'gateway': '192.168.1.1', 'interface': 'en0'}
    assert v6 == {}

def test_get_default_interfaces_v6(network, mock_module, monkeypatch):
    def mock_run_command(cmd):
        return (0, "default fe80::1 UG 0 0 en1", "")
    
    monkeypatch.setattr(mock_module, 'run_command', mock_run_command)
    
    v4, v6 = network.get_default_interfaces('/some/path')
    
    assert v4 == {}
    assert v6 == {'gateway': 'fe80::1', 'interface': 'en1'}

def test_get_default_interfaces_no_default(network, mock_module, monkeypatch):
    def mock_run_command(cmd):
        return (0, "notdefault 192.168.1.1 UG 0 0 en0", "")
    
    monkeypatch.setattr(mock_module, 'run_command', mock_run_command)
    
    v4, v6 = network.get_default_interfaces('/some/path')
    
    assert v4 == {}
    assert v6 == {}
