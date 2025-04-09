# file: lib/ansible/module_utils/facts/hardware/freebsd.py:239-241
# asked: {"lines": [239, 240, 241], "branches": []}
# gained: {"lines": [239, 240, 241], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardwareCollector
from ansible.module_utils.facts.hardware.base import HardwareCollector
from ansible.module_utils.facts.hardware.base import Hardware
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware

def test_freebsd_hardware_collector_inheritance():
    assert issubclass(FreeBSDHardwareCollector, HardwareCollector)
    assert FreeBSDHardwareCollector._fact_class == FreeBSDHardware
    assert FreeBSDHardwareCollector._platform == 'FreeBSD'

def test_freebsd_hardware_inheritance():
    assert issubclass(FreeBSDHardware, Hardware)
    assert FreeBSDHardware.platform == 'FreeBSD'
    assert FreeBSDHardware.DMESG_BOOT == '/var/run/dmesg.boot'
