# file lib/ansible/module_utils/facts/virtual/linux.py:403-405
# lines [403, 404, 405]
# branches []

import pytest
from ansible.module_utils.facts.virtual.linux import LinuxVirtualCollector

# Mocking the LinuxVirtual class to test the LinuxVirtualCollector
class MockLinuxVirtual:
    pass

@pytest.fixture
def linux_virtual_collector(mocker):
    mocker.patch.object(LinuxVirtualCollector, '_fact_class', new=MockLinuxVirtual)
    return LinuxVirtualCollector()

def test_linux_virtual_collector_initialization(linux_virtual_collector):
    assert linux_virtual_collector._fact_class is MockLinuxVirtual
    assert linux_virtual_collector._platform == 'Linux'
