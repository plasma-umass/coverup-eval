# file: lib/ansible/module_utils/facts/hardware/aix.py:250-252
# asked: {"lines": [250, 251, 252], "branches": []}
# gained: {"lines": [250, 251, 252], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.aix import AIXHardwareCollector, AIXHardware

def test_aix_hardware_collector_initialization():
    collector = AIXHardwareCollector()
    assert collector._platform == 'AIX'
    assert collector._fact_class == AIXHardware

@pytest.fixture
def mock_hardware_class(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.aix.AIXHardware', autospec=True)

def test_aix_hardware_collector_fact_class(mock_hardware_class):
    collector = AIXHardwareCollector()
    assert collector._fact_class == AIXHardware
