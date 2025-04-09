# file: lib/ansible/module_utils/facts/hardware/hpux.py:142-158
# asked: {"lines": [142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158], "branches": [[148, 149], [148, 158], [150, 151], [150, 152], [155, 156], [155, 158]]}
# gained: {"lines": [142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158], "branches": [[148, 149], [148, 158], [150, 151], [150, 152], [155, 156], [155, 158]]}

import pytest
from unittest.mock import MagicMock

from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def hpux_hardware():
    module = MagicMock()
    return HPUXHardware(module)

def test_get_hw_facts_no_collected_facts(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(return_value=(0, "TestModel", ""))
    result = hpux_hardware.get_hw_facts()
    assert result == {'model': 'TestModel'}

def test_get_hw_facts_with_ia64_architecture(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(side_effect=[
        (0, "TestModel", ""),
        (0, "Firmware revision: TestFirmware", ""),
        (0, "Machine serial number: TestSerial", "")
    ])
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    result = hpux_hardware.get_hw_facts(collected_facts)
    assert result == {
        'model': 'TestModel',
        'firmware_version': 'TestFirmware',
        'product_serial': 'TestSerial'
    }

def test_get_hw_facts_with_ia64_architecture_and_specific_version(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(side_effect=[
        (0, "TestModel", ""),
        (0, "Firmware revision=TestFirmware", ""),
        (0, "Machine serial number=TestSerial", "")
    ])
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    result = hpux_hardware.get_hw_facts(collected_facts)
    assert result == {
        'model': 'TestModel',
        'firmware_version': 'TestFirmware',
        'product_serial': 'TestSerial'
    }

def test_get_hw_facts_with_ia64_architecture_no_serial(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(side_effect=[
        (0, "TestModel", ""),
        (0, "Firmware revision: TestFirmware", ""),
        (1, "", "")
    ])
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    result = hpux_hardware.get_hw_facts(collected_facts)
    assert result == {
        'model': 'TestModel',
        'firmware_version': 'TestFirmware'
    }
