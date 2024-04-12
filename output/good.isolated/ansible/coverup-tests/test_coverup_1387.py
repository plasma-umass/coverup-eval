# file lib/ansible/module_utils/facts/hardware/sunos.py:206-265
# lines [247]
# branches ['246->247']

import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardware

@pytest.fixture
def sunos_hardware(mocker):
    module_mock = mocker.MagicMock()
    hardware = SunOSHardware(module=module_mock)
    return hardware

def test_get_device_facts_with_run_command_failure(sunos_hardware, mocker):
    mocker.patch.object(sunos_hardware.module, 'run_command', return_value=(1, '', ''))
    device_facts = sunos_hardware.get_device_facts()
    assert device_facts == {'devices': {}}
