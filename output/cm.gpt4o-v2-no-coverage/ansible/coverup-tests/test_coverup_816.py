# file: lib/ansible/module_utils/facts/hardware/openbsd.py:182-184
# asked: {"lines": [182, 183, 184], "branches": []}
# gained: {"lines": [182, 183, 184], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

def test_openbsd_hardware_collector_inheritance():
    assert issubclass(OpenBSDHardwareCollector, HardwareCollector)

def test_openbsd_hardware_collector_fact_class():
    assert OpenBSDHardwareCollector._fact_class == OpenBSDHardware

def test_openbsd_hardware_collector_platform():
    assert OpenBSDHardwareCollector._platform == 'OpenBSD'
