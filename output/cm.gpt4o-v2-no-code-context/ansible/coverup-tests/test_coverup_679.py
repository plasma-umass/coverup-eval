# file: lib/ansible/module_utils/facts/hardware/hurd.py:51-53
# asked: {"lines": [51, 52, 53], "branches": []}
# gained: {"lines": [51, 52, 53], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.hurd import HurdHardwareCollector, HardwareCollector, HurdHardware

def test_hurd_hardware_collector_inheritance():
    assert issubclass(HurdHardwareCollector, HardwareCollector)

def test_hurd_hardware_collector_fact_class():
    assert HurdHardwareCollector._fact_class == HurdHardware

def test_hurd_hardware_collector_platform():
    assert HurdHardwareCollector._platform == 'GNU'
