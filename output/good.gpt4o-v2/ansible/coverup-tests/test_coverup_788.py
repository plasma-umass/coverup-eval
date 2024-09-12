# file: lib/ansible/module_utils/facts/hardware/darwin.py:157-159
# asked: {"lines": [157, 158, 159], "branches": []}
# gained: {"lines": [157, 158, 159], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.darwin import DarwinHardwareCollector, DarwinHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_darwin_hardware_collector_inheritance():
    assert issubclass(DarwinHardwareCollector, HardwareCollector), "DarwinHardwareCollector should inherit from HardwareCollector"

def test_darwin_hardware_collector_fact_class():
    assert DarwinHardwareCollector._fact_class is DarwinHardware, "DarwinHardwareCollector should have _fact_class set to DarwinHardware"

def test_darwin_hardware_collector_platform():
    assert DarwinHardwareCollector._platform == 'Darwin', "DarwinHardwareCollector should have _platform set to 'Darwin'"
