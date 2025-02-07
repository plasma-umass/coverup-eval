# file: lib/ansible/module_utils/facts/hardware/openbsd.py:114-130
# asked: {"lines": [114, 116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}
# gained: {"lines": [114, 116, 117, 119, 121, 122, 124, 125, 126, 128, 129], "branches": [[121, 122], [121, 124], [125, 126], [125, 128]]}

import pytest
import time
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

class MockModule:
    def get_bin_path(self, binary_name):
        return f"/usr/sbin/{binary_name}"

    def run_command(self, cmd):
        if cmd == ["/usr/sbin/sysctl", "-n", "kern.boottime"]:
            return 0, "1633072800", ""  # Mocked boottime
        return 1, "", "error"

@pytest.fixture
def mock_module():
    return MockModule()

def test_get_uptime_facts_success(mock_module):
    hardware = OpenBSDHardware(module=mock_module)
    result = hardware.get_uptime_facts()
    assert 'uptime_seconds' in result
    assert isinstance(result['uptime_seconds'], int)

def test_get_uptime_facts_failure_non_digit(mock_module, monkeypatch):
    def mock_run_command(cmd):
        return 0, "non-digit", ""
    monkeypatch.setattr(mock_module, "run_command", mock_run_command)
    
    hardware = OpenBSDHardware(module=mock_module)
    result = hardware.get_uptime_facts()
    assert result == {}

def test_get_uptime_facts_failure_command_error(mock_module, monkeypatch):
    def mock_run_command(cmd):
        return 1, "", "error"
    monkeypatch.setattr(mock_module, "run_command", mock_run_command)
    
    hardware = OpenBSDHardware(module=mock_module)
    result = hardware.get_uptime_facts()
    assert result == {}
