# file: lib/ansible/module_utils/facts/hardware/hurd.py:51-53
# asked: {"lines": [51, 52, 53], "branches": []}
# gained: {"lines": [51, 52, 53], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hurd import HurdHardwareCollector, HurdHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_hurd_hardware_collector_inheritance():
    collector = HurdHardwareCollector()
    assert isinstance(collector, HardwareCollector)
    assert collector._fact_class == HurdHardware
    assert collector._platform == 'GNU'

def test_hurd_hardware_collector_fact_class():
    collector = HurdHardwareCollector()
    assert collector._fact_class == HurdHardware

def test_hurd_hardware_collector_platform():
    collector = HurdHardwareCollector()
    assert collector._platform == 'GNU'
