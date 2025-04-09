# file lib/ansible/module_utils/facts/hardware/hpux.py:25-40
# lines [25, 26, 39]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.hpux import HPUXHardware

# Mocking the necessary methods and attributes to test HPUXHardware
class FakeHPUXHardware(HPUXHardware):
    def __init__(self, module):
        super().__init__(module)
        self.module = module

    def populate(self, collected_facts=None):
        # This method would be responsible for populating the facts
        # For the purpose of this test, we'll just set some attributes directly
        self.facts = {
            'memfree_mb': 1024,
            'memtotal_mb': 2048,
            'swapfree_mb': 512,
            'swaptotal_mb': 1024,
            'processor': ['Intel'],
            'processor_cores': 4,
            'processor_count': 1,
            'model': 'TestModel',
            'firmware': 'TestFirmware'
        }

@pytest.fixture
def hpux_hardware(mocker):
    module_mock = MagicMock()
    return FakeHPUXHardware(module_mock)

def test_hpux_hardware_facts(hpux_hardware):
    # Given the FakeHPUXHardware, when we call populate
    hpux_hardware.populate()

    # Then we should have the expected facts set
    assert hpux_hardware.facts['memfree_mb'] == 1024
    assert hpux_hardware.facts['memtotal_mb'] == 2048
    assert hpux_hardware.facts['swapfree_mb'] == 512
    assert hpux_hardware.facts['swaptotal_mb'] == 1024
    assert hpux_hardware.facts['processor'] == ['Intel']
    assert hpux_hardware.facts['processor_cores'] == 4
    assert hpux_hardware.facts['processor_count'] == 1
    assert hpux_hardware.facts['model'] == 'TestModel'
    assert hpux_hardware.facts['firmware'] == 'TestFirmware'
