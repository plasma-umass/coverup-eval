# file: lib/ansible/module_utils/facts/hardware/darwin.py:58-67
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65, 66, 67], "branches": [[60, 61], [60, 62], [63, 64], [63, 67], [64, 63], [64, 65]]}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65, 66, 67], "branches": [[60, 61], [60, 62], [63, 64], [63, 67], [64, 65]]}

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardware

class MockModule:
    def run_command(self, command):
        if command == ["/usr/sbin/system_profiler", "SPHardwareDataType"]:
            return (0, "Model Name: MacBook Pro\nProcessor Name: Intel Core i7", "")
        return (1, "", "Error")

@pytest.fixture
def mock_module():
    return MockModule()

def test_get_system_profile_success(mock_module, monkeypatch):
    dh = DarwinHardware(module=mock_module)
    result = dh.get_system_profile()
    assert result == {
        "Model Name": "MacBook Pro",
        "Processor Name": "Intel Core i7"
    }

def test_get_system_profile_failure(mock_module, monkeypatch):
    def mock_run_command_failure(command):
        return (1, "", "Error")
    
    dh = DarwinHardware(module=mock_module)
    monkeypatch.setattr(mock_module, 'run_command', mock_run_command_failure)
    result = dh.get_system_profile()
    assert result == {}
