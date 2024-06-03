# file lib/ansible/module_utils/facts/hardware/hpux.py:142-158
# lines [142, 143, 144, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158]
# branches ['148->149', '148->158', '150->151', '150->152', '155->156', '155->158']

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

@pytest.fixture
def mock_module(mocker):
    module = mocker.MagicMock()
    return module

def test_get_hw_facts_ia64_version_B_11_23(mock_module):
    hw = HPUXHardware(mock_module)

    mock_module.run_command.side_effect = [
        (0, "model_output", ""),  # First run_command call for "model"
        (0, "Firmware revision=1.2.3", ""),  # Second run_command call for firmware version
        (0, "Machine serial number=123456", "")  # Third run_command call for product serial
    ]

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.23'
    }

    hw_facts = hw.get_hw_facts(collected_facts)

    assert hw_facts['model'] == "model_output"
    assert hw_facts['firmware_version'] == "1.2.3"
    assert hw_facts['product_serial'] == "123456"

def test_get_hw_facts_ia64_other_version(mock_module):
    hw = HPUXHardware(mock_module)

    mock_module.run_command.side_effect = [
        (0, "model_output", ""),  # First run_command call for "model"
        (0, "Firmware revision: 1.2.3", ""),  # Second run_command call for firmware version
        (0, "Machine serial number: 123456", "")  # Third run_command call for product serial
    ]

    collected_facts = {
        'ansible_architecture': 'ia64',
        'ansible_distribution_version': 'B.11.31'
    }

    hw_facts = hw.get_hw_facts(collected_facts)

    assert hw_facts['model'] == "model_output"
    assert hw_facts['firmware_version'] == "1.2.3"
    assert hw_facts['product_serial'] == "123456"

def test_get_hw_facts_non_ia64(mock_module):
    hw = HPUXHardware(mock_module)

    mock_module.run_command.side_effect = [
        (0, "model_output", "")  # First run_command call for "model"
    ]

    collected_facts = {
        'ansible_architecture': 'x86_64',
    }

    hw_facts = hw.get_hw_facts(collected_facts)

    assert hw_facts['model'] == "model_output"
    assert 'firmware_version' not in hw_facts
    assert 'product_serial' not in hw_facts
