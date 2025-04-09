# file: lib/ansible/module_utils/facts/hardware/hpux.py:161-165
# asked: {"lines": [161, 162, 163, 165], "branches": []}
# gained: {"lines": [161, 162, 163, 165], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector

def test_hpux_hardware_collector_class_attributes():
    assert HPUXHardwareCollector._fact_class.__name__ == 'HPUXHardware'
    assert HPUXHardwareCollector._platform == 'HP-UX'
    assert HPUXHardwareCollector.required_facts == {'platform', 'distribution'}
