# file: lib/ansible/module_utils/facts/hardware/hurd.py:51-53
# asked: {"lines": [51, 52, 53], "branches": []}
# gained: {"lines": [51, 52, 53], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hurd import HurdHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_hurd_hardware_collector_inheritance():
    collector = HurdHardwareCollector()
    assert isinstance(collector, HardwareCollector)
    assert collector._platform == 'GNU'
    assert collector._fact_class.__name__ == 'HurdHardware'
