# file: lib/ansible/module_utils/facts/hardware/darwin.py:42-56
# asked: {"lines": [42, 43, 45, 46, 47, 48, 49, 51, 52, 53, 54, 56], "branches": []}
# gained: {"lines": [42, 43, 45, 46, 47, 48, 49, 51, 52, 53, 54, 56], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from ansible.module_utils.facts.sysctl import get_sysctl

@pytest.fixture
def mock_module():
    module = MagicMock()
    module.get_bin_path.return_value = '/usr/sbin/sysctl'
    module.run_command.return_value = (0, 'hw.memsize: 17179869184\nhw.ncpu: 8', '')
    return module

@pytest.fixture
def darwin_hardware(mock_module):
    return DarwinHardware(mock_module)

def test_populate(monkeypatch, darwin_hardware, mock_module):
    # Mocking get_sysctl
    def mock_get_sysctl(module, prefixes):
        return {'hw.memsize': '17179869184', 'hw.ncpu': '8'}
    
    monkeypatch.setattr('ansible.module_utils.facts.sysctl.get_sysctl', mock_get_sysctl)
    
    # Mocking other methods
    def mock_get_mac_facts():
        return {'mac_facts': 'value'}
    
    def mock_get_cpu_facts():
        return {'cpu_facts': 'value'}
    
    def mock_get_memory_facts():
        return {'memory_facts': 'value'}
    
    def mock_get_uptime_facts():
        return {'uptime_facts': 'value'}
    
    monkeypatch.setattr(darwin_hardware, 'get_mac_facts', mock_get_mac_facts)
    monkeypatch.setattr(darwin_hardware, 'get_cpu_facts', mock_get_cpu_facts)
    monkeypatch.setattr(darwin_hardware, 'get_memory_facts', mock_get_memory_facts)
    monkeypatch.setattr(darwin_hardware, 'get_uptime_facts', mock_get_uptime_facts)
    
    # Call the method
    result = darwin_hardware.populate()
    
    # Assertions
    assert result == {
        'mac_facts': 'value',
        'cpu_facts': 'value',
        'memory_facts': 'value',
        'uptime_facts': 'value'
    }
    assert darwin_hardware.sysctl == {'hw.memsize': '17179869184', 'hw.ncpu': '8'}
