# file: lib/ansible/module_utils/facts/hardware/openbsd.py:182-184
# asked: {"lines": [182, 183, 184], "branches": []}
# gained: {"lines": [182, 183, 184], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardwareCollector

def test_openbsd_hardware_collector_class_attributes():
    assert OpenBSDHardwareCollector._fact_class.__name__ == 'OpenBSDHardware'
    assert OpenBSDHardwareCollector._platform == 'OpenBSD'
