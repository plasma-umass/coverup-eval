# file: lib/ansible/module_utils/facts/hardware/freebsd.py:239-241
# asked: {"lines": [239, 240, 241], "branches": []}
# gained: {"lines": [239, 240, 241], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardwareCollector, FreeBSDHardware

def test_freebsd_hardware_collector():
    # Ensure the class attributes are set correctly
    assert FreeBSDHardwareCollector._fact_class == FreeBSDHardware
    assert FreeBSDHardwareCollector._platform == 'FreeBSD'
