# file lib/ansible/module_utils/facts/virtual/dragonfly.py:22-25
# lines [22, 24, 25]
# branches []

import pytest
from ansible.module_utils.facts.virtual.dragonfly import DragonFlyVirtualCollector
from ansible.module_utils.facts.virtual.freebsd import FreeBSDVirtual

# Mocking the FreeBSDVirtual class to ensure it can be instantiated without side effects
class MockFreeBSDVirtual(FreeBSDVirtual):
    def populate(self, collected_facts=None):
        return {}

@pytest.fixture
def mock_freebsd_virtual(mocker):
    mocker.patch('ansible.module_utils.facts.virtual.dragonfly.FreeBSDVirtual', new=MockFreeBSDVirtual)

def test_dragonfly_virtual_collector_instantiation(mock_freebsd_virtual):
    collector = DragonFlyVirtualCollector()
    assert isinstance(collector, DragonFlyVirtualCollector)
    assert collector._platform == 'DragonFly'
    assert issubclass(collector._fact_class, FreeBSDVirtual)
