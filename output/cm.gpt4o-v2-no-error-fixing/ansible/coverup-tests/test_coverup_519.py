# file: lib/ansible/module_utils/facts/virtual/linux.py:403-405
# asked: {"lines": [403, 404, 405], "branches": []}
# gained: {"lines": [403, 404, 405], "branches": []}

import pytest
from ansible.module_utils.facts.virtual.linux import LinuxVirtualCollector, LinuxVirtual

def test_linux_virtual_collector():
    # Ensure the class attributes are set correctly
    assert LinuxVirtualCollector._fact_class is LinuxVirtual
    assert LinuxVirtualCollector._platform == 'Linux'
