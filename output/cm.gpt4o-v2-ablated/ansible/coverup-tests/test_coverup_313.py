# file: lib/ansible/module_utils/facts/hardware/aix.py:250-252
# asked: {"lines": [250, 251, 252], "branches": []}
# gained: {"lines": [250, 251, 252], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.aix import AIXHardwareCollector, AIXHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_aix_hardware_collector_inheritance():
    collector = AIXHardwareCollector()
    assert isinstance(collector, HardwareCollector)
    assert collector._platform == 'AIX'
    assert collector._fact_class == AIXHardware

def test_aix_hardware_collector_platform():
    collector = AIXHardwareCollector()
    assert collector._platform == 'AIX'

def test_aix_hardware_collector_fact_class():
    collector = AIXHardwareCollector()
    assert collector._fact_class == AIXHardware
