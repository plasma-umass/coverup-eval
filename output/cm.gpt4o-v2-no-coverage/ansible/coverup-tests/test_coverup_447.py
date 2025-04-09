# file: lib/ansible/module_utils/facts/hardware/openbsd.py:132-149
# asked: {"lines": [132, 133, 134, 135, 136, 138, 146, 147, 149], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [132, 133, 134, 135, 136, 138, 146, 147, 149], "branches": [[135, 136], [135, 138]]}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

@pytest.fixture
def mock_sysctl():
    return {
        'hw.ncpuonline': '4',
        'hw.model': 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    }

def test_get_processor_facts(monkeypatch, mock_sysctl):
    def mock_init(self):
        self.sysctl = mock_sysctl

    monkeypatch.setattr(OpenBSDHardware, '__init__', mock_init)
    
    hardware = OpenBSDHardware()
    cpu_facts = hardware.get_processor_facts()
    
    assert cpu_facts['processor'] == [
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz',
        'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    ]
    assert cpu_facts['processor_count'] == '4'
    assert cpu_facts['processor_cores'] == '4'
