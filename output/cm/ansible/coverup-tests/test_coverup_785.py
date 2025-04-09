# file lib/ansible/module_utils/facts/hardware/openbsd.py:182-184
# lines [182, 183, 184]
# branches []

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardwareCollector

# Since the class OpenBSDHardwareCollector does not contain any methods,
# we will create a test that simply instantiates it and checks its attributes.

def test_openbsd_hardware_collector_instantiation():
    collector = OpenBSDHardwareCollector()
    assert collector._fact_class.__name__ == "OpenBSDHardware"
    assert collector._platform == "OpenBSD"
