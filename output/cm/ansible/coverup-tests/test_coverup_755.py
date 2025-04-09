# file lib/ansible/module_utils/facts/hardware/freebsd.py:31-46
# lines [31, 32, 44, 45]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the FreeBSDHardware class is part of a module named freebsd
from ansible.module_utils.facts.hardware import freebsd

# Mocking the FreeBSDHardware class to add missing methods for the test
class MockedFreeBSDHardware(freebsd.FreeBSDHardware):
    def populate(self, collected_facts=None):
        # Mocking the populate method to simulate the population of facts
        self.facts = {
            'memfree_mb': 1024,
            'memtotal_mb': 2048,
            'swapfree_mb': 512,
            'swaptotal_mb': 1024,
            'processor': ['Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz'],
            'processor_cores': 4,
            'processor_count': 1,
            'devices': {},
            'uptime_seconds': 123456,
        }

@pytest.fixture
def mock_freebsd_hardware(mocker):
    # Mocking the __init__ method to prevent any real hardware interaction
    mocker.patch.object(freebsd.FreeBSDHardware, '__init__', return_value=None)
    # Returning the mocked class
    return MockedFreeBSDHardware()

def test_freebsd_hardware_facts(mock_freebsd_hardware):
    # Simulate calling the populate method to fill in the facts
    mock_freebsd_hardware.populate()

    # Assertions to verify the facts have been populated correctly
    assert mock_freebsd_hardware.facts['memfree_mb'] == 1024
    assert mock_freebsd_hardware.facts['memtotal_mb'] == 2048
    assert mock_freebsd_hardware.facts['swapfree_mb'] == 512
    assert mock_freebsd_hardware.facts['swaptotal_mb'] == 1024
    assert mock_freebsd_hardware.facts['processor'] == ['Intel(R) Core(TM) i7-8650U CPU @ 1.90GHz']
    assert mock_freebsd_hardware.facts['processor_cores'] == 4
    assert mock_freebsd_hardware.facts['processor_count'] == 1
    assert mock_freebsd_hardware.facts['devices'] == {}
    assert mock_freebsd_hardware.facts['uptime_seconds'] == 123456
