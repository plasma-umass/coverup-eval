# file: lib/ansible/module_utils/facts/hardware/dragonfly.py:23-26
# asked: {"lines": [23, 25, 26], "branches": []}
# gained: {"lines": [23, 25, 26], "branches": []}

import pytest
from ansible.module_utils.facts.hardware.dragonfly import DragonFlyHardwareCollector
from ansible.module_utils.facts.hardware.freebsd import FreeBSDHardware
from ansible.module_utils.facts.hardware.base import HardwareCollector

def test_dragonfly_hardware_collector_inheritance():
    assert issubclass(DragonFlyHardwareCollector, HardwareCollector)

def test_dragonfly_hardware_collector_fact_class():
    assert DragonFlyHardwareCollector._fact_class is FreeBSDHardware

def test_dragonfly_hardware_collector_platform():
    assert DragonFlyHardwareCollector._platform == 'DragonFly'
