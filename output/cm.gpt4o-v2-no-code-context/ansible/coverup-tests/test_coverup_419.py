# file: lib/ansible/module_utils/facts/hardware/sunos.py:267-279
# asked: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}
# gained: {"lines": [267, 268, 271, 273, 274, 277, 279], "branches": [[273, 274], [273, 277]]}

import pytest
import time
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware(mocker):
    module_mock = mocker.Mock()
    return SunOSHardware(module=module_mock)

def test_get_uptime_facts_success(mocker, sunos_hardware):
    mocker.patch('time.time', return_value=1600000000)
    sunos_hardware.module.run_command.return_value = (0, 'unix:0:system_misc:boot_time\t1599990000\n', '')

    result = sunos_hardware.get_uptime_facts()

    assert result == {'uptime_seconds': 10000}
    sunos_hardware.module.run_command.assert_called_once_with('/usr/bin/kstat -p unix:0:system_misc:boot_time')

def test_get_uptime_facts_failure(sunos_hardware):
    sunos_hardware.module.run_command.return_value = (1, '', 'error')

    result = sunos_hardware.get_uptime_facts()

    assert result is None
    sunos_hardware.module.run_command.assert_called_once_with('/usr/bin/kstat -p unix:0:system_misc:boot_time')
