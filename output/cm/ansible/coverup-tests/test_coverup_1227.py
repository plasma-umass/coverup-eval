# file lib/ansible/module_utils/facts/hardware/netbsd.py:46-65
# lines [47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 60, 61, 62, 63, 65]
# branches []

import pytest
from ansible.module_utils.facts.hardware.netbsd import NetBSDHardware
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_module(mocker):
    mock_module = MagicMock()
    mock_module.params = {}
    return mock_module

@pytest.fixture
def netbsd_hardware(mock_module):
    return NetBSDHardware(module=mock_module)

def test_netbsd_hardware_populate(mocker, netbsd_hardware):
    mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_sysctl', return_value={'machdep': 'some_value'})
    mocker.patch.object(netbsd_hardware, 'get_cpu_facts', return_value={'cpu': 'some_cpu_fact'})
    mocker.patch.object(netbsd_hardware, 'get_memory_facts', return_value={'memory': 'some_memory_fact'})
    mocker.patch.object(netbsd_hardware, 'get_mount_facts', return_value={'mount': 'some_mount_fact'})
    mocker.patch.object(netbsd_hardware, 'get_dmi_facts', return_value={'dmi': 'some_dmi_fact'})

    hardware_facts = netbsd_hardware.populate()

    assert hardware_facts['cpu'] == 'some_cpu_fact'
    assert hardware_facts['memory'] == 'some_memory_fact'
    assert hardware_facts['mount'] == 'some_mount_fact'
    assert hardware_facts['dmi'] == 'some_dmi_fact'
    assert 'machdep' in netbsd_hardware.sysctl

def test_netbsd_hardware_populate_with_timeout_error(mocker, netbsd_hardware):
    mocker.patch('ansible.module_utils.facts.hardware.netbsd.get_sysctl', return_value={'machdep': 'some_value'})
    mocker.patch.object(netbsd_hardware, 'get_cpu_facts', return_value={'cpu': 'some_cpu_fact'})
    mocker.patch.object(netbsd_hardware, 'get_memory_facts', return_value={'memory': 'some_memory_fact'})
    mocker.patch.object(netbsd_hardware, 'get_mount_facts', side_effect=TimeoutError())
    mocker.patch.object(netbsd_hardware, 'get_dmi_facts', return_value={'dmi': 'some_dmi_fact'})

    with patch('ansible.module_utils.facts.hardware.netbsd.TimeoutError', new=TimeoutError):
        hardware_facts = netbsd_hardware.populate()

    assert hardware_facts['cpu'] == 'some_cpu_fact'
    assert hardware_facts['memory'] == 'some_memory_fact'
    assert 'mount' not in hardware_facts
    assert hardware_facts['dmi'] == 'some_dmi_fact'
    assert 'machdep' in netbsd_hardware.sysctl
