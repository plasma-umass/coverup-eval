# file: lib/ansible/module_utils/facts/hardware/openbsd.py:114-130
# asked: {"lines": [116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}
# gained: {"lines": [116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}

import pytest
import time
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
from unittest.mock import Mock

@pytest.fixture
def mock_module():
    module = Mock()
    module.get_bin_path.return_value = '/sbin/sysctl'
    return module

def test_get_uptime_facts_success(mock_module):
    mock_module.run_command.return_value = (0, '1633072800', '')
    hardware = OpenBSDHardware(mock_module)
    
    result = hardware.get_uptime_facts()
    
    assert 'uptime_seconds' in result
    assert isinstance(result['uptime_seconds'], int)
    assert result['uptime_seconds'] > 0

def test_get_uptime_facts_failure_non_zero_rc(mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    hardware = OpenBSDHardware(mock_module)
    
    result = hardware.get_uptime_facts()
    
    assert result == {}

def test_get_uptime_facts_failure_non_digit_boottime(mock_module):
    mock_module.run_command.return_value = (0, 'invalid_time', '')
    hardware = OpenBSDHardware(mock_module)
    
    result = hardware.get_uptime_facts()
    
    assert result == {}
