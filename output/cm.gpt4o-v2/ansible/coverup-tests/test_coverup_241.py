# file: lib/ansible/module_utils/facts/hardware/hurd.py:24-48
# asked: {"lines": [24, 25, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 44, 45, 46, 48], "branches": []}
# gained: {"lines": [24, 25, 31, 33, 34, 35, 36, 38, 39, 40, 41, 42, 44, 45, 46, 48], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hurd import HurdHardware
from ansible.module_utils.facts.timeout import TimeoutError

@pytest.fixture
def hurd_hardware(mocker):
    module_mock = mocker.Mock()
    return HurdHardware(module=module_mock)

def test_populate_success(mocker, hurd_hardware):
    mocker.patch.object(hurd_hardware, 'get_uptime_facts', return_value={'uptime': '1000'})
    mocker.patch.object(hurd_hardware, 'get_memory_facts', return_value={'memory': '8GB'})
    mocker.patch.object(hurd_hardware, 'get_mount_facts', return_value={'mounts': '/mnt'})

    result = hurd_hardware.populate()
    
    assert result == {'uptime': '1000', 'memory': '8GB', 'mounts': '/mnt'}

def test_populate_timeout_error(mocker, hurd_hardware):
    mocker.patch.object(hurd_hardware, 'get_uptime_facts', return_value={'uptime': '1000'})
    mocker.patch.object(hurd_hardware, 'get_memory_facts', return_value={'memory': '8GB'})
    mocker.patch.object(hurd_hardware, 'get_mount_facts', side_effect=TimeoutError)

    result = hurd_hardware.populate()
    
    assert result == {'uptime': '1000', 'memory': '8GB'}
