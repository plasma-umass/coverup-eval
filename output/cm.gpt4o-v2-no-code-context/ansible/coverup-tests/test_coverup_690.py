# file: lib/ansible/module_utils/facts/hardware/freebsd.py:239-241
# asked: {"lines": [239, 240, 241], "branches": []}
# gained: {"lines": [239, 240, 241], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardwareCollector, FreeBSDHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_FreeBSDHardwareCollector_inheritance():
    collector = FreeBSDHardwareCollector()
    assert isinstance(collector, FreeBSDHardwareCollector)
    assert isinstance(collector, HardwareCollector)

def test_FreeBSDHardwareCollector_fact_class():
    collector = FreeBSDHardwareCollector()
    assert collector._fact_class == FreeBSDHardware

def test_FreeBSDHardwareCollector_platform():
    collector = FreeBSDHardwareCollector()
    assert collector._platform == 'FreeBSD'
