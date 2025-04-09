# file lib/ansible/module_utils/facts/hardware/aix.py:250-252
# lines [250, 251, 252]
# branches []

import pytest
from ansible.module_utils.facts.hardware.aix import AIXHardwareCollector, AIXHardware

# Mocking AIXHardware to avoid any side effects
class MockAIXHardware(AIXHardware):
    def populate(self, collected_facts=None):
        return {}

@pytest.fixture
def mock_aix_hardware(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.aix.AIXHardware', MockAIXHardware)

def test_aix_hardware_collector_initialization(mock_aix_hardware):
    collector = AIXHardwareCollector()
    assert collector._platform == 'AIX'
    assert issubclass(collector._fact_class, AIXHardware)
