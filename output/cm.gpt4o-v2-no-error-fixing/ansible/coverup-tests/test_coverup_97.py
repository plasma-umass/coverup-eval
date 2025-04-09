# file: lib/ansible/module_utils/facts/hardware/hpux.py:142-158
# asked: {"lines": [142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158], "branches": [[148, 149], [148, 158], [150, 151], [150, 152], [155, 156], [155, 158]]}
# gained: {"lines": [142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158], "branches": [[148, 149], [148, 158], [150, 151], [150, 152], [155, 156], [155, 158]]}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def hpux_hardware(mock_module):
    return HPUXHardware(module=mock_module)

def test_get_hw_facts_no_collected_facts(hpux_hardware, mock_module):
    mock_module.run_command.return_value = (0, "test_model", "")
    hw_facts = hpux_hardware.get_hw_facts()
    assert hw_facts == {'model': 'test_model'}

def test_get_hw_facts_with_ia64_architecture(hpux_hardware, mock_module):
    collected_facts = {'ansible_architecture': 'ia64'}
    mock_module.run_command.side_effect = [
        (0, "test_model", ""),
        (0, "Firmware revision: 1.0", ""),
        (0, "Machine serial number: 12345", "")
    ]
    hw_facts = hpux_hardware.get_hw_facts(collected_facts)
    assert hw_facts == {
        'model': 'test_model',
        'firmware_version': '1.0',
        'product_serial': '12345'
    }

def test_get_hw_facts_with_ia64_architecture_and_specific_version(hpux_hardware, mock_module):
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    mock_module.run_command.side_effect = [
        (0, "test_model", ""),
        (0, "Firmware revision= 1.0", ""),
        (0, "Machine serial number= 12345", "")
    ]
    hw_facts = hpux_hardware.get_hw_facts(collected_facts)
    assert hw_facts == {
        'model': 'test_model',
        'firmware_version': '1.0',
        'product_serial': '12345'
    }

def test_get_hw_facts_with_ia64_architecture_no_serial(hpux_hardware, mock_module):
    collected_facts = {'ansible_architecture': 'ia64'}
    mock_module.run_command.side_effect = [
        (0, "test_model", ""),
        (0, "Firmware revision: 1.0", ""),
        (1, "", "error")
    ]
    hw_facts = hpux_hardware.get_hw_facts(collected_facts)
    assert hw_facts == {
        'model': 'test_model',
        'firmware_version': '1.0'
    }
