# file: lib/ansible/module_utils/facts/hardware/darwin.py:42-56
# asked: {"lines": [42, 43, 45, 46, 47, 48, 49, 51, 52, 53, 54, 56], "branches": []}
# gained: {"lines": [42, 43, 45, 46, 47, 48, 49, 51, 52, 53, 54, 56], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def darwin_hardware(mock_module):
    return DarwinHardware(mock_module)

@patch('ansible.module_utils.facts.hardware.darwin.get_sysctl')
@patch.object(DarwinHardware, 'get_mac_facts', return_value={'mac': 'facts'})
@patch.object(DarwinHardware, 'get_cpu_facts', return_value={'cpu': 'facts'})
@patch.object(DarwinHardware, 'get_memory_facts', return_value={'memory': 'facts'})
@patch.object(DarwinHardware, 'get_uptime_facts', return_value={'uptime': 'facts'})
def test_populate(mock_get_uptime_facts, mock_get_memory_facts, mock_get_cpu_facts, mock_get_mac_facts, mock_get_sysctl, darwin_hardware):
    mock_get_sysctl.return_value = {'hw': 'value', 'machdep': 'value', 'kern': 'value'}
    
    result = darwin_hardware.populate()
    
    assert result == {
        'mac': 'facts',
        'cpu': 'facts',
        'memory': 'facts',
        'uptime': 'facts'
    }
    mock_get_sysctl.assert_called_once_with(darwin_hardware.module, ['hw', 'machdep', 'kern'])
    mock_get_mac_facts.assert_called_once()
    mock_get_cpu_facts.assert_called_once()
    mock_get_memory_facts.assert_called_once()
    mock_get_uptime_facts.assert_called_once()
