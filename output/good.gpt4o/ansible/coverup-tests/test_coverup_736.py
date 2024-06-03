# file lib/ansible/module_utils/facts/hardware/freebsd.py:239-241
# lines [239, 240, 241]
# branches []

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardwareCollector, FreeBSDHardware

def test_freebsd_hardware_collector_initialization():
    collector = FreeBSDHardwareCollector()
    assert collector._fact_class == FreeBSDHardware
    assert collector._platform == 'FreeBSD'
