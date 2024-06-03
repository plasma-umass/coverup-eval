# file lib/ansible/module_utils/facts/hardware/aix.py:250-252
# lines [250, 251, 252]
# branches []

import pytest
from ansible.module_utils.facts.hardware.aix import AIXHardwareCollector, HardwareCollector, AIXHardware

def test_aix_hardware_collector_initialization():
    collector = AIXHardwareCollector()
    assert collector._platform == 'AIX'
    assert isinstance(collector, HardwareCollector)
    assert collector._fact_class == AIXHardware
