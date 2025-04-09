# file: lib/ansible/module_utils/facts/hardware/aix.py:250-252
# asked: {"lines": [250, 251, 252], "branches": []}
# gained: {"lines": [250, 251, 252], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.aix import AIXHardwareCollector
from ansible.module_utils.facts.hardware.aix import AIXHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector, Hardware

def test_aix_hardware_collector_inheritance():
    assert issubclass(AIXHardwareCollector, HardwareCollector)
    assert AIXHardwareCollector._platform == 'AIX'
    assert AIXHardwareCollector._fact_class == AIXHardware

def test_aix_hardware_inheritance():
    assert issubclass(AIXHardware, Hardware)
    assert AIXHardware.platform == 'AIX'
