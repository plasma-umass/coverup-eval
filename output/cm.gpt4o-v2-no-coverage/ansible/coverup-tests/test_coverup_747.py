# file: lib/ansible/module_utils/facts/hardware/hpux.py:161-165
# asked: {"lines": [161, 162, 163, 165], "branches": []}
# gained: {"lines": [161, 162, 163, 165], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector, HPUXHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

@pytest.fixture
def mock_hardware_collector(mocker):
    mocker.patch('ansible.module_utils.facts.hardware.hpux.HPUXHardwareCollector._fact_class', HPUXHardware)
    mocker.patch('ansible.module_utils.facts.hardware.hpux.HPUXHardwareCollector._platform', 'HP-UX')
    return HPUXHardwareCollector()

def test_hpux_hardware_collector_initialization(mock_hardware_collector):
    assert mock_hardware_collector._fact_class == HPUXHardware
    assert mock_hardware_collector._platform == 'HP-UX'
    assert mock_hardware_collector.required_facts == set(['platform', 'distribution'])

def test_hpux_hardware_collector_collect(mocker, mock_hardware_collector):
    mocker.patch.object(HardwareCollector, 'collect', return_value={'platform': 'HP-UX', 'distribution': 'HP-UX'})
    collected_facts = mock_hardware_collector.collect()
    assert collected_facts == {'platform': 'HP-UX', 'distribution': 'HP-UX'}
