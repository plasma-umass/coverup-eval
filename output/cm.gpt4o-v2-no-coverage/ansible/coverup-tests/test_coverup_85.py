# file: lib/ansible/module_utils/facts/hardware/aix.py:57-84
# asked: {"lines": [57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 76, 77, 79, 80, 81, 82, 84], "branches": [[62, 63], [62, 84], [64, 66], [64, 72], [66, 64], [66, 67], [67, 68], [67, 71], [80, 81], [80, 84]]}
# gained: {"lines": [57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 74, 76, 77, 79, 80, 81, 82, 84], "branches": [[62, 63], [62, 84], [64, 66], [64, 72], [66, 67], [67, 68], [67, 71], [80, 81], [80, 84]]}

import pytest
from unittest.mock import MagicMock

from ansible.module_utils.facts.hardware.aix import AIXHardware

@pytest.fixture
def module_mock():
    return MagicMock()

@pytest.fixture
def aix_hardware(module_mock):
    return AIXHardware(module_mock)

def test_get_cpu_facts_no_output(aix_hardware, module_mock):
    module_mock.run_command.return_value = (0, '', '')
    result = aix_hardware.get_cpu_facts()
    assert result == {'processor': []}

def test_get_cpu_facts_with_output(aix_hardware, module_mock):
    module_mock.run_command.side_effect = [
        (0, 'proc0 Available\nproc1 Available\n', ''),
        (0, 'type PowerPC_POWER8', ''),
        (0, 'smt_threads 8', '')
    ]
    result = aix_hardware.get_cpu_facts()
    assert result == {
        'processor': 'PowerPC_POWER8',
        'processor_count': 2,
        'processor_cores': 8
    }

def test_get_cpu_facts_partial_output(aix_hardware, module_mock):
    module_mock.run_command.side_effect = [
        (0, 'proc0 Available\nproc1 Available\n', ''),
        (0, 'type PowerPC_POWER8', ''),
        (0, '', '')
    ]
    result = aix_hardware.get_cpu_facts()
    assert result == {
        'processor': 'PowerPC_POWER8',
        'processor_count': 2
    }
