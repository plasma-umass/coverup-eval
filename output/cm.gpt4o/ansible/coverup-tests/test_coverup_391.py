# file lib/ansible/module_utils/facts/hardware/darwin.py:42-56
# lines [42, 43, 45, 46, 47, 48, 49, 51, 52, 53, 54, 56]
# branches []

import pytest
from unittest.mock import patch, MagicMock

# Assuming the necessary imports from ansible.module_utils.facts.hardware.darwin
from ansible.module_utils.facts.hardware.darwin import DarwinHardware, get_sysctl

class TestDarwinHardware:
    @patch('ansible.module_utils.facts.hardware.darwin.get_sysctl')
    @patch.object(DarwinHardware, 'get_mac_facts')
    @patch.object(DarwinHardware, 'get_cpu_facts')
    @patch.object(DarwinHardware, 'get_memory_facts')
    @patch.object(DarwinHardware, 'get_uptime_facts')
    def test_populate(self, mock_get_uptime_facts, mock_get_memory_facts, mock_get_cpu_facts, mock_get_mac_facts, mock_get_sysctl):
        # Arrange
        mock_module = MagicMock()
        mock_get_sysctl.return_value = {'hw': {}, 'machdep': {}, 'kern': {}}
        mock_get_mac_facts.return_value = {'mac': 'facts'}
        mock_get_cpu_facts.return_value = {'cpu': 'facts'}
        mock_get_memory_facts.return_value = {'memory': 'facts'}
        mock_get_uptime_facts.return_value = {'uptime': 'facts'}
        
        darwin_hardware = DarwinHardware(mock_module)
        
        # Act
        result = darwin_hardware.populate()
        
        # Assert
        assert result == {
            'mac': 'facts',
            'cpu': 'facts',
            'memory': 'facts',
            'uptime': 'facts'
        }
        mock_get_sysctl.assert_called_once_with(mock_module, ['hw', 'machdep', 'kern'])
        mock_get_mac_facts.assert_called_once()
        mock_get_cpu_facts.assert_called_once()
        mock_get_memory_facts.assert_called_once()
        mock_get_uptime_facts.assert_called_once()
