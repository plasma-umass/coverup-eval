# file lib/ansible/module_utils/facts/hardware/openbsd.py:132-149
# lines [133, 134, 135, 136, 138, 146, 147, 149]
# branches ['135->136', '135->138']

import pytest
from unittest.mock import MagicMock

# Assuming the OpenBSDHardware class is part of a module named openbsd
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def mock_sysctl():
    return {
        'hw.ncpuonline': '2',
        'hw.model': 'Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz'
    }

@pytest.fixture
def openbsd_hardware(mock_sysctl):
    module_mock = MagicMock()
    hardware = OpenBSDHardware(module=module_mock)
    hardware.sysctl = mock_sysctl
    return hardware

def test_get_processor_facts(openbsd_hardware):
    expected_processor = [
        'Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz',
        'Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz'
    ]
    expected_processor_count = 2
    expected_processor_cores = 2

    cpu_facts = openbsd_hardware.get_processor_facts()

    assert cpu_facts['processor'] == expected_processor
    assert int(cpu_facts['processor_count']) == expected_processor_count
    assert int(cpu_facts['processor_cores']) == expected_processor_cores
