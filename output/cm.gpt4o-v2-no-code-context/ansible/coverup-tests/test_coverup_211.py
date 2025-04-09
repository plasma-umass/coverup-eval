# file: lib/ansible/module_utils/facts/hardware/darwin.py:58-67
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65, 66, 67], "branches": [[60, 61], [60, 62], [63, 64], [63, 67], [64, 63], [64, 65]]}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65, 66, 67], "branches": [[60, 61], [60, 62], [63, 64], [63, 67], [64, 65]]}

import pytest
from unittest.mock import Mock

# Assuming the DarwinHardware class is imported from the module
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def darwin_hardware(mock_module):
    return DarwinHardware(module=mock_module)

def test_get_system_profile_success(darwin_hardware, mock_module):
    mock_module.run_command.return_value = (0, "Model Name: MacBook Pro\nModel Identifier: MacBookPro15,1", "")
    
    result = darwin_hardware.get_system_profile()
    
    expected_result = {
        "Model Name": "MacBook Pro",
        "Model Identifier": "MacBookPro15,1"
    }
    
    assert result == expected_result
    mock_module.run_command.assert_called_once_with(["/usr/sbin/system_profiler", "SPHardwareDataType"])

def test_get_system_profile_failure(darwin_hardware, mock_module):
    mock_module.run_command.return_value = (1, "", "Error")
    
    result = darwin_hardware.get_system_profile()
    
    assert result == {}
    mock_module.run_command.assert_called_once_with(["/usr/sbin/system_profiler", "SPHardwareDataType"])
