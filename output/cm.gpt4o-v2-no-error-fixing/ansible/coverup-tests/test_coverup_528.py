# file: lib/ansible/module_utils/facts/hardware/freebsd.py:239-241
# asked: {"lines": [239, 240, 241], "branches": []}
# gained: {"lines": [239, 240, 241], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardwareCollector, FreeBSDHardware

def test_freebsd_hardware_collector():
    # Ensure the class is correctly set up
    assert FreeBSDHardwareCollector._fact_class == FreeBSDHardware
    assert FreeBSDHardwareCollector._platform == 'FreeBSD'

    # Create an instance and verify it is an instance of HardwareCollector
    collector = FreeBSDHardwareCollector()
    assert isinstance(collector, FreeBSDHardwareCollector)
    assert isinstance(collector, FreeBSDHardwareCollector.__bases__[0])  # Check if it's a subclass of HardwareCollector
