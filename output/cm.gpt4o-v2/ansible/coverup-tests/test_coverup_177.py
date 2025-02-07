# file: lib/ansible/module_utils/facts/hardware/hpux.py:142-158
# asked: {"lines": [142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158], "branches": [[148, 149], [148, 158], [150, 151], [150, 152], [155, 156], [155, 158]]}
# gained: {"lines": [142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158], "branches": [[148, 149], [148, 158], [150, 151], [150, 152], [155, 156], [155, 158]]}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def hpux_hardware():
    from ansible.module_utils.facts.hardware.hpux import HPUXHardware
    module = MagicMock()
    hpux = HPUXHardware(module)
    return hpux

def test_get_hw_facts_model(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(return_value=(0, "HP-UX Model", ""))
    hw_facts = hpux_hardware.get_hw_facts()
    assert hw_facts['model'] == "HP-UX Model"

def test_get_hw_facts_ia64(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(side_effect=[
        (0, "HP-UX Model", ""),
        (0, "Firmware revision: 1.2.3", ""),
        (0, "Machine serial number: ABC123", "")
    ])
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    hw_facts = hpux_hardware.get_hw_facts(collected_facts)
    assert hw_facts['model'] == "HP-UX Model"
    assert hw_facts['firmware_version'] == "1.2.3"
    assert hw_facts['product_serial'] == "ABC123"

def test_get_hw_facts_ia64_b1123(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(side_effect=[
        (0, "HP-UX Model", ""),
        (0, "Firmware revision= 1.2.3", ""),
        (0, "Machine serial number= ABC123", "")
    ])
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }
    hw_facts = hpux_hardware.get_hw_facts(collected_facts)
    assert hw_facts['model'] == "HP-UX Model"
    assert hw_facts['firmware_version'] == "1.2.3"
    assert hw_facts['product_serial'] == "ABC123"

def test_get_hw_facts_no_serial(hpux_hardware):
    hpux_hardware.module.run_command = MagicMock(side_effect=[
        (0, "HP-UX Model", ""),
        (0, "Firmware revision: 1.2.3", ""),
        (1, "", "Error")
    ])
    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }
    hw_facts = hpux_hardware.get_hw_facts(collected_facts)
    assert hw_facts['model'] == "HP-UX Model"
    assert hw_facts['firmware_version'] == "1.2.3"
    assert 'product_serial' not in hw_facts
