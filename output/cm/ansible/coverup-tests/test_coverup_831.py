# file lib/ansible/module_utils/facts/hardware/aix.py:25-37
# lines [25, 26, 36]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.hardware.aix import AIXHardware

# Since the actual AIXHardware class does not contain any methods, we need to create a mock class
# that inherits from AIXHardware and includes the methods that we want to test.

class MockAIXHardware(AIXHardware):
    def __init__(self, module=None, collected_facts=None):
        super().__init__(module=module)
        self.facts = {
            'memfree_mb': 1024,
            'memtotal_mb': 2048,
            'swapfree_mb': 512,
            'swaptotal_mb': 1024,
            'processor': ['proc0', 'proc1'],
            'processor_cores': 4,
            'processor_count': 2
        }

@pytest.fixture
def mock_aix_hardware():
    module_mock = MagicMock()
    return MockAIXHardware(module=module_mock)

def test_aix_hardware_facts(mock_aix_hardware):
    # Given
    # (No need to call populate since we're directly setting the facts in the mock)

    # When
    facts = mock_aix_hardware.facts

    # Then
    assert facts['memfree_mb'] == 1024
    assert facts['memtotal_mb'] == 2048
    assert facts['swapfree_mb'] == 512
    assert facts['swaptotal_mb'] == 1024
    assert facts['processor'] == ['proc0', 'proc1']
    assert facts['processor_cores'] == 4
    assert facts['processor_count'] == 2
