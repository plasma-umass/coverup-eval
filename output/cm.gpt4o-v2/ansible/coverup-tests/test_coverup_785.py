# file: lib/ansible/module_utils/facts/hardware/hurd.py:51-53
# asked: {"lines": [51, 52, 53], "branches": []}
# gained: {"lines": [51, 52, 53], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hurd import HurdHardwareCollector, HurdHardware

def test_hurd_hardware_collector_initialization():
    collector = HurdHardwareCollector()
    assert collector._fact_class == HurdHardware
    assert collector._platform == 'GNU'
