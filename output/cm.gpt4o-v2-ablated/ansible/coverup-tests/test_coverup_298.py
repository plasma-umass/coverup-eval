# file: lib/ansible/module_utils/facts/virtual/linux.py:403-405
# asked: {"lines": [403, 404, 405], "branches": []}
# gained: {"lines": [403, 404, 405], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.linux import LinuxVirtualCollector, VirtualCollector, LinuxVirtual

def test_linux_virtual_collector_inheritance():
    collector = LinuxVirtualCollector()
    assert isinstance(collector, VirtualCollector)
    assert collector._fact_class == LinuxVirtual
    assert collector._platform == 'Linux'
