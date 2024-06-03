# file lib/ansible/module_utils/facts/hardware/openbsd.py:182-184
# lines [182, 183, 184]
# branches []

import pytest
from ansible.module_utils.facts.hardware.openbsd import OpenBSDHardwareCollector, HardwareCollector, OpenBSDHardware

def test_openbsd_hardware_collector():
    # Verify that OpenBSDHardwareCollector is a subclass of HardwareCollector
    assert issubclass(OpenBSDHardwareCollector, HardwareCollector)
    
    # Verify that the _fact_class attribute is set correctly
    assert OpenBSDHardwareCollector._fact_class is OpenBSDHardware
    
    # Verify that the _platform attribute is set correctly
    assert OpenBSDHardwareCollector._platform == 'OpenBSD'
