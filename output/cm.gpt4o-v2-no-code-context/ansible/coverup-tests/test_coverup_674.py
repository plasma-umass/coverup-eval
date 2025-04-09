# file: lib/ansible/module_utils/facts/virtual/sunos.py:137-139
# asked: {"lines": [137, 138, 139], "branches": []}
# gained: {"lines": [137, 138, 139], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.sunos import SunOSVirtualCollector, SunOSVirtual
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_sunos_virtual_collector_class_attributes():
    assert issubclass(SunOSVirtualCollector, VirtualCollector)
    assert SunOSVirtualCollector._fact_class is SunOSVirtual
    assert SunOSVirtualCollector._platform == 'SunOS'
