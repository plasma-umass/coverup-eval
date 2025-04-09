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
    module = MockModule()
    hardware = SunOSHardware(module)
    return hardware

def test_get_uptime_facts_success(sunos_hardware, mocker):
    mock_time = mocker.patch('time.time', return_value=1548253689)
    result = sunos_hardware.get_uptime_facts()
    assert result == {'uptime_seconds': 4000}
    mock_time.assert_called_once()

def test_get_uptime_facts_failure(sunos_hardware, mocker):
    sunos_hardware.module.run_command = mocker.Mock(return_value=(1, '', 'error'))
    result = sunos_hardware.get_uptime_facts()
    assert result is None
    sunos_hardware.module.run_command.assert_called_once_with('/usr/bin/kstat -p unix:0:system_misc:boot_time')
