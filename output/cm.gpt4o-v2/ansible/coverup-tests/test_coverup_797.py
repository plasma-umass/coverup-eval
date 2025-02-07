# file: lib/ansible/module_utils/facts/virtual/linux.py:403-405
# asked: {"lines": [403, 404, 405], "branches": []}
# gained: {"lines": [403, 404, 405], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.linux import LinuxVirtualCollector, LinuxVirtual
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_linux_virtual_collector_inheritance():
    assert issubclass(LinuxVirtualCollector, VirtualCollector), "LinuxVirtualCollector should inherit from VirtualCollector"

def test_linux_virtual_collector_fact_class():
    assert LinuxVirtualCollector._fact_class is LinuxVirtual, "LinuxVirtualCollector._fact_class should be LinuxVirtual"

def test_linux_virtual_collector_platform():
    assert LinuxVirtualCollector._platform == 'Linux', "LinuxVirtualCollector._platform should be 'Linux'"
