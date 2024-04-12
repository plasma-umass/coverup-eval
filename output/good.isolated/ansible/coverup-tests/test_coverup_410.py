# file lib/ansible/module_utils/facts/hardware/openbsd.py:48-64
# lines [48, 49, 50, 52, 53, 54, 55, 56, 59, 60, 61, 62, 64]
# branches []

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
from ansible.module_utils.facts.timeout import TimeoutError

# Mocking the get_sysctl function
def mock_get_sysctl(module, keys):
    return {'hw.some_key': 'some_value'}

# Mocking the OpenBSDHardware methods
def mock_get_processor_facts(self):
    return {'processor': 'some_processor'}

def mock_get_memory_facts(self):
    return {'memory': 'some_memory'}

def mock_get_device_facts(self):
    return {'device': 'some_device'}

def mock_get_dmi_facts(self):
    return {'dmi': 'some_dmi'}

def mock_get_uptime_facts(self):
    return {'uptime': 'some_uptime'}

def mock_get_mount_facts(self):
    return {'mount': 'some_mount'}

def mock_get_mount_facts_timeout(self):
    raise TimeoutError()

@pytest.fixture
def openbsd_hardware(mocker):
    module_mock = mocker.MagicMock()
    hardware = OpenBSDHardware(module=module_mock)
    mocker.patch.object(OpenBSDHardware, 'get_processor_facts', mock_get_processor_facts)
    mocker.patch.object(OpenBSDHardware, 'get_memory_facts', mock_get_memory_facts)
    mocker.patch.object(OpenBSDHardware, 'get_device_facts', mock_get_device_facts)
    mocker.patch.object(OpenBSDHardware, 'get_dmi_facts', mock_get_dmi_facts)
    mocker.patch.object(OpenBSDHardware, 'get_uptime_facts', mock_get_uptime_facts)
    mocker.patch.object(OpenBSDHardware, 'get_mount_facts', mock_get_mount_facts)
    mocker.patch('ansible.module_utils.facts.hardware.openbsd.get_sysctl', mock_get_sysctl)
    return hardware

@pytest.fixture
def openbsd_hardware_timeout(mocker):
    module_mock = mocker.MagicMock()
    hardware = OpenBSDHardware(module=module_mock)
    mocker.patch.object(OpenBSDHardware, 'get_processor_facts', mock_get_processor_facts)
    mocker.patch.object(OpenBSDHardware, 'get_memory_facts', mock_get_memory_facts)
    mocker.patch.object(OpenBSDHardware, 'get_device_facts', mock_get_device_facts)
    mocker.patch.object(OpenBSDHardware, 'get_dmi_facts', mock_get_dmi_facts)
    mocker.patch.object(OpenBSDHardware, 'get_uptime_facts', mock_get_uptime_facts)
    mocker.patch.object(OpenBSDHardware, 'get_mount_facts', mock_get_mount_facts_timeout)
    mocker.patch('ansible.module_utils.facts.hardware.openbsd.get_sysctl', mock_get_sysctl)
    return hardware

def test_openbsd_hardware_populate(openbsd_hardware):
    facts = openbsd_hardware.populate()
    assert facts['processor'] == 'some_processor'
    assert facts['memory'] == 'some_memory'
    assert facts['device'] == 'some_device'
    assert facts['dmi'] == 'some_dmi'
    assert facts['uptime'] == 'some_uptime'
    assert facts['mount'] == 'some_mount'

def test_openbsd_hardware_populate_with_timeout(openbsd_hardware_timeout):
    facts = openbsd_hardware_timeout.populate()
    assert facts['processor'] == 'some_processor'
    assert facts['memory'] == 'some_memory'
    assert facts['device'] == 'some_device'
    assert facts['dmi'] == 'some_dmi'
    assert facts['uptime'] == 'some_uptime'
    assert 'mount' not in facts
