# file lib/ansible/module_utils/facts/hardware/hpux.py:161-165
# lines [161, 162, 163, 165]
# branches []

import pytest
from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector

def test_hpux_hardware_collector_initialization():
    collector = HPUXHardwareCollector()
    assert collector._fact_class.__name__ == 'HPUXHardware'
    assert collector._platform == 'HP-UX'
    assert collector.required_facts == {'platform', 'distribution'}
