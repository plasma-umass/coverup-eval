# file lib/ansible/module_utils/facts/virtual/netbsd.py:71-73
# lines [71, 72, 73]
# branches []

import pytest
from ansible.module_utils.facts.virtual.netbsd import NetBSDVirtualCollector

# Mocking the NetBSDVirtual class
class MockNetBSDVirtual:
    def populate(self, collected_facts):
        return {}

@pytest.fixture
def mock_netbsd_virtual(mocker):
    mocker.patch('ansible.module_utils.facts.virtual.netbsd.NetBSDVirtual', return_value=MockNetBSDVirtual())

def test_netbsd_virtual_collector(mock_netbsd_virtual):
    collector = NetBSDVirtualCollector()
    assert collector._platform == 'NetBSD'
    facts = collector.collect(None)
    assert isinstance(facts, dict)
