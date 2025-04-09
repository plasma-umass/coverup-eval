# file: lib/ansible/module_utils/facts/hardware/openbsd.py:132-149
# asked: {"lines": [133, 134, 135, 136, 138, 146, 147, 149], "branches": [[135, 136], [135, 138]]}
# gained: {"lines": [133, 134, 135, 136, 138, 146, 147, 149], "branches": [[135, 136], [135, 138]]}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware
from ansible.module_utils.basic import AnsibleModule
import json
import sys

class MockSysctl:
    def __init__(self, ncpuonline, model):
        self.data = {
            'hw.ncpuonline': ncpuonline,
            'hw.model': model
        }

    def __getitem__(self, item):
        return self.data[item]

@pytest.fixture
def mock_sysctl():
    return MockSysctl(ncpuonline=4, model='Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz')

@pytest.fixture
def openbsd_hardware(mock_sysctl, monkeypatch):
    def mock_load_params():
        return {}

    monkeypatch.setattr('ansible.module_utils.basic._load_params', mock_load_params)
    module = AnsibleModule(argument_spec={})
    hardware = OpenBSDHardware(module)
    hardware.sysctl = mock_sysctl
    return hardware

def test_get_processor_facts(openbsd_hardware):
    cpu_facts = openbsd_hardware.get_processor_facts()
    
    assert 'processor' in cpu_facts
    assert len(cpu_facts['processor']) == 4
    assert cpu_facts['processor'][0] == 'Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz'
    assert cpu_facts['processor_count'] == 4
    assert cpu_facts['processor_cores'] == 4
