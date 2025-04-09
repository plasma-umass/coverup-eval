# file: lib/ansible/module_utils/facts/hardware/openbsd.py:182-184
# asked: {"lines": [182, 183, 184], "branches": []}
# gained: {"lines": [182, 183, 184], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_openbsd_hardware_collector_inheritance():
    collector = OpenBSDHardwareCollector()
    assert isinstance(collector, HardwareCollector)

def test_openbsd_hardware_collector_fact_class():
    assert OpenBSDHardwareCollector._fact_class.__name__ == 'OpenBSDHardware'

def test_openbsd_hardware_collector_platform():
    assert OpenBSDHardwareCollector._platform == 'OpenBSD'
