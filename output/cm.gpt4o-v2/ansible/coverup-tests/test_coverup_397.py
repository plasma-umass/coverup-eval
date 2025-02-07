# file: lib/ansible/module_utils/facts/hardware/openbsd.py:132-149
# asked: {"lines": [132, 133, 134, 135, 136, 138, 146, 147, 149], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [132, 133, 134, 135, 136, 138, 146, 147, 149], "branches": [[135, 136], [135, 138]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def openbsd_hardware():
    module = MagicMock()
    hardware = OpenBSDHardware(module)
    hardware.sysctl = {
        'hw.ncpuonline': '4',
        'hw.model': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    }
    return hardware

def test_get_processor_facts(openbsd_hardware):
    cpu_facts = openbsd_hardware.get_processor_facts()
    
    assert cpu_facts['processor'] == [
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    ]
    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor_cores'] == '4'
