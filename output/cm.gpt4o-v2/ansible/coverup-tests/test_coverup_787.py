# file: lib/ansible/module_utils/facts/hardware/openbsd.py:182-184
# asked: {"lines": [182, 183, 184], "branches": []}
# gained: {"lines": [182, 183, 184], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardware

def test_openbsd_hardware_collector_inheritance():
    assert issubclass(OpenBSDHardwareCollector, HardwareCollector), "OpenBSDHardwareCollector should inherit from HardwareCollector"

def test_openbsd_hardware_collector_fact_class():
    assert OpenBSDHardwareCollector._fact_class == OpenBSDHardware, "OpenBSDHardwareCollector should have _fact_class set to OpenBSDHardware"

def test_openbsd_hardware_collector_platform():
    assert OpenBSDHardwareCollector._platform == 'OpenBSD', "OpenBSDHardwareCollector should have _platform set to 'OpenBSD'"
