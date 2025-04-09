# file: lib/ansible/module_utils/facts/hardware/hpux.py:161-165
# asked: {"lines": [161, 162, 163, 165], "branches": []}
# gained: {"lines": [161, 162, 163, 165], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hpux import HPUXHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_hpux_hardware_collector_inheritance():
    collector = HPUXHardwareCollector()
    assert isinstance(collector, HardwareCollector)

def test_hpux_hardware_collector_fact_class():
    collector = HPUXHardwareCollector()
    assert collector._fact_class.__name__ == 'HPUXHardware'

def test_hpux_hardware_collector_platform():
    collector = HPUXHardwareCollector()
    assert collector._platform == 'HP-UX'

def test_hpux_hardware_collector_required_facts():
    collector = HPUXHardwareCollector()
    assert collector.required_facts == {'platform', 'distribution'}
