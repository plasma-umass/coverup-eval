# file: lib/ansible/module_utils/facts/hardware/sunos.py:282-286
# asked: {"lines": [282, 283, 284, 286], "branches": []}
# gained: {"lines": [282, 283, 284, 286], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.sunos import SunOSHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_sunos_hardware_collector_inheritance():
    # Ensure SunOSHardwareCollector inherits from HardwareCollector
    assert issubclass(SunOSHardwareCollector, HardwareCollector)

def test_sunos_hardware_collector_fact_class():
    # Ensure the _fact_class attribute is set correctly
    assert SunOSHardwareCollector._fact_class.__name__ == 'SunOSHardware'

def test_sunos_hardware_collector_platform():
    # Ensure the _platform attribute is set correctly
    assert SunOSHardwareCollector._platform == 'SunOS'

def test_sunos_hardware_collector_required_facts():
    # Ensure the required_facts attribute is set correctly
    assert SunOSHardwareCollector.required_facts == set(['platform'])
