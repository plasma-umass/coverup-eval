# file: lib/ansible/module_utils/facts/hardware/freebsd.py:47-69
# asked: {"lines": [47, 48, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69], "branches": []}
# gained: {"lines": [47, 48, 50, 51, 52, 53, 54, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def freebsd_hardware():
    module = MagicMock()
    return FreeBSDHardware(module)

def test_populate_all_methods_called(freebsd_hardware):
    with patch.object(freebsd_hardware, 'get_cpu_facts', return_value={'cpu': 'facts'}) as mock_cpu_facts, \
         patch.object(freebsd_hardware, 'get_memory_facts', return_value={'memory': 'facts'}) as mock_memory_facts, \
         patch.object(freebsd_hardware, 'get_uptime_facts', return_value={'uptime': 'facts'}) as mock_uptime_facts, \
         patch.object(freebsd_hardware, 'get_dmi_facts', return_value={'dmi': 'facts'}) as mock_dmi_facts, \
         patch.object(freebsd_hardware, 'get_device_facts', return_value={'device': 'facts'}) as mock_device_facts, \
         patch.object(freebsd_hardware, 'get_mount_facts', return_value={'mount': 'facts'}) as mock_mount_facts:
        
        result = freebsd_hardware.populate()
        
        mock_cpu_facts.assert_called_once()
        mock_memory_facts.assert_called_once()
        mock_uptime_facts.assert_called_once()
        mock_dmi_facts.assert_called_once()
        mock_device_facts.assert_called_once()
        mock_mount_facts.assert_called_once()
        
        assert result == {
            'cpu': 'facts',
            'memory': 'facts',
            'uptime': 'facts',
            'dmi': 'facts',
            'device': 'facts',
            'mount': 'facts'
        }

def test_populate_timeout_error(freebsd_hardware):
    with patch.object(freebsd_hardware, 'get_cpu_facts', return_value={'cpu': 'facts'}) as mock_cpu_facts, \
         patch.object(freebsd_hardware, 'get_memory_facts', return_value={'memory': 'facts'}) as mock_memory_facts, \
         patch.object(freebsd_hardware, 'get_uptime_facts', return_value={'uptime': 'facts'}) as mock_uptime_facts, \
         patch.object(freebsd_hardware, 'get_dmi_facts', return_value={'dmi': 'facts'}) as mock_dmi_facts, \
         patch.object(freebsd_hardware, 'get_device_facts', return_value={'device': 'facts'}) as mock_device_facts, \
         patch.object(freebsd_hardware, 'get_mount_facts', side_effect=TimeoutError) as mock_mount_facts:
        
        result = freebsd_hardware.populate()
        
        mock_cpu_facts.assert_called_once()
        mock_memory_facts.assert_called_once()
        mock_uptime_facts.assert_called_once()
        mock_dmi_facts.assert_called_once()
        mock_device_facts.assert_called_once()
        mock_mount_facts.assert_called_once()
        
        assert result == {
            'cpu': 'facts',
            'memory': 'facts',
            'uptime': 'facts',
            'dmi': 'facts',
            'device': 'facts'
        }
