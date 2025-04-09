# file: lib/ansible/module_utils/facts/virtual/linux.py:403-405
# asked: {"lines": [403, 404, 405], "branches": []}
# gained: {"lines": [403, 404, 405], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.linux import LinuxVirtualCollector, LinuxVirtual
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_linux_virtual_collector_initialization():
    collector = LinuxVirtualCollector()
    assert collector._fact_class == LinuxVirtual
    assert collector._platform == 'Linux'
    assert isinstance(collector, VirtualCollector)
