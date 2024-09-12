# file: lib/ansible/module_utils/facts/hardware/sunos.py:267-279
# asked: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}
# gained: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}

import pytest
import time
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

class MockModule:
    def run_command(self, command):
        if command == '/usr/bin/kstat -p unix:0:system_misc:boot_time':
            return (0, 'unix:0:system_misc:boot_time\t1548249689\n', '')
        return (1, '', 'error')

@pytest.fixture
def sunos_hardware():
    return SunOSHardware(module=MockModule())

def test_get_uptime_facts_success(sunos_hardware, monkeypatch):
    current_time = 1548250000
    monkeypatch.setattr(time, 'time', lambda: current_time)
    
    result = sunos_hardware.get_uptime_facts()
    
    assert result is not None
    assert 'uptime_seconds' in result
    assert result['uptime_seconds'] == current_time - 1548249689

def test_get_uptime_facts_command_failure(sunos_hardware, monkeypatch):
    class MockModuleFailure:
        def run_command(self, command):
            return (1, '', 'error')
    
    sunos_hardware.module = MockModuleFailure()
    
    result = sunos_hardware.get_uptime_facts()
    
    assert result is None
