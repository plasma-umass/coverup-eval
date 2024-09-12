# file: lib/ansible/module_utils/facts/hardware/hpux.py:161-165
# asked: {"lines": [161, 162, 163, 165], "branches": []}
# gained: {"lines": [161, 162, 163, 165], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector, HPUXHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_hpux_hardware_collector_initialization():
    collector = HPUXHardwareCollector()
    assert collector._fact_class == HPUXHardware
    assert collector._platform == 'HP-UX'
    assert collector.required_facts == {'platform', 'distribution'}

@pytest.fixture
def mock_hardware_collector(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.hpux.HPUXHardwareCollector.__init__', return_value=None)
    return HPUXHardwareCollector()

def test_hpux_hardware_collector_required_facts(mock_hardware_collector):
    assert mock_hardware_collector.required_facts == {'platform', 'distribution'}
