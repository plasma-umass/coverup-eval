# file: lib/ansible/module_utils/facts/hardware/openbsd.py:151-157
# asked: {"lines": [151, 152, 153, 154, 155, 157], "branches": []}
# gained: {"lines": [151, 152, 153, 154, 155, 157], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

class MockHardware:
    def __init__(self, sysctl):
        self.sysctl = sysctl

@pytest.fixture
def mock_hardware():
    sysctl = {'hw.disknames': 'sd0,sd1,sd2'}
    return MockHardware(sysctl)

def test_get_device_facts(mock_hardware, monkeypatch):
    def mock_init(self, sysctl):
        self.sysctl = sysctl

    monkeypatch.setattr(OpenBSDHardware, '__init__', mock_init)
    openbsd_hardware = OpenBSDHardware(mock_hardware.sysctl)
    device_facts = openbsd_hardware.get_device_facts()
    
    assert 'devices' in device_facts
    assert device_facts['devices'] == ['sd0', 'sd1', 'sd2']
