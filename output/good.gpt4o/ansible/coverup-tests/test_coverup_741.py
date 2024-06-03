# file lib/ansible/module_utils/facts/virtual/linux.py:403-405
# lines [403, 404, 405]
# branches []

import pytest
from ansible.module_utils.facts.virtual.linux import LinuxVirtualCollector, LinuxVirtual
from ansible.module_utils.facts.virtual.base import VirtualCollector

def test_linux_virtual_collector():
    # Ensure the class is correctly inheriting from VirtualCollector
    assert issubclass(LinuxVirtualCollector, VirtualCollector)
    
    # Ensure the _fact_class attribute is set correctly
    assert LinuxVirtualCollector._fact_class == LinuxVirtual
    
    # Ensure the _platform attribute is set correctly
    assert LinuxVirtualCollector._platform == 'Linux'
