# file: lib/ansible/module_utils/facts/hardware/darwin.py:157-159
# asked: {"lines": [157, 158, 159], "branches": []}
# gained: {"lines": [157, 158, 159], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_darwin_hardware_collector_inheritance():
    # Ensure DarwinHardwareCollector inherits from HardwareCollector
    assert issubclass(DarwinHardwareCollector, HardwareCollector)

def test_darwin_hardware_collector_fact_class():
    # Ensure the _fact_class attribute is set correctly
    assert DarwinHardwareCollector._fact_class.__name__ == 'DarwinHardware'

def test_darwin_hardware_collector_platform():
    # Ensure the _platform attribute is set correctly
    assert DarwinHardwareCollector._platform == 'Darwin'
