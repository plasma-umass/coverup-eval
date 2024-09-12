# file: lib/ansible/module_utils/facts/hardware/darwin.py:58-67
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65, 66, 67], "branches": [[60, 61], [60, 62], [63, 64], [63, 67], [64, 63], [64, 65]]}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65, 66, 67], "branches": [[60, 61], [60, 62], [63, 64], [63, 67], [64, 63], [64, 65]]}

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardware
from unittest.mock import Mock

@pytest.fixture
def darwin_hardware():
    module = Mock()
    return DarwinHardware(module)

def test_get_system_profile_success(darwin_hardware):
    darwin_hardware.module.run_command = Mock(return_value=(0, "Model Name: MacBook Pro\nProcessor Name: Intel Core i7", ""))
    result = darwin_hardware.get_system_profile()
    assert result == {
        "Model Name": "MacBook Pro",
        "Processor Name": "Intel Core i7"
    }

def test_get_system_profile_failure(darwin_hardware):
    darwin_hardware.module.run_command = Mock(return_value=(1, "", "Error"))
    result = darwin_hardware.get_system_profile()
    assert result == {}

def test_get_system_profile_empty_output(darwin_hardware):
    darwin_hardware.module.run_command = Mock(return_value=(0, "", ""))
    result = darwin_hardware.get_system_profile()
    assert result == {}

def test_get_system_profile_malformed_output(darwin_hardware):
    darwin_hardware.module.run_command = Mock(return_value=(0, "Malformed Line Without Colon", ""))
    result = darwin_hardware.get_system_profile()
    assert result == {}
